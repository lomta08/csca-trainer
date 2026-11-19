import { runGenerator, type GeneratorDef, type Generated } from './core';
import { algebraGenerators } from './algebra';
import { trigSeqGenerators } from './trigseq';
import { calculusGenerators } from './calculus';
import { geometryGenerators } from './geometry';
import { probabilityGenerators } from './probability';
import { randomSeed } from '../rng';

export const GENERATORS: GeneratorDef[] = [
  ...algebraGenerators,
  ...trigSeqGenerators,
  ...calculusGenerators,
  ...geometryGenerators,
  ...probabilityGenerators,
];

export function getGenerator(id: string): GeneratorDef | undefined {
  return GENERATORS.find((g) => g.id === id);
}

export function generate(id: string, seed: number = randomSeed()): Generated {
  const def = getGenerator(id);
  if (!def) throw new Error(`Unknown generator ${id}`);
  return runGenerator(def, seed);
}

/** Rebuild a generated question from its id `gen:<type>:<seed>`. */
export function fromGeneratedId(qid: string): Generated | undefined {
  const m = /^gen:([a-z0-9-]+):(\d+)$/.exec(qid);
  if (!m) return undefined;
  const def = getGenerator(m[1]);
  if (!def) return undefined;
  return runGenerator(def, Number(m[2]));
}

export function generatorsFor(subtopics?: string[]): GeneratorDef[] {
  if (!subtopics || subtopics.length === 0) return GENERATORS;
  return GENERATORS.filter((g) => subtopics.includes(g.subtopic));
}

export { runGenerator };
export type { GeneratorDef, Generated };
