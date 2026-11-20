import { useMemo, useState } from 'react';
import { GENERATORS, runGenerator } from '../lib/generators';
import { randomSeed, Rng } from '../lib/rng';
import { allSubtopics } from '../content/syllabus';
import { PracticeSession } from '../components/PracticeSession';
import { setLastLocation } from '../lib/store';
import type { Question } from '../lib/types';

const BATCH = 5;

export function Drill() {
  const [chosen, setChosen] = useState<string[]>([]);
  const [running, setRunning] = useState(false);
  const groups = useMemo(
    () =>
      allSubtopics('math')
        .map((r) => ({ ref: r, gens: GENERATORS.filter((g) => g.subtopic === r.subtopic.id) }))
        .filter((g) => g.gens.length),
    [],
  );
  const active = chosen.length ? GENERATORS.filter((g) => chosen.includes(g.id)) : GENERATORS;

  const batch = (): Question[] => {
    const r = new Rng(randomSeed());
    return Array.from({ length: BATCH }, () => runGenerator(r.pick(active), randomSeed()));
  };

  if (running) {
    return (
      <PracticeSession
        questions={batch()}
        more={batch}
        mode="drill"
        title={`Math drill · ${chosen.length ? `${chosen.length} question type(s)` : 'all question types'}`}
        onExit={() => setRunning(false)}
      />
    );
  }

  const toggle = (id: string) => setChosen((c) => (c.includes(id) ? c.filter((x) => x !== id) : [...c, id]));

  return (
    <div className="stack">
      <h1>Unlimited math drill</h1>
      <p className="muted">
        Fresh questions are generated every time. The program computes each answer, and the wrong options come from typical mistakes (sign errors, forgotten conditions,
        wrong formulas). Tick the types you want to drill, or leave them all unticked for a random mix. The drill never ends: press <em>Finish</em> when you are done.
      </p>
      <div className="card">
        <div className="spread mb">
          <strong>{chosen.length ? `${chosen.length} selected` : `All ${GENERATORS.length} question types`}</strong>
          <span className="row">
            {chosen.length > 0 && (
              <button className="btn small" onClick={() => setChosen([])}>
                Clear
              </button>
            )}
            <button
              className="btn primary"
              onClick={() => {
                setLastLocation({ path: '/drill', label: 'Unlimited math drill' });
                setRunning(true);
              }}
            >
              Start drill →
            </button>
          </span>
        </div>
        <div className="grid grid-2">
          {groups.map(({ ref, gens }) => (
            <fieldset key={ref.subtopic.id} style={{ border: '1px solid var(--border)', borderRadius: 10, padding: '6px 12px' }}>
              <legend className="small" style={{ fontWeight: 700 }}>
                {ref.subtopic.name}
              </legend>
              {gens.map((g) => (
                <label key={g.id} className="check-row" style={{ padding: '3px 0' }}>
                  <input type="checkbox" checked={chosen.includes(g.id)} onChange={() => toggle(g.id)} />
                  <span>{g.name}</span>
                </label>
              ))}
            </fieldset>
          ))}
        </div>
      </div>
    </div>
  );
}
