import { test, expect, type Page } from '@playwright/test';

async function fresh(page: Page) {
  await page.goto('./');
  await page.evaluate(() => localStorage.clear());
}

test('completes a short practice session with keyboard answers and feedback', async ({ page }) => {
  await fresh(page);
  await page.goto('./#/practice');
  await expect(page.getByRole('heading', { name: 'Practice' })).toBeVisible();
  await page.getByRole('button', { name: '5', exact: true }).click();
  await page.getByRole('button', { name: /Start practice/ }).click();

  for (let i = 0; i < 5; i++) {
    await expect(page.getByText(`Question ${i + 1} of 5`)).toBeVisible();
    // answer with the keyboard (1–4), check the feedback and the solution appear
    await page.keyboard.press(String((i % 4) + 1));
    await expect(page.getByText(/✓ Correct|✗ Not quite/)).toBeVisible();
    await expect(page.getByText('Solution', { exact: true })).toBeVisible();
    // KaTeX rendered somewhere in the card
    expect(await page.locator('.qcard .katex').count()).toBeGreaterThan(0);
    await page.keyboard.press('Enter');
  }
  await expect(page.getByRole('heading', { name: 'Session complete' })).toBeVisible();
  // progress is stored
  const stored = await page.evaluate(() => JSON.parse(localStorage.getItem('csca.v1') || '{}'));
  expect(stored.attempts.length).toBe(5);
});

test('takes a full mock exam: navigator, flag, submit, score and review', async ({ page }) => {
  await fresh(page);
  await page.goto('./#/mock');
  await page.getByRole('button', { name: 'Start random mock' }).click();
  await expect(page.getByText('Question 1 of 48')).toBeVisible();
  await expect(page.getByRole('timer')).toContainText(/59:5\d|1:00:00|60:00/);

  // answer the first 10 questions; no feedback must be shown during the exam
  for (let i = 0; i < 10; i++) {
    await page.locator('.option').first().click();
    await expect(page.getByText(/✓ Correct|✗ Not quite/)).toHaveCount(0);
    await page.getByRole('button', { name: 'Next →' }).first().click();
  }
  // flag question 11 and jump with the navigator
  await page.getByRole('button', { name: /Flag/ }).click();
  await page.getByRole('button', { name: 'Question 48' }).click();
  await expect(page.getByText('Question 48 of 48')).toBeVisible();
  await page.getByRole('button', { name: 'Question 11, flagged' }).click();
  await expect(page.getByText('Question 11 of 48')).toBeVisible();

  await page.getByRole('button', { name: 'Submit', exact: true }).click();
  await expect(page.getByText(/38 question\(s\) are unanswered/)).toBeVisible();
  await page.getByRole('button', { name: 'Yes, submit' }).click();

  await expect(page.getByText(/score out of 100/)).toBeVisible();
  await expect(page.getByRole('heading', { name: 'Per-topic breakdown' })).toBeVisible();
  await expect(page.getByText(/Time spent: \d+ s/).first()).toBeVisible();
  // the review shows solutions
  expect(await page.getByText('Solution', { exact: true }).count()).toBeGreaterThan(0);

  // history and chart on the mock page
  await page.getByRole('link', { name: 'All mock exams' }).click();
  await expect(page.getByRole('link', { name: 'Review' })).toHaveCount(1);
  await expect(page.locator('.chart svg')).toBeVisible();
});

test('auto-submits a mock exam when time runs out', async ({ page }) => {
  await page.clock.install();
  await fresh(page);
  await page.goto('./#/mock');
  await page.getByRole('button', { name: 'Start random mock' }).click();
  await expect(page.getByText('Question 1 of 48')).toBeVisible();
  await page.locator('.option').nth(1).click();
  await page.clock.fastForward(61 * 60 * 1000);
  await expect(page.getByText(/auto-submitted at time-up/)).toBeVisible({ timeout: 10000 });
});

test('main pages render without errors', async ({ page }) => {
  const errors: string[] = [];
  page.on('pageerror', (e) => errors.push(e.message));
  for (const path of ['', 'learn', 'learn/math/conics', 'learn/physics/kinematics', 'learn/chemistry/redox', 'formulas/math', 'formulas/chemistry', 'drill', 'mistakes', 'plan', 'tutor', 'resources', 'chemistry-data', 'chinese', 'settings']) {
    await page.goto(`./#/${path}`);
    await expect(page.locator('main h1').first()).toBeVisible();
  }
  // KaTeX errors render as red .katex-error spans
  await page.goto('./#/formulas/physics');
  expect(await page.locator('.katex-error').count()).toBe(0);
  expect(errors).toEqual([]);
});

test('study plan and tutor import round-trip', async ({ page }) => {
  await fresh(page);
  await page.goto('./#/plan');
  await page.getByRole('button', { name: 'Generate plan' }).click();
  await expect(page.getByText(/Week 1 \(this week\)/)).toBeVisible();
  await page.locator('.check-row input[type=checkbox]').first().check();
  await expect(page.getByText(/1\/\d+ tasks done/)).toBeVisible();

  await page.goto('./#/tutor');
  const code = await page.locator('#my-code').inputValue();
  expect(JSON.parse(code).csca).toBe(1);
  await page.getByRole('button', { name: 'Import a code (tutor)' }).click();
  await page.locator('#paste-code').fill(code);
  await expect(page.getByText(/Report for/)).toBeVisible();
});
