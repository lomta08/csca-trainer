import { useState } from 'react';
import { ELEMENTS, type Element } from '../content/elements';
import { Md } from '../components/Md';

const DATA = String.raw`
| Constant | Value |
|---|---|
| Avogadro constant $N_A$ | $6.02\times10^{23}\ \text{mol}^{-1}$ |
| Molar volume of a gas at STP ($0^\circ$C, $101$ kPa) | $22.4$ L/mol |
| Gas constant $R$ | $8.31\ \text{J/(mol}\cdot\text{K)}$ |
| Ionic product of water at $25^\circ$C | $K_w=1\times10^{-14}$ |

**Solubility rules (water, room temperature)**

- All salts of $\mathrm{Na^+}$, $\mathrm{K^+}$, $\mathrm{NH_4^+}$ and all nitrates are soluble.
- Chlorides are soluble except $\mathrm{AgCl}$ (white).
- Sulfates are soluble except $\mathrm{BaSO_4}$ (white); $\mathrm{CaSO_4}$ and $\mathrm{Ag_2SO_4}$ are slightly soluble.
- Carbonates are insoluble except those of $\mathrm{Na^+}$, $\mathrm{K^+}$, $\mathrm{NH_4^+}$.
- Hydroxides: NaOH, KOH, $\mathrm{Ba(OH)_2}$ soluble; $\mathrm{Ca(OH)_2}$ slightly soluble; $\mathrm{Mg(OH)_2}$ (white), $\mathrm{Al(OH)_3}$ (white), $\mathrm{Cu(OH)_2}$ (blue), $\mathrm{Fe(OH)_3}$ (red-brown) insoluble.

**Common colours:** $\mathrm{Cu^{2+}}$ blue, $\mathrm{Fe^{2+}}$ pale green, $\mathrm{Fe^{3+}}$ yellow, $\mathrm{MnO_4^-}$ purple, $\mathrm{Cl_2}$ yellow-green, $\mathrm{NO_2}$ red-brown, $\mathrm{Na_2O_2}$ pale yellow, $\mathrm{CuO}$ black, $\mathrm{Fe_2O_3}$ red-brown.

**Reactivity series of metals:** K > Ca > Na > Mg > Al > Zn > Fe > Sn > Pb > (H) > Cu > Hg > Ag > Pt > Au
`;

export function ChemData() {
  const [sel, setSel] = useState<Element | null>(ELEMENTS.find((e) => e.z === 6) ?? null);
  return (
    <div className="stack">
      <h1>Chemistry data</h1>
      <p className="muted">
        Relative atomic masses are the rounded standard values used in CSCA/gaokao-style questions (e.g. Cl = 35.5, Cu = 64). Questions on this site always state the values they use.
      </p>
      <div className="card">
        <h2 style={{ marginTop: 0 }}>Periodic table</h2>
        <div className="table-wrap">
          <div className="ptable" role="grid" aria-label="Periodic table">
            {ELEMENTS.map((e) => (
              <button
                key={e.z}
                className={`el ${e.cls}`}
                style={{ gridColumn: e.group, gridRow: e.period, cursor: 'pointer', outline: sel?.z === e.z ? '2px solid var(--primary)' : undefined }}
                onClick={() => setSel(e)}
                aria-label={`${e.name}, atomic number ${e.z}, relative atomic mass ${e.mass}`}
              >
                <span>{e.z}</span>
                <b>{e.sym}</b>
                <span>{e.mass}</span>
              </button>
            ))}
          </div>
        </div>
        <div className="row small mt">
          <span className="el metal" style={{ width: 16, height: 16, padding: 0 }} /> metal
          <span className="el nonmetal" style={{ width: 16, height: 16, padding: 0 }} /> non-metal
          <span className="el metalloid" style={{ width: 16, height: 16, padding: 0 }} /> metalloid
          <span className="el noble" style={{ width: 16, height: 16, padding: 0 }} /> noble gas
        </div>
        {sel && (
          <div className="notice mt" aria-live="polite">
            <strong>
              {sel.name} ({sel.sym})
            </strong>{' '}
            — atomic number {sel.z}, relative atomic mass {sel.mass}, period {sel.period}, group {sel.group <= 2 ? `${['I', 'II'][sel.group - 1]}A` : sel.group >= 13 ? (sel.group === 18 ? '0 (noble gases)' : `${['III', 'IV', 'V', 'VI', 'VII'][sel.group - 13]}A`) : `${sel.group} (transition)`}.
          </div>
        )}
        <p className="small muted">*Lanthanides (57–71) and actinides are not shown individually; they are not needed for the CSCA syllabus.</p>
      </div>
      <div className="card">
        <h2 style={{ marginTop: 0 }}>Constants and useful data</h2>
        <Md>{DATA}</Md>
      </div>
    </div>
  );
}
