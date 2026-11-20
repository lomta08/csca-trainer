import { useSyncExternalStore } from 'react';
import type { AppState, AttemptRecord, MockResult, ActiveMock, StudyPlan, Question, Mode, LastLocation } from './types';
import { applyAnswer } from './srs';
import { toDateKey } from './dates';

const KEY = 'csca.v1';
const MAX_ATTEMPTS = 6000;

export function emptyState(): AppState {
  return {
    version: 1,
    name: '',
    examDate: null,
    attempts: [],
    mistakes: {},
    flags: [],
    mocks: [],
    activeMock: null,
    plan: null,
    studyLog: {},
    last: null,
    lessonsRead: [],
  };
}

/** Fill in any fields missing from older or hand-edited data. */
export function normalizeState(raw: unknown): AppState {
  const base = emptyState();
  if (!raw || typeof raw !== 'object') return base;
  const r = raw as Partial<AppState>;
  return {
    ...base,
    ...r,
    version: 1,
    attempts: Array.isArray(r.attempts) ? r.attempts : [],
    mistakes: r.mistakes && typeof r.mistakes === 'object' ? r.mistakes : {},
    flags: Array.isArray(r.flags) ? r.flags : [],
    mocks: Array.isArray(r.mocks) ? r.mocks : [],
    studyLog: r.studyLog && typeof r.studyLog === 'object' ? r.studyLog : {},
    lessonsRead: Array.isArray(r.lessonsRead) ? r.lessonsRead : [],
  };
}

function load(): AppState {
  try {
    if (typeof localStorage === 'undefined') return emptyState();
    const txt = localStorage.getItem(KEY);
    if (!txt) return emptyState();
    return normalizeState(JSON.parse(txt));
  } catch {
    return emptyState();
  }
}

let state: AppState = load();
const listeners = new Set<() => void>();
let saveWarned = false;

function persist() {
  try {
    if (typeof localStorage !== 'undefined') localStorage.setItem(KEY, JSON.stringify(state));
  } catch (e) {
    if (!saveWarned) {
      saveWarned = true;
      console.warn('Could not save progress (storage full or blocked):', e);
    }
  }
}

export function getState(): AppState {
  return state;
}

export function setState(updater: (s: AppState) => AppState) {
  state = updater(state);
  persist();
  listeners.forEach((l) => l());
}

export function subscribe(l: () => void) {
  listeners.add(l);
  return () => listeners.delete(l);
}

export function useAppState(): AppState {
  return useSyncExternalStore(subscribe, getState, getState);
}

// Keep tabs in sync.
if (typeof window !== 'undefined') {
  window.addEventListener('storage', (e) => {
    if (e.key === KEY) {
      state = load();
      listeners.forEach((l) => l());
    }
  });
}

// ---- actions -------------------------------------------------------------

export function recordAnswer(q: Question, chosen: number, timeMs: number, mode: Mode) {
  const correct = chosen === q.answer;
  const capped = Math.min(Math.max(0, timeMs), 5 * 60 * 1000);
  const now = Date.now();
  const rec: AttemptRecord = {
    qid: q.id,
    subject: q.subject,
    topic: q.topic,
    subtopic: q.subtopic,
    correct,
    ts: now,
    timeMs: capped,
    mode,
  };
  setState((s) => {
    const attempts = [...s.attempts, rec];
    if (attempts.length > MAX_ATTEMPTS) attempts.splice(0, attempts.length - MAX_ATTEMPTS);
    const day = toDateKey(now);
    return {
      ...s,
      attempts,
      mistakes: applyAnswer(s.mistakes, q, correct, now),
      studyLog: { ...s.studyLog, [day]: (s.studyLog[day] ?? 0) + capped },
    };
  });
  return correct;
}

export function addStudyTime(ms: number) {
  if (ms <= 0) return;
  const day = toDateKey();
  setState((s) => ({ ...s, studyLog: { ...s.studyLog, [day]: (s.studyLog[day] ?? 0) + Math.min(ms, 30 * 60 * 1000) } }));
}

