// Loads all content files at build time. To add questions, edit the JSON files —
// see CONTENT_GUIDE.md. Nothing in this file needs to change.
import type { Question } from '../lib/types';
import type { SubjectId } from './syllabus';
import fixedMocksJson from './mocks/fixed-mocks.json';

const questionFiles = import.meta.glob<Question[]>(['./math/*.json', './physics/*.json', './chemistry/*.json'], { eager: true, import: 'default' });
const noteFiles = import.meta.glob<string>('./notes/*/*.md', { eager: true, query: '?raw', import: 'default' });
const formulaFiles = import.meta.glob<string>('./formulas/*.md', { eager: true, query: '?raw', import: 'default' });

export const QUESTIONS: Question[] = Object.values(questionFiles).flat();
export const QUESTION_BY_ID = new Map(QUESTIONS.map((q) => [q.id, q]));

export function questionsFor(subject: SubjectId, subtopics?: string[]): Question[] {
  return QUESTIONS.filter((q) => q.subject === subject && (!subtopics || subtopics.length === 0 || subtopics.includes(q.subtopic)));
}

export function getNote(subject: string, subtopic: string): string | undefined {
  return noteFiles[`./notes/${subject}/${subtopic}.md`];
}

export function getFormulaSheet(subject: string): string | undefined {
  return formulaFiles[`./formulas/${subject}.md`];
}

export interface FixedMock {
  id: string;
  title: string;
  qids: string[];
}

export const FIXED_MOCKS = fixedMocksJson as unknown as Record<SubjectId, FixedMock[]>;
