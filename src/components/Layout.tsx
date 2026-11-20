import { useEffect, useState, type ReactNode } from 'react';
import { NavLink, Link, useLocation } from 'react-router-dom';
import { applyTheme, getTheme, type Theme } from '../lib/store';

const NAV = [
  { to: '/', label: 'Home', end: true },
  { to: '/learn', label: 'Learn' },
  { to: '/practice', label: 'Practice' },
  { to: '/drill', label: 'Math drill' },
  { to: '/mock', label: 'Mock exams' },
  { to: '/mistakes', label: 'Mistakes' },
  { to: '/plan', label: 'Study plan' },
  { to: '/formulas', label: 'Formulas' },
  { to: '/resources', label: 'Resources' },
  { to: '/tutor', label: 'Tutor' },
];

const THEME_NEXT: Record<Theme, Theme> = { system: 'dark', dark: 'light', light: 'system' };
const THEME_ICON: Record<Theme, string> = { system: '◐', dark: '☾', light: '☀' };

export function Layout({ children }: { children: ReactNode }) {
  const [open, setOpen] = useState(false);
  const [theme, setTheme] = useState<Theme>(() => getTheme());
  const loc = useLocation();
  useEffect(() => {
    setOpen(false);
    window.scrollTo(0, 0);
  }, [loc.pathname]);

  return (
    <div className="app">
      <a href="#main" className="skip-link">Skip to content</a>
      <header className="topbar">
        <div className="topbar-inner">
          <Link to="/" className="brand">
            <span className="brand-badge" aria-hidden="true">C</span>
            CSCA Trainer
          </Link>
          <nav className={`nav ${open ? 'open' : ''}`} aria-label="Main">
            {NAV.map((n) => (
              <NavLink key={n.to} to={n.to} end={n.end}>
                {n.label}
              </NavLink>
            ))}
          </nav>
          <div className="row" style={{ flexWrap: 'nowrap', gap: 6 }}>
            <button
              type="button"
              className="icon-btn"
              onClick={() => {
                const t = THEME_NEXT[theme];
                setTheme(t);
                applyTheme(t);
              }}
              aria-label={`Theme: ${theme}. Click to change.`}
              title={`Theme: ${theme}`}
            >
              {THEME_ICON[theme]}
            </button>
            <button type="button" className="icon-btn menu-btn" aria-label="Menu" aria-expanded={open} onClick={() => setOpen((o) => !o)}>
              ☰
            </button>
          </div>
        </div>
      </header>
      <main id="main">{children}</main>
      <footer className="footer">
        CSCA Trainer · original practice material, not affiliated with the China Scholarship Council · <Link to="/settings">Settings &amp; data</Link>
      </footer>
    </div>
  );
}