export function toggleFlag(qid: string) {
  setState((s) => ({ ...s, flags: s.flags.includes(qid) ? s.flags.filter((f) => f !== qid) : [...s.flags, qid] }));
}

export function removeMistake(qid: string) {
  setState((s) => {
    const m = { ...s.mistakes };
    delete m[qid];
    return { ...s, mistakes: m };
  });
}

export function setExamDate(date: string | null) {
  setState((s) => ({ ...s, examDate: date }));
}

export function setName(name: string) {
  setState((s) => ({ ...s, name }));
}

export function setActiveMock(m: ActiveMock | null) {
  setState((s) => ({ ...s, activeMock: m }));
}

export function saveMockResult(r: MockResult) {
  setState((s) => ({ ...s, mocks: [...s.mocks, r], activeMock: null }));
}

/**
 * Save a finished mock in one write: the result, an attempt record per answered question,
 * mistakes for wrong or unanswered questions, and the study time.
 */
export function submitMockResult(r: MockResult, questions: Question[]) {
  setState((s) => {
    let mistakes = s.mistakes;
    const attempts = [...s.attempts];
    questions.forEach((q, i) => {
      const choice = r.answers[i];
      const correct = choice !== null && choice === q.answer;
      if (choice !== null) {
        attempts.push({ qid: q.id, subject: q.subject, topic: q.topic, subtopic: q.subtopic, correct, ts: r.finishedTs, timeMs: Math.min(r.timePerQ[i] ?? 0, 5 * 60 * 1000), mode: 'mock' });
      }
      mistakes = applyAnswer(mistakes, q, correct, r.finishedTs);
    });
    if (attempts.length > MAX_ATTEMPTS) attempts.splice(0, attempts.length - MAX_ATTEMPTS);
    const day = toDateKey(r.finishedTs);
    return {
      ...s,
      attempts,
      mistakes,
      mocks: [...s.mocks, r],
      activeMock: null,
      studyLog: { ...s.studyLog, [day]: (s.studyLog[day] ?? 0) + Math.min(r.durationMs, 2 * 60 * 60 * 1000) },
    };
  });
}

export function setPlan(plan: StudyPlan | null) {
  setState((s) => ({ ...s, plan }));
}

export function togglePlanItem(itemId: string) {
  setState((s) => {
    if (!s.plan) return s;
    return {
      ...s,
      plan: {
        ...s.plan,
        weeks: s.plan.weeks.map((w) => ({ ...w, items: w.items.map((it) => (it.id === itemId ? { ...it, done: !it.done } : it)) })),
      },
    };
  });
}

export function setLastLocation(loc: Omit<LastLocation, 'ts'>) {
  const cur = state.last;
  if (cur && cur.path === loc.path && Date.now() - cur.ts < 60000) return;
  setState((s) => ({ ...s, last: { ...loc, ts: Date.now() } }));
}

export function markLessonRead(key: string) {
  if (state.lessonsRead.includes(key)) return;
  setState((s) => ({ ...s, lessonsRead: [...s.lessonsRead, key] }));
}

export function replaceState(next: AppState) {
  setState(() => normalizeState(next));
}

export function resetAll() {
  setState(() => emptyState());
}

// ---- theme ---------------------------------------------------------------

export type Theme = 'light' | 'dark' | 'system';

export function getTheme(): Theme {
  try {
    const t = localStorage.getItem('csca.theme');
    return t === 'light' || t === 'dark' ? t : 'system';
  } catch {
    return 'system';
  }
}

export function applyTheme(t: Theme) {
  try {
    if (t === 'system') localStorage.removeItem('csca.theme');
    else localStorage.setItem('csca.theme', t);
  } catch {
    /* ignore */
  }
  if (t === 'system') delete document.documentElement.dataset.theme;
  else document.documentElement.dataset.theme = t;
}
