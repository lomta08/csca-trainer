import { allSubtopics, getSubject, type SubjectId, type SubtopicRef } from '../content/syllabus';
import { addDays, daysBetween, toDateKey } from './dates';
import type { PlanItem, PlanWeek, StudyPlan } from './types';

export interface PlanInput {
  examDate: string; // YYYY-MM-DD
  subjects: SubjectId[];
  hoursPerWeek: number;
  startDate?: string; // defaults to today
}

const MOCK_HOURS = 1.5; // 60 min exam + review

/** Interleave subjects round-robin (in the order given) so every week mixes subjects. */
function interleave(subjects: SubjectId[]): SubtopicRef[] {
  const queues = subjects.map((s) => allSubtopics(s));
  const out: SubtopicRef[] = [];
  while (queues.some((q) => q.length)) for (const q of queues) if (q.length) out.push(q.shift()!);
  return out;
}

function mockWeekCount(weeks: number): number {
  if (weeks >= 8) return 3;
  if (weeks >= 4) return 2;
  return 1;
}

/**
 * Week-by-week plan: every syllabus subtopic of the chosen subjects is studied (lesson + practice),
 * with mock exams in the final week(s). Throws if the exam date is not after the start date.
 */
export function generatePlan(input: PlanInput): StudyPlan {
  const start = input.startDate ?? toDateKey();
  const subjects = (['math', 'physics', 'chemistry'] as SubjectId[]).filter((s) => input.subjects.includes(s));
  if (subjects.length === 0) throw new Error('Choose at least one subject.');
  const days = daysBetween(start, input.examDate);
  if (days < 1) throw new Error('The exam date must be after today.');
  const hoursPerWeek = Math.max(1, input.hoursPerWeek);
  const weeks = Math.max(1, Math.ceil(days / 7));
  const mockWeeks = weeks === 1 ? 1 : mockWeekCount(weeks);
  const studyWeeks = Math.max(1, weeks - mockWeeks);

  const order = interleave(subjects);
  const totalHours = order.reduce((s, r) => s + r.subtopic.hours, 0);
  const perWeek = totalHours / studyWeeks;

  const weekList: PlanWeek[] = Array.from({ length: weeks }, (_, i) => {
    const ws = addDays(start, i * 7);
    const we = i === weeks - 1 ? input.examDate : addDays(start, i * 7 + 6);
    return { index: i + 1, start: ws, end: we, title: '', items: [] };
  });

  // study weeks
  let cum = 0;
  for (const ref of order) {
    const w = Math.min(studyWeeks - 1, Math.floor((cum + 1e-9) / perWeek));
    cum += ref.subtopic.hours;
    const s = ref.subject.id;
    const st = ref.subtopic.id;
    const items = weekList[w].items;
    items.push({
      id: `w${w + 1}-learn-${s}-${st}`,
      kind: 'learn',
      label: `Read the lesson: ${ref.subtopic.name} (${ref.subject.short})`,
      subject: s,
      subtopic: st,
      link: `/learn/${s}/${st}`,
      hours: Math.round(ref.subtopic.hours * 0.4 * 10) / 10,
      done: false,
    });
    items.push({
      id: `w${w + 1}-practice-${s}-${st}`,
      kind: 'practice',
      label: `Practise 15 questions: ${ref.subtopic.name} (${ref.subject.short})`,
      subject: s,
      subtopic: st,
      link: `/practice?subject=${s}&subtopics=${st}&start=1`,
      hours: Math.round(ref.subtopic.hours * 0.6 * 10) / 10,
      done: false,
    });
  }
  for (let w = 0; w < studyWeeks; w++) {
    const week = weekList[w];
    week.items.push({ id: `w${w + 1}-review`, kind: 'review', label: 'Retry your mistakes notebook', link: '/mistakes', hours: 0.5, done: false });
    const subs = [...new Set(week.items.filter((i) => i.subject).map((i) => getSubject(i.subject!)!.short))];
    week.title = subs.length ? `Study: ${subs.join(' + ')}` : 'Review';
  }

  // mock weeks (the last `mockWeeks` weeks; with a single week everything shares it)
  const firstMock = weeks === 1 ? 0 : studyWeeks;
  for (let w = firstMock; w < weeks; w++) {
    const k = w - firstMock + 1; // 1-based mock-week number
    const week = weekList[w];
    for (const s of subjects) {
      const subj = getSubject(s)!;
      const fixedNo = Math.min(3, k);
      week.items.push({
        id: `w${w + 1}-mock-${s}-${k}`,
        kind: 'mock',
        label: k <= 3 ? `Mock exam: ${subj.name} Mock ${fixedNo} (60 min, then review)` : `Random mock exam: ${subj.name}`,
        subject: s,
        link: '/mock',
        hours: MOCK_HOURS,
        done: false,
      });
    }
    if (mockWeeks >= 2 && w === weeks - 1 && weeks > 1) {
      for (const s of subjects)
        week.items.push({ id: `w${w + 1}-mock-${s}-random`, kind: 'mock', label: `Random mock exam: ${getSubject(s)!.name}`, subject: s, link: '/mock', hours: MOCK_HOURS, done: false });
    }
    week.items.push({ id: `w${w + 1}-mockreview`, kind: 'review', label: 'Review every mock mistake and retry the notebook', link: '/mistakes', hours: 1, done: false });
    week.items.push({ id: `w${w + 1}-formulas`, kind: 'review', label: 'Revise the formula sheets', link: '/formulas', hours: 0.5, done: false });
    if (w === weeks - 1)
      week.items.push({ id: `w${w + 1}-examday`, kind: 'review', label: 'Read the exam-day tips and check the official exam notice', link: '/resources', hours: 0.25, done: false });
    week.title = weeks === 1 ? 'Study + mock exams' : w === weeks - 1 ? 'Final mocks + review' : 'Mock exams + review';
  }

  const needed = weekList.reduce((s, w) => s + w.items.reduce((t, i) => t + i.hours, 0), 0);
  const avail = hoursPerWeek * weeks;
  const warning =
    needed > avail * 1.05
      ? `This plan needs about ${Math.ceil(needed / weeks)} hours per week, but you entered ${hoursPerWeek}. Consider studying more each week, or focus on the topics you find hardest first.`
      : undefined;

  return { createdTs: Date.now(), examDate: input.examDate, startDate: start, subjects, hoursPerWeek, weeks: weekList, warning };
}

export function planProgress(plan: StudyPlan): { done: number; total: number } {
  const items: PlanItem[] = plan.weeks.flatMap((w) => w.items);
  return { done: items.filter((i) => i.done).length, total: items.length };
}

/** Index of the plan week containing `today` (clamped). */
export function currentWeekIndex(plan: StudyPlan, today = toDateKey()): number {
  const i = plan.weeks.findIndex((w) => today >= w.start && today <= w.end);
  if (i >= 0) return i;
  return today < plan.weeks[0].start ? 0 : plan.weeks.length - 1;
}
