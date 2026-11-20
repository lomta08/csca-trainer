import { useEffect, useState } from 'react';
// Loads all content files at build time. To add questions, edit the JSON files —
// see CONTENT_GUIDE.md. Nothing in this file needs to change.
import type { Question } from '../lib/types';
import type { SubjectId } from './syllabus';
import fixedMocksJson from './mocks/fixed-mocks.json';

const questionFiles = import.meta.glob<Question[]>(['./math/*.json', './physics/*.json', './chemistry/*.json'], { eager: true, import: 'default' });
// Lessons and formula sheets are loaded on demand (separate chunks) to keep the first load small.
const noteFiles = import.meta.glob<string>('./notes/*/*.md', { query: '?raw', import: 'default' });
const formulaFiles = import.meta.glob<string>('./formulas/*.md', { query: '?raw', import: 'default' });

export const QUESTIONS: Question[] = Object.values(questionFiles).flat();
export const QUESTION_BY_ID = new Map(QUESTIONS.map((q) => [q.id, q]));

export function questionsFor(subject: SubjectId, subtopics?: string[]): Question[] {
  return QUESTIONS.filter((q) => q.subject === subject && (!subtopics || subtopics.length === 0 || subtopics.includes(q.subtopic)));
}

export async function loadNote(subject: string, subtopic: string): Promise<string | undefined> {
  const f = noteFiles[`./notes/${subject}/${subtopic}.md`];
  return f ? f() : undefined;
}

export async function loadFormulaSheet(subject: string): Promise<string | undefined> {
  const f = formulaFiles[`./formulas/${subject}.md`];
  return f ? f() : undefined;
}

/** React hook: load a Markdown file lazily. undefined = loading, null = missing. */
export function useAsyncText(loader: () => Promise<string | undefined>, deps: unknown[]): string | null | undefined {
  const [text, setText] = useState<string | null | undefined>(undefined);
  useEffect(() => {
    let alive = true;
    setText(undefined);
    loader().then((t) => alive && setText(t ?? null)).catch(() => alive && setText(null));
    return () => {
      alive = false;
    };
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, deps);
  return text;
}

export interface FixedMock {
  id: string;
  title: string;
  qids: string[];
}

export const FIXED_MOCKS = fixedMocksJson as unknown as Record<SubjectId, FixedMock[]>;
