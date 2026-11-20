import { useMemo, useState } from 'react';
import { useAppState } from '../lib/store';
import { buildSummary, parseProgressCode, reportText, summaryTopicStats, type ProgressSummary } from '../lib/report';
import { SUBJECTS, getSubject } from '../content/syllabus';
import { LineChart } from '../components/LineChart';
import { formatDate, formatDuration, toDateKey } from '../lib/dates';
import { weakestTopics } from '../lib/stats';

async function copy(text: string): Promise<boolean> {
  try {
    await navigator.clipboard.writeText(text);
    return true;
  } catch {
    // fallback for older browsers / insecure contexts
    try {
      const ta = document.createElement('textarea');
      ta.value = text;
      document.body.appendChild(ta);
      ta.select();
      const ok = document.execCommand('copy');
      ta.remove();
      return ok;
    } catch {
      return false;
    }
  }
}

function CopyButton({ text, label, primary }: { text: string; label: string; primary?: boolean }) {
  const [msg, setMsg] = useState<string | null>(null);
  return (
    <span className="row" style={{ gap: 6 }}>
      <button
        className={`btn ${primary ? 'primary' : ''}`}
        onClick={async () => {
          const ok = await copy(text);
          setMsg(ok ? 'Copied!' : 'Copy failed — select the text and copy it manually.');
          setTimeout(() => setMsg(null), 3000);
        }}
      >
        {label}
      </button>
      {msg && (
        <span className="small muted" role="status">
          {msg}
        </span>
      )}
    </span>
  );
}

