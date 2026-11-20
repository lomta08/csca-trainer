import type { AppState, AttemptRecord } from './types';
import { allSubtopics, SUBJECTS, type SubjectId } from '../content/syllabus';
import { computeStreak, toDateKey } from './dates';

export interface TopicStat {
  subject: SubjectId;
  topic: string;
  subtopic: string;
  name: string;
  attempts: number;
  correct: number;
  /** accuracy over the last 20 attempts (0–1), null if none */
  recent: number | null;
}

/** Accuracy per subtopic for every syllabus subtopic (including untouched ones). */
export function subtopicStats(attempts: AttemptRecord[]): TopicStat[] {
  const map = new Map<string, AttemptRecord[]>();
  for (const a of attempts) {
    const key = `${a.subject}/${a.subtopic}`;
    const list = map.get(key) ?? [];
    list.push(a);
    map.set(key, list);
  }
  return allSubtopics().map(({ subject, topic, subtopic }) => {
    const list = map.get(`${subject.id}/${subtopic.id}`) ?? [];
    const last = list.slice(-20);
    return {
      subject: subject.id,
      topic: topic.id,
      subtopic: subtopic.id,
      name: subtopic.name,
      attempts: list.length,
      correct: list.filter((a) => a.correct).length,
      recent: last.length ? last.filter((a) => a.correct).length / last.length : null,
    };
  });
}

/** Weakest subtopics: at least `minAttempts` attempts, lowest recent accuracy first. */
export function weakestTopics(stats: TopicStat[], n = 5, minAttempts = 3): TopicStat[] {
  return stats
    .filter((s) => s.attempts >= minAttempts && s.recent !== null)
    .sort((a, b) => a.recent! - b.recent! || b.attempts - a.attempts)
    .slice(0, n);
}

export interface SubjectProgress {
  subject: SubjectId;
  attempts: number;
  correct: number;
  /** share of subtopics practised at least 5 times */
  coverage: number;
  /** mastery: mean of recent accuracy over all subtopics (untouched count as 0) */
  mastery: number;
  bestMock: number | null;
  lastMock: number | null;
}

export function subjectProgress(state: AppState): SubjectProgress[] {
  const stats = subtopicStats(state.attempts);
  return SUBJECTS.map((s) => {
    const mine = stats.filter((x) => x.subject === s.id);
    const mocks = state.mocks.filter((m) => m.subject === s.id).sort((a, b) => a.finishedTs - b.finishedTs);
    return {
      subject: s.id,
      attempts: mine.reduce((t, x) => t + x.attempts, 0),
      correct: mine.reduce((t, x) => t + x.correct, 0),
      coverage: mine.filter((x) => x.attempts >= 5).length / mine.length,
      mastery: mine.reduce((t, x) => t + (x.recent ?? 0), 0) / mine.length,
      bestMock: mocks.length ? Math.max(...mocks.map((m) => m.score)) : null,
      lastMock: mocks.length ? mocks[mocks.length - 1].score : null,
    };
  });
}

/** Days with any activity (study time, attempts or mocks). */
export function activeDays(state: AppState): Set<string> {
  const days = new Set<string>(Object.keys(state.studyLog).filter((d) => state.studyLog[d] > 0));
  for (const a of state.attempts) days.add(toDateKey(a.ts));
  for (const m of state.mocks) days.add(toDateKey(m.finishedTs));
  return days;
}

export function streak(state: AppState, today = toDateKey()): number {
  return computeStreak(activeDays(state), today);
}

export function totalStudyMs(state: AppState): number {
  return Object.values(state.studyLog).reduce((s, v) => s + v, 0);
}

/** Study minutes for each of the last `n` days (oldest first). */
export function recentStudy(state: AppState, n = 14, today = new Date()): { day: string; ms: number }[] {
  const out: { day: string; ms: number }[] = [];
  for (let i = n - 1; i >= 0; i--) {
    const d = new Date(today);
    d.setDate(d.getDate() - i);
    const key = toDateKey(d);
    out.push({ day: key, ms: state.studyLog[key] ?? 0 });
  }
  return out;
}
