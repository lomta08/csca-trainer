import { useState } from 'react';
import { applyTheme, getState, getTheme, normalizeState, replaceState, resetAll, setExamDate, setName, useAppState, type Theme } from '../lib/store';

export function Settings() {
  const state = useAppState();
  const [theme, setTheme] = useState<Theme>(getTheme());
  const [restoreText, setRestoreText] = useState('');
  const [msg, setMsg] = useState<string | null>(null);

  const download = () => {
    const blob = new Blob([JSON.stringify(getState())], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `csca-trainer-backup-${new Date().toISOString().slice(0, 10)}.json`;
    a.click();
    URL.revokeObjectURL(url);
  };

  const restore = (text: string) => {
    try {
      const data = JSON.parse(text);
      if (!data || data.version !== 1 || !Array.isArray(data.attempts)) throw new Error('not a backup');
      if (!window.confirm('Replace all progress on this device with the backup?')) return;
      replaceState(normalizeState(data));
      setMsg('Backup restored.');
      setRestoreText('');
    } catch {
      setMsg('That is not a valid CSCA Trainer backup file.');
    }
  };

  return (
    <div className="stack">
      <h1>Settings &amp; data</h1>
      <div className="card stack">
        <div>
          <label className="field" htmlFor="name">Your name (shown on reports)</label>
          <input id="name" type="text" value={state.name} onChange={(e) => setName(e.target.value)} placeholder="e.g. Amina" />
        </div>
        <div>
          <label className="field" htmlFor="exam">Exam date</label>
          <input id="exam" type="date" value={state.examDate ?? ''} onChange={(e) => setExamDate(e.target.value || null)} />
        </div>
        <div>
          <label className="field" htmlFor="theme">Theme</label>
          <select
            id="theme"
            value={theme}
            onChange={(e) => {
              const t = e.target.value as Theme;
              setTheme(t);
              applyTheme(t);
            }}
          >
            <option value="system">Same as device</option>
            <option value="light">Light</option>
            <option value="dark">Dark</option>
          </select>
        </div>
      </div>

      <div className="card stack">
        <h2 style={{ marginTop: 0 }}>Backup and restore</h2>
        <p className="small muted">
          Progress is saved in this browser only. Download a backup to move it to another device (for example from phone to laptop), then restore it there.
        </p>
        <div className="row">
          <button className="btn primary" onClick={download}>Download backup</button>
          <label className="btn">
            Restore from file
            <input
              type="file"
              accept="application/json,.json"
              className="hidden"
              onChange={async (e) => {
                const f = e.target.files?.[0];
                if (f) restore(await f.text());
                e.target.value = '';
              }}
            />
          </label>
        </div>
        <details>
          <summary>Or paste a backup</summary>
          <textarea aria-label="Backup JSON" value={restoreText} onChange={(e) => setRestoreText(e.target.value)} rows={4} />
          <button className="btn mt" disabled={!restoreText.trim()} onClick={() => restore(restoreText)}>
            Restore pasted backup
          </button>
        </details>
        {msg && (
          <div className="notice" role="status">
            {msg}
          </div>
        )}
      </div>

      <div className="card stack">
        <h2 style={{ marginTop: 0 }}>Reset</h2>
        <p className="small muted">
          {state.attempts.length} answers, {state.mocks.length} mock exams and {Object.keys(state.mistakes).length} mistakes are stored on this device.
        </p>
        <button
          className="btn danger"
          onClick={() => {
            if (window.confirm('Delete ALL progress on this device? This cannot be undone.')) {
              resetAll();
              setMsg('All progress deleted.');
            }
          }}
        >
          Delete all progress
        </button>
      </div>
    </div>
  );
}
