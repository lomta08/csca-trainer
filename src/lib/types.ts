import type { SubjectId } from '../content/syllabus';

export type Difficulty = 1 | 2 | 3;

/** A multiple-choice question. Text fields are Markdown with $inline$ and $$display$$ LaTeX. */
export interface Question {
  id: string;
  subject: SubjectId;
  topic: string;
  subtopic: string;
  difficulty: Difficulty;
  question: string;
  options: [string, string, string, string];
  /** index 0–3 of the correct option */
  answer: number;
  explanation: string;
  tags: string[];
  /** true for questions produced by a generator */
  generated?: boolean;
}

export type Mode = 'practice' | 'mock' | 'mistakes' | 'drill';

export interface AttemptRecord {
  qid: string;
  subject: SubjectId;
  topic: string;
  subtopic: string;
  correct: boolean;
  ts: number;
  timeMs: number;
  mode: Mode;
}

export interface MistakeEntry {
  qid: string;
  subject: SubjectId;
  subtopic: string;
  addedTs: number;
  lastWrongTs: number;
  wrongCount: number;
  /** distinct local dates (YYYY-MM-DD) on which it was answered correctly since the last wrong answer */
  correctDays: string[];
}

export interface MockResult {
  id: string;
  subject: SubjectId;
  kind: 'random' | 'fixed';
  fixedId?: string;
  title: string;
  startedTs: number;
  finishedTs: number;
  durationMs: number;
  qids: string[];
  answers: (number | null)[];
  timePerQ: number[];
  flagged: boolean[];
  correct: number;
  total: number;
  score: number;
  autoSubmitted: boolean;
}

export interface ActiveMock {
  id: string;
  subject: SubjectId;
  kind: 'random' | 'fixed';
  fixedId?: string;
  title: string;
  qids: string[];
  answers: (number | null)[];
  flagged: boolean[];
  timePerQ: number[];
  current: number;
  startedTs: number;
  /** epoch ms when time runs out */
  endsTs: number;
}

export interface PlanItem {
  id: string;
  kind: 'learn' | 'practice' | 'review' | 'mock';
  label: string;
  subject?: SubjectId;
  subtopic?: string;
  link: string;
  hours: number;
  done: boolean;
}

export interface PlanWeek {
  index: number;
  start: string; // YYYY-MM-DD
  end: string;
  title: string;
  items: PlanItem[];
}

export interface StudyPlan {
  createdTs: number;
  examDate: string;
  startDate: string;
  subjects: SubjectId[];
  hoursPerWeek: number;
  weeks: PlanWeek[];
  warning?: string;
}

export interface LastLocation {
  path: string;
  label: string;
  ts: number;
}

export interface AppState {
  version: 1;
  name: string;
  examDate: string | null;
  attempts: AttemptRecord[];
  mistakes: Record<string, MistakeEntry>;
  flags: string[];
  mocks: MockResult[];
  activeMock: ActiveMock | null;
  plan: StudyPlan | null;
  /** ms of study per local date */
  studyLog: Record<string, number>;
  last: LastLocation | null;
  lessonsRead: string[];
}
