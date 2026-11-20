/**
 * Take screenshots of the main pages at phone and desktop sizes (light + dark).
 *   npm run build && npx vite preview --port 4173 &   then   npx tsx scripts/screenshots.ts
 * Output: screenshots/tmp/*.png (git-ignored).
 */
import { chromium, type Page } from '@playwright/test';
import fs from 'node:fs';

const BASE = process.env.BASE_URL ?? 'http://localhost:4173/csca-trainer/';
const OUT = 'screenshots/tmp';
fs.mkdirSync(OUT, { recursive: true });

async function seed(page: Page) {
  await page.goto(BASE);
  await page.evaluate(() => {
    localStorage.clear();
  });
  await page.goto(`${BASE}#/settings`);
  await page.locator('#name').fill('Amina');
  await page.locator('#exam').fill('2027-03-15');
  // a practice session
  await page.goto(`${BASE}#/practice`);
  await page.getByRole('button', { name: '5', exact: true }).click();
  await page.getByRole('button', { name: /Start practice/ }).click();
  for (let i = 0; i < 5; i++) {
    await page.keyboard.press(String((i % 4) + 1));
    await page.keyboard.press('Enter');
  }
  // a mock exam
  await page.goto(`${BASE}#/mock`);
  await page.getByRole('button', { name: 'Start random mock' }).click();
  for (let i = 0; i < 30; i++) {
    await page.keyboard.press(String((i % 4) + 1));
    await page.keyboard.press('Enter');
  }
  await page.getByRole('button', { name: 'Submit', exact: true }).click();
  await page.getByRole('button', { name: 'Yes, submit' }).click();
  await page.waitForSelector('text=score out of 100');
  // a plan
  await page.goto(`${BASE}#/plan`);
  await page.getByRole('button', { name: 'Generate plan' }).click();
}

const SHOTS: [string, string, ((p: Page) => Promise<void>)?][] = [
  ['home', ''],
  ['learn', 'learn'],
  ['lesson-conics', 'learn/math/conics'],
  ['lesson-chem-redox', 'learn/chemistry/redox'],
  [
    'practice-feedback',
    'practice',
    async (p) => {
      await p.getByRole('button', { name: /Start practice/ }).click();
      await p.keyboard.press('2');
      await p.waitForTimeout(400);
    },
  ],
  [
    'mock-run',
    'mock',
    async (p) => {
      p.once('dialog', (d) => d.accept());
      await p.getByRole('button', { name: 'Start random mock' }).click();
      await p.keyboard.press('3');
      await p.waitForTimeout(200);
    },
  ],
  ['mock-home', 'mock'],
  ['formulas-math', 'formulas/math'],
  ['formulas-physics', 'formulas/physics'],
  ['chem-data', 'chemistry-data'],
  ['mistakes', 'mistakes'],
  ['plan', 'plan'],
  ['tutor', 'tutor'],
  ['drill', 'drill'],
  ['resources', 'resources'],
];

async function main() {
  const browser = await chromium.launch();
  for (const [vpName, viewport] of [
    ['mobile', { width: 390, height: 844 }],
    ['desktop', { width: 1280, height: 900 }],
  ] as const) {
    for (const scheme of ['light', 'dark'] as const) {
      const ctx = await browser.newContext({ viewport, colorScheme: scheme, deviceScaleFactor: vpName === 'mobile' ? 2 : 1 });
      const page = await ctx.newPage();
      const errors: string[] = [];
      page.on('pageerror', (e) => errors.push(e.message));
      await seed(page);
      for (const [name, path, act] of SHOTS) {
        if (scheme === 'dark' && !['home', 'lesson-conics', 'practice-feedback', 'mock-run'].includes(name)) continue;
        await page.goto(`${BASE}#/${path}`);
        await page.waitForTimeout(300);
        if (act) await act(page);
        await page.screenshot({ path: `${OUT}/${vpName}-${scheme}-${name}.png`, fullPage: true });
        // overflow check: nothing wider than the viewport
        const overflow = await page.evaluate(() => document.documentElement.scrollWidth - window.innerWidth);
        if (overflow > 1) console.log(`OVERFLOW ${vpName} ${name}: ${overflow}px`);
        const kErr = await page.locator('.katex-error').count();
        if (kErr) console.log(`KATEX ERRORS ${vpName} ${name}: ${kErr}`);
        if (name === 'mock-run') {
          // leave the exam so the next shots are not affected
          await page.evaluate(() => {
            const s = JSON.parse(localStorage.getItem('csca.v1')!);
            s.activeMock = null;
            localStorage.setItem('csca.v1', JSON.stringify(s));
          });
        }
      }
      if (errors.length) console.log(`PAGE ERRORS ${vpName}/${scheme}:`, errors);
      await ctx.close();
    }
  }
  await browser.close();
  console.log('done');
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
