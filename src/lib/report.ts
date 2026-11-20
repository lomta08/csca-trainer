import type { AppState } from './types';
import { subtopicStats, streak, totalStudyMs, recentStudy, weakestTopics, type TopicStat } from './stats';
import { planProgress } from './plan';
import { getSubject, subtopicName, type SubjectId } from '../content/syllabus';
import { formatDate, formatDuration, toDateKey } from './dates';

/** Compact summary the student sends to the tutor (no raw history, so it stays short). */
export interface ProgressSummary {
  csca: 1;
  name: string;
  generated: number;
  examDate: string | null;
  streak: number;
  studyMs: number;
  last7Ms: number;
  /** [subject, subtopic, attempts, correct, recent accuracy % or -1] */
  topics: [SubjectId, string, number, number, number][];
  /** [subject, title, score, finishedTs, durationMs] */
  mocks: [SubjectId, string, number, number, number][];
  mistakes: number;
  plan: { done: number; total: number } | null;
}

export function buildSummary(state: AppState, now = Date.now()): ProgressSummary {
  const stats = subtopicStats(state.attempts);
  return {
    csca: 1,
    name: state.name || 'Student',
    generated: now,
    examDate: state.examDate,
    streak: streak(state, toDateKey(now)),
    studyMs: Math.round(totalStudyMs(state)),
    last7Ms: Math.round(recentStudy(state, 7, new Date(now)).reduce((s, d) => s + d.ms, 0)),
    topics: stats.filter((s) => s.attempts > 0).map((s) => [s.subject, s.subtopic, s.attempts, s.correct, s.recent === null ? -1 : Math.round(s.recent * 100)]),
    mocks: state.mocks.map((m) => [m.subject, m.title, m.score, m.finishedTs, Math.round(m.durationMs)]),
    mistakes: Object.keys(state.mistakes).length,
    plan: state.plan ? planProgress(state.plan) : null,
  };
}

export function progressCode(state: AppState): string {
  return JSON.stringify(buildSummary(state));
}

/** Parse a pasted progress code. Accepts surrounding whitespace or text around the JSON. */
export function parseProgressCode(text: string): ProgressSummary {
  const start = text.indexOf('{');
  const end = text.lastIndexOf('}');
  if (start < 0 || end < start) throw new Error('No progress code found. Paste the whole code, starting with { and ending with }.');
  let data: unknown;
  try {
    data = JSON.parse(text.slice(start, end + 1));
  } catch {
    throw new Error('The code is damaged (not valid JSON). Ask the student to copy it again.');
  }
  const d = data as Partial<ProgressSummary>;
  if (d.csca !== 1 || !Array.isArray(d.topics) || !Array.isArray(d.mocks)) throw new Error('This is not a CSCA Trainer progress code.');
  return {
    csca: 1,
    name: String(d.name ?? 'Student'),
    generated: Number(d.generated ?? 0),
    examDate: d.examDate ?? null,
    streak: Number(d.streak ?? 0),
    studyMs: Number(d.studyMs ?? 0),
    last7Ms: Number(d.last7Ms ?? 0),
    topics: d.topics,
    mocks: d.mocks,
    mistakes: Number(d.mistakes ?? 0),
    plan: d.plan ?? null,
  };
}

export function summaryTopicStats(s: ProgressSummary): TopicStat[] {
  return s.topics.map(([subject, subtopic, attempts, correct, recent]) => ({
    subject,
    topic: '',
    subtopic,
    name: subtopicName(subject, subtopic),
    attempts,
    correct,
    recent: recent < 0 ? null : recent / 100,
  }));
}

/** Short plain-text report for pasting into a message. */
export function reportText(s: ProgressSummary): string {
  const lines: string[] = [];
  lines.push(`CSCA progress report — ${s.name} (${formatDate(toDateKey(s.generated))})`);
  if (s.examDate) lines.push(`Exam date: ${formatDate(s.examDate)}`);
  lines.push(`Study time: ${formatDuration(s.studyMs)} total, ${formatDuration(s.last7Ms)} in the last 7 days. Streak: ${s.streak} day(s).`);
  for (const subj of ['math', 'physics', 'chemistry'] as SubjectId[]) {
    const t = s.topics.filter((x) => x[0] === subj);
    const attempts = t.reduce((a, x) => a + x[2], 0);
    const correct = t.reduce((a, x) => a + x[3], 0);
    const mocks = s.mocks.filter((m) => m[0] === subj).sort((a, b) => a[3] - b[3]);
    if (!attempts && !mocks.length) continue;
    const name = getSubject(subj)!.name;
    const acc = attempts ? `${Math.round((100 * correct) / attempts)}% of ${attempts} questions` : 'no practice yet';
    const mockTxt = mocks.length ? `; mocks: ${mocks.map((m) => m[2]).join(', ')} (latest ${mocks[mocks.length - 1][2]}/100)` : '';
    lines.push(`${name}: ${acc}${mockTxt}`);
  }
  const weak = weakestTopics(summaryTopicStats(s), 3);
  if (weak.length) lines.push(`Weakest topics: ${weak.map((w) => `${w.name} (${Math.round((w.recent ?? 0) * 100)}%)`).join('; ')}`);
  lines.push(`Mistakes notebook: ${s.mistakes} question(s) to retry.`);
  if (s.plan) lines.push(`Study plan: ${s.plan.done}/${s.plan.total} tasks done.`);
  return lines.join('\n');
}
