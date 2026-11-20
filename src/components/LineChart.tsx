export interface Series {
  name: string;
  color: string;
  points: { x: number; y: number; label?: string }[];
}

/** Minimal responsive SVG line chart (y fixed to 0–100 by default). */
export function LineChart({ series, height = 220, yMax = 100, ariaLabel }: { series: Series[]; height?: number; yMax?: number; ariaLabel: string }) {
  const W = 640;
  const H = height;
  const pad = { l: 36, r: 12, t: 12, b: 28 };
  const all = series.flatMap((s) => s.points);
  if (all.length === 0) return <p className="muted">No data yet.</p>;
  const xs = all.map((p) => p.x);
  let xMin = Math.min(...xs);
  let xMax = Math.max(...xs);
  if (xMin === xMax) {
    xMin -= 1;
    xMax += 1;
  }
  const sx = (x: number) => pad.l + ((x - xMin) / (xMax - xMin)) * (W - pad.l - pad.r);
  const sy = (y: number) => pad.t + (1 - y / yMax) * (H - pad.t - pad.b);
  const ticks = [0, 25, 50, 75, 100].filter((t) => t <= yMax);
  return (
    <div className="chart">
      <svg viewBox={`0 0 ${W} ${H}`} role="img" aria-label={ariaLabel}>
        {ticks.map((t) => (
          <g key={t}>
            <line className="gridline" x1={pad.l} x2={W - pad.r} y1={sy(t)} y2={sy(t)} />
            <text x={pad.l - 6} y={sy(t) + 4} textAnchor="end">
              {t}
            </text>
          </g>
        ))}
        <line className="axis" x1={pad.l} x2={W - pad.r} y1={sy(0)} y2={sy(0)} />
        {series.map((s) => {
          const pts = [...s.points].sort((a, b) => a.x - b.x);
          const d = pts.map((p, i) => `${i ? 'L' : 'M'}${sx(p.x).toFixed(1)},${sy(p.y).toFixed(1)}`).join(' ');
          return (
            <g key={s.name}>
              <path d={d} fill="none" stroke={s.color} strokeWidth={2.5} />
              {pts.map((p, i) => (
                <circle key={i} cx={sx(p.x)} cy={sy(p.y)} r={4} fill={s.color}>
                  <title>{`${s.name}: ${p.y}${p.label ? ` (${p.label})` : ''}`}</title>
                </circle>
              ))}
            </g>
          );
        })}
      </svg>
      {series.length > 1 && (
        <div className="row small" style={{ justifyContent: 'center' }}>
          {series.map((s) => (
            <span key={s.name} className="row" style={{ gap: 6 }}>
              <span style={{ width: 12, height: 12, borderRadius: 3, background: s.color, display: 'inline-block' }} />
              {s.name}
            </span>
          ))}
        </div>
      )}
    </div>
  );
}