export function ProgressReport({ s }: { s: ProgressSummary }) {
  const stats = summaryTopicStats(s);
  const weak = weakestTopics(stats, 5);
  const series = SUBJECTS.map((sub) => ({
    name: sub.name,
    color: `var(--${sub.id})`,
    points: s.mocks
      .filter((m) => m[0] === sub.id)
      .sort((a, b) => a[3] - b[3])
      .map((m, i) => ({ x: i + 1, y: m[2], label: m[1] })),
  })).filter((x) => x.points.length);
  return (
    <div className="stack">
      <div className="grid grid-3">
        <div className="card stat">
          <span className="value">{formatDuration(s.studyMs)}</span>
          <span className="label">time studied ({formatDuration(s.last7Ms)} in the last 7 days)</span>
        </div>
        <div className="card stat">
          <span className="value">{s.streak}</span>
          <span className="label">day streak · {s.mistakes} questions in the mistakes notebook</span>
        </div>
        <div className="card stat">
          <span className="value">{s.examDate ? formatDate(s.examDate) : '—'}</span>
          <span className="label">exam date{s.plan ? ` · plan ${s.plan.done}/${s.plan.total} tasks` : ''}</span>
        </div>
      </div>
      <div className="card">
        <h2>Accuracy by subject</h2>
        <div className="table-wrap">
          <table>
            <thead>
              <tr>
                <th>Subject</th>
                <th>Questions</th>
                <th>Accuracy</th>
                <th>Mock scores</th>
              </tr>
            </thead>
            <tbody>
              {SUBJECTS.map((sub) => {
                const t = s.topics.filter((x) => x[0] === sub.id);
                const att = t.reduce((a, x) => a + x[2], 0);
                const cor = t.reduce((a, x) => a + x[3], 0);
                const mocks = s.mocks.filter((m) => m[0] === sub.id).sort((a, b) => a[3] - b[3]);
                return (
                  <tr key={sub.id}>
                    <td>{sub.name}</td>
                    <td>{att}</td>
                    <td>{att ? `${Math.round((100 * cor) / att)}%` : '—'}</td>
                    <td>{mocks.length ? mocks.map((m) => m[2]).join(', ') : '—'}</td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        </div>
      </div>
      <div className="card">
        <h2>Mock exam scores</h2>
        {series.length ? <LineChart series={series} ariaLabel="Mock exam score trend" /> : <p className="muted">No mock exams yet.</p>}
        {s.mocks.length > 0 && (
          <div className="table-wrap mt">
            <table>
              <thead>
                <tr>
                  <th>Date</th>
                  <th>Paper</th>
                  <th>Score</th>
                  <th>Time</th>
                </tr>
              </thead>
              <tbody>
                {[...s.mocks]
                  .sort((a, b) => b[3] - a[3])
                  .map((m, i) => (
                    <tr key={i}>
                      <td>{formatDate(toDateKey(m[3]))}</td>
                      <td>{m[1]}</td>
                      <td>{m[2]}</td>
                      <td>{formatDuration(m[4])}</td>
                    </tr>
                  ))}
              </tbody>
            </table>
          </div>
        )}
      </div>
      <div className="card">
        <h2>Accuracy by topic</h2>
        {weak.length > 0 && (
          <p>
            <strong>Weakest:</strong> {weak.map((w) => `${w.name} (${Math.round((w.recent ?? 0) * 100)}%)`).join(', ')}
          </p>
        )}
        <div className="table-wrap">
          <table>
            <thead>
              <tr>
                <th>Topic</th>
                <th>Questions</th>
                <th>Overall</th>
                <th>Last 20</th>
              </tr>
            </thead>
            <tbody>
              {stats
                .sort((a, b) => a.subject.localeCompare(b.subject) || (a.recent ?? 0) - (b.recent ?? 0))
                .map((t) => (
                  <tr key={t.subject + t.subtopic}>
                    <td>
                      {t.name} <span className="small muted">({getSubject(t.subject)?.short})</span>
                    </td>
                    <td>{t.attempts}</td>
                    <td>{Math.round((100 * t.correct) / Math.max(1, t.attempts))}%</td>
                    <td>{t.recent === null ? '—' : `${Math.round(t.recent * 100)}%`}</td>
                  </tr>
                ))}
              {stats.length === 0 && (
                <tr>
                  <td colSpan={4} className="muted">
                    No practice recorded yet.
                  </td>
                </tr>
              )}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}

export function Tutor() {
  const state = useAppState();
  const [tab, setTab] = useState<'mine' | 'import'>('mine');
  const [pasted, setPasted] = useState('');
  const mine = useMemo(() => buildSummary(state), [state]);
  const code = JSON.stringify(mine);
  let imported: ProgressSummary | null = null;
  let error: string | null = null;
  if (pasted.trim()) {
    try {
      imported = parseProgressCode(pasted);
    } catch (e) {
      error = (e as Error).message;
    }
  }

  return (
    <div className="stack">
      <h1>Tutor view</h1>
      <p className="muted">
        Progress is stored only in this browser. To share it, the student copies the <strong>progress code</strong> and sends it to the tutor, who pastes it under
        “Import a code”.
      </p>
      <div className="tabs">
        <button className={`tab ${tab === 'mine' ? 'active' : ''}`} onClick={() => setTab('mine')}>
          This device’s progress
        </button>
        <button className={`tab ${tab === 'import' ? 'active' : ''}`} onClick={() => setTab('import')}>
          Import a code (tutor)
        </button>
      </div>

      {tab === 'mine' ? (
        <>
          <div className="card stack">
            <h2 style={{ marginTop: 0 }}>Send your progress to your tutor</h2>
            <div className="row">
              <CopyButton text={code} label="Copy progress code" primary />
              <CopyButton text={reportText(mine)} label="Copy report" />
            </div>
            <label className="field" htmlFor="my-code">Progress code</label>
            <textarea id="my-code" readOnly value={code} onFocus={(e) => e.target.select()} rows={4} />
            <details>
              <summary>Preview the plain-text report</summary>
              <pre className="small" style={{ whiteSpace: 'pre-wrap' }}>{reportText(mine)}</pre>
            </details>
          </div>
          <ProgressReport s={mine} />
        </>
      ) : (
        <>
          <div className="card stack">
            <label className="field" htmlFor="paste-code">Paste the student’s progress code</label>
            <textarea id="paste-code" value={pasted} onChange={(e) => setPasted(e.target.value)} placeholder='{"csca":1, ...}' rows={5} />
            {error && <div className="notice bad">{error}</div>}
            {imported && (
              <div className="spread">
                <span>
                  Report for <strong>{imported.name}</strong>, generated {formatDate(toDateKey(imported.generated))}
                </span>
                <CopyButton text={reportText(imported)} label="Copy report" primary />
              </div>
            )}
          </div>
          {imported && <ProgressReport s={imported} />}
        </>
      )}
    </div>
  );
}
