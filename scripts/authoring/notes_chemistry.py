"""Writes chemistry lesson notes to src/content/notes/chemistry/*.md. Original explanations."""
from pathlib import Path

OUT = Path(__file__).resolve().parents[2] / "src" / "content" / "notes" / "chemistry"
OUT.mkdir(parents=True, exist_ok=True)
N = {}

N["matter-classification"] = r"""
## Classification

- **Mixture** (air, sea water, alloys) vs **pure substance** (one substance, fixed composition).
- Pure substances are **elements** (one kind of atom: $\mathrm{O_2}$, $\mathrm{O_3}$, Fe) or **compounds** ($\mathrm{H_2O}$, NaCl).
- Compounds: **oxides** (acidic $\mathrm{CO_2,SO_2}$; basic $\mathrm{Na_2O,CaO}$; amphoteric $\mathrm{Al_2O_3}$), **acids**, **bases**, **salts** (metal ion or $\mathrm{NH_4^+}$ + acid anion).
- **Allotropes:** different forms of one element (diamond/graphite, $\mathrm{O_2}$/$\mathrm{O_3}$). **Isotopes:** atoms of one element with different neutron numbers.

## Dispersions

| | Solution | Colloid | Suspension/emulsion |
|---|---|---|---|
| Particle size | $<1$ nm | $1$–$100$ nm | $>100$ nm |
| Passes filter paper | yes | yes | no |
| Tyndall effect | no | **yes** | — |

## Changes of state and changes of substance

- **Physical change:** no new substance (melting, evaporation, dissolving, sublimation).
- **Chemical change:** new substances form (burning, rusting, fermentation); often colour change, gas, precipitate, energy change.
- State changes: melting/freezing, vaporisation/condensation, sublimation (solid → gas)/deposition.

## Worked examples

**Example 1.** Classify: liquid oxygen, bleach, ice-water mixture, brass.

*Solution.* Liquid oxygen — element; bleach — mixture; ice + water — **pure** compound ($\mathrm{H_2O}$ only); brass — mixture (alloy).

**Example 2.** How can you tell a colloid from a solution quickly?

*Solution.* Shine a beam of light through it: a colloid shows a bright path (Tyndall effect).

## Common traps

- An ice–water mixture is a pure substance.
- One element can make a mixture ($\mathrm{O_2}$ + $\mathrm{O_3}$).
- $\mathrm{Na_2CO_3}$ is a salt, even though its solution is basic.
"""

N["chemical-equations"] = r"""
## Formulas and oxidation states

Common valences: $\mathrm{H}\ +1$, $\mathrm{O}\ -2$, $\mathrm{Na,K}\ +1$, $\mathrm{Mg,Ca,Zn}\ +2$, $\mathrm{Al}\ +3$, $\mathrm{Cl}\ -1$ (in chlorides). Polyatomic ions: $\mathrm{OH^-}$, $\mathrm{NO_3^-}$, $\mathrm{SO_4^{2-}}$, $\mathrm{CO_3^{2-}}$, $\mathrm{NH_4^+}$, $\mathrm{PO_4^{3-}}$.

Write a formula by balancing charges: $\mathrm{Al^{3+}}$ + $\mathrm{SO_4^{2-}}$ → $\mathrm{Al_2(SO_4)_3}$. The sum of oxidation states in a compound is $0$.

## Balancing equations

1. Write correct formulas (never change subscripts to balance!).
2. Balance elements that appear in only one compound on each side first, then O and H.
3. Use the smallest whole-number coefficients; add conditions (heat $\Delta$, catalyst) and $\uparrow$ / $\downarrow$.

## Reaction types

| Type | Pattern | Example |
|---|---|---|
| Combination | A + B → AB | $\mathrm{2H_2+O_2\rightarrow2H_2O}$ |
| Decomposition | AB → A + B | $\mathrm{CaCO_3\xrightarrow{high\ temp}CaO+CO_2}$ |
| Displacement | A + BC → AC + B | $\mathrm{Fe+CuSO_4\rightarrow FeSO_4+Cu}$ |
| Double displacement | AB + CD → AD + CB | $\mathrm{NaOH+HCl\rightarrow NaCl+H_2O}$ |

Relative molecular mass = sum of relative atomic masses. Mass fraction of an element $=\dfrac{\text{atoms}\times A_r}{M_r}$.

## Worked examples

**Example 1.** Balance $\mathrm{C_2H_6+O_2\rightarrow CO_2+H_2O}$.

*Solution.* C: $2\mathrm{CO_2}$; H: $3\mathrm{H_2O}$; O: $7$ atoms → $\tfrac72\mathrm{O_2}$. Double: $\mathrm{2C_2H_6+7O_2\rightarrow4CO_2+6H_2O}$.

**Example 2.** Find the oxidation state of Mn in $\mathrm{KMnO_4}$.

*Solution.* $+1+x-8=0$, $x=+7$.

**Example 3.** Find the mass fraction of O in $\mathrm{CaCO_3}$ (Ca $40$, C $12$, O $16$).

*Solution.* $\dfrac{48}{100}=48\%$.

## Common traps

- Changing a formula's subscripts to balance an equation.
- Forgetting brackets: $\mathrm{Ca(OH)_2}$, not $\mathrm{CaOH_2}$.
"""

N["concentration-ph"] = r"""
## Concentration

- Mass fraction: $w=\dfrac{m_{\text{solute}}}{m_{\text{solution}}}\times100\%$ (solution = solute + solvent).
- **Molar concentration:** $c=\dfrac nV$ (mol/L), with $V$ in litres.
- **Dilution:** the amount of solute is unchanged: $c_1V_1=c_2V_2$.
- Ion concentrations: $0.1$ mol/L $\mathrm{Al_2(SO_4)_3}$ has $[\mathrm{Al^{3+}}]=0.2$, $[\mathrm{SO_4^{2-}}]=0.3$ mol/L.
- Preparing a solution: weigh/measure → dissolve in a beaker → cool → transfer to a **volumetric flask** (rinse) → make up to the mark → invert to mix.

## pH (at 25 °C)

$$\mathrm{pH}=-\lg[\mathrm{H^+}],\qquad [\mathrm{H^+}][\mathrm{OH^-}]=K_w=1\times10^{-14}.$$

- pH $<7$ acidic, $=7$ neutral, $>7$ basic. One pH unit = a factor of $10$ in $[\mathrm{H^+}]$.
- Strong acid $c$ (monoprotic): $\mathrm{pH}=-\lg c$. Strong base: $[\mathrm{H^+}]=\dfrac{10^{-14}}{[\mathrm{OH^-}]}$.
- Mixing acid and base: find the **excess** $\mathrm{H^+}$ or $\mathrm{OH^-}$ and divide by the total volume.

## Worked examples

**Example 1.** $0.005$ mol/L $\mathrm{H_2SO_4}$: find the pH.

*Solution.* $[\mathrm{H^+}]=0.01$ mol/L, pH $=2$.

**Example 2.** How many mL of $10$ mol/L HCl make $500$ mL of $0.2$ mol/L?

*Solution.* $V_1=\dfrac{0.2\times500}{10}=10$ mL.

**Example 3.** $5.85$ g NaCl (Na $23$, Cl $35.5$) in $100$ mL solution. Find $c$.

*Solution.* $n=0.1$ mol, $c=1$ mol/L.

## Common traps

- Dividing by the volume of water added instead of the solution volume.
- Forgetting that $\mathrm{H_2SO_4}$ gives two $\mathrm{H^+}$.
- Forgetting to convert mL to L.
"""

N["mole-calculations"] = r"""
## The mole

$1$ mol contains $N_A=6.02\times10^{23}$ particles (Avogadro constant).

$$n=\frac{N}{N_A}=\frac mM=\frac{V_{\text{gas}}}{V_m}=cV$$

- Molar mass $M$ (g/mol) has the same number as $M_r$: $M(\mathrm{H_2O})=18$ g/mol.
- Always say **which particle**: $1$ mol $\mathrm{CO_2}$ contains $1$ mol molecules, $3$ mol atoms, $22$ mol electrons.

## Stoichiometry

Coefficients in a balanced equation give **mole** ratios.

1. Convert the given quantity to moles.
2. Use the mole ratio from the equation.
3. Convert to the quantity asked for.

**Limiting reagent:** compare the available moles with the ratio needed; the reactant that runs out first sets the amount of product. Mass is conserved overall.

Standard relative atomic masses used on this site: H $1$, C $12$, N $14$, O $16$, Na $23$, Mg $24$, Al $27$, S $32$, Cl $35.5$, K $39$, Ca $40$, Fe $56$, Cu $64$, Zn $65$.

## Worked examples

**Example 1.** How many molecules are in $8.8$ g of $\mathrm{CO_2}$?

*Solution.* $n=0.2$ mol, $N=1.204\times10^{23}$.

**Example 2.** $2.7$ g Al reacts with excess HCl ($\mathrm{2Al+6HCl\rightarrow2AlCl_3+3H_2}$). Find the mass of $\mathrm{H_2}$.

*Solution.* $n(\mathrm{Al})=0.1$ mol → $0.15$ mol $\mathrm{H_2}$ → $0.3$ g.

**Example 3.** $6.5$ g Zn and $0.1$ mol HCl react. Which is limiting?

*Solution.* $0.1$ mol Zn would need $0.2$ mol HCl; HCl is limiting, giving $0.05$ mol $\mathrm{H_2}$.

## Common traps

- Confusing molecules with atoms.
- Using mass ratios instead of mole ratios.
- Forgetting to check for a limiting reagent.
"""

N["gas-law"] = r"""
## Molar volume

At **STP** ($0^\circ$C, $101$ kPa) one mole of **any gas** occupies about $V_m=22.4$ L/mol. It does **not** apply to liquids or solids (e.g. water at STP), and it changes with temperature and pressure.

$$n=\frac{V}{22.4\ \text{L/mol}}\ (\text{STP}),\qquad \rho=\frac{M}{V_m}\Rightarrow M=22.4\rho.$$

## Avogadro's law and consequences

Equal volumes of gases at the same $T$ and $p$ contain equal numbers of molecules. Hence at the same $T$ and $p$:

- $\dfrac{V_1}{V_2}=\dfrac{n_1}{n_2}$;
- $\dfrac{\rho_1}{\rho_2}=\dfrac{M_1}{M_2}$ (relative density);
- the molar volume applies to gas **mixtures** too.

## Ideal gas law

$$pV=nRT,\qquad R=8.31\ \text{J/(mol}\cdot\text{K)},\ T\text{ in kelvin},\ V\text{ in m}^3.$$

## Worked examples

**Example 1.** Find the volume of $3.2$ g $\mathrm{O_2}$ at STP.

*Solution.* $0.1$ mol × $22.4$ = $2.24$ L.

**Example 2.** A gas has density $1.96$ g/L at STP. Find $M$.

*Solution.* $1.96\times22.4\approx44$ g/mol (perhaps $\mathrm{CO_2}$).

**Example 3.** Same $T$ and $p$: ratio of the masses of equal volumes of $\mathrm{CH_4}$ and $\mathrm{O_2}$?

*Solution.* $16:32=1:2$.

## Common traps

- Using $22.4$ L/mol for water, ethanol or $\mathrm{SO_3}$ at STP (not gases there).
- Using $22.4$ L/mol at room temperature.
"""

N["inorganic"] = r"""
## Metals

- **Sodium:** soft, floats on water and reacts vigorously: $\mathrm{2Na+2H_2O\rightarrow2NaOH+H_2\uparrow}$. Burns to yellow $\mathrm{Na_2O_2}$; $\mathrm{2Na_2O_2+2CO_2\rightarrow2Na_2CO_3+O_2}$ (oxygen source). $\mathrm{NaHCO_3}$ decomposes on heating; $\mathrm{Na_2CO_3}$ does not.
- **Aluminium:** protective oxide film; $\mathrm{Al_2O_3}$ and $\mathrm{Al(OH)_3}$ are **amphoteric** (react with acids and strong bases). Aluminium reacts with NaOH solution releasing $\mathrm{H_2}$.
- **Iron:** $\mathrm{Fe^{2+}}$ (pale green) ⇌ $\mathrm{Fe^{3+}}$ (yellow). Test $\mathrm{Fe^{3+}}$ with KSCN (blood red). $\mathrm{2FeCl_3+Fe\rightarrow3FeCl_2}$; $\mathrm{2FeCl_2+Cl_2\rightarrow2FeCl_3}$. $\mathrm{Fe(OH)_2}$ (white) turns grey-green then red-brown $\mathrm{Fe(OH)_3}$ in air.
- **Copper:** does not react with dilute HCl or $\mathrm{H_2SO_4}$; reacts with concentrated $\mathrm{H_2SO_4}$ (gives $\mathrm{SO_2}$) and with nitric acid.

Reactivity series: K > Na > Ca > Mg > Al > Zn > Fe > Sn > Pb > (H) > Cu > Hg > Ag > Pt > Au.

## Non-metals

- **Chlorine:** yellow-green, toxic. $\mathrm{Cl_2+H_2O\rightleftharpoons HCl+HClO}$ (HClO bleaches); $\mathrm{Cl_2+2NaOH\rightarrow NaCl+NaClO+H_2O}$.
- **Sulfur:** $\mathrm{SO_2}$ bleaches (reversibly), is acidic, causes acid rain. Concentrated $\mathrm{H_2SO_4}$: dehydrating, water-absorbing (drying agent), strongly oxidising.
- **Nitrogen:** $\mathrm{NH_3}$ is the only common basic gas. $\mathrm{NO}$ (colourless) $\to\mathrm{NO_2}$ (red-brown) in air. Nitric acid is strongly oxidising: concentrated gives $\mathrm{NO_2}$, dilute gives NO, never $\mathrm{H_2}$.
- **Carbon/silicon:** $\mathrm{CO_2}$ turns limewater milky; $\mathrm{SiO_2}$ is used for optical fibres, Si for chips and solar cells.

## Worked examples

**Example 1.** How can you remove $\mathrm{FeCl_3}$ impurity from $\mathrm{FeCl_2}$ solution?

*Solution.* Add excess iron powder and filter.

**Example 2.** Why can NaOH solution not be stored in a glass bottle with a glass stopper?

*Solution.* NaOH reacts with $\mathrm{SiO_2}$ in glass to form sticky $\mathrm{Na_2SiO_3}$, gluing the stopper.

## Common traps

- Thinking all metals displace hydrogen from nitric acid.
- Thinking sodium sinks in water.
- Forgetting that $\mathrm{Al(OH)_3}$ dissolves in excess NaOH.
"""

N["organic"] = r"""
## Hydrocarbons

| Class | General formula | Example | Typical reaction |
|---|---|---|---|
| Alkanes | $\mathrm{C_nH_{2n+2}}$ | methane $\mathrm{CH_4}$ | substitution with $\mathrm{Cl_2}$ in light; combustion |
| Alkenes | $\mathrm{C_nH_{2n}}$ | ethene $\mathrm{CH_2=CH_2}$ | addition (decolourises bromine water), addition polymerisation, oxidised by $\mathrm{KMnO_4}$ |
| Alkynes | $\mathrm{C_nH_{2n-2}}$ | ethyne $\mathrm{HC\equiv CH}$ | addition |
| Benzene | $\mathrm{C_6H_6}$ | | substitution (bromination, nitration); does not decolourise bromine water by reaction |

**Isomers:** same molecular formula, different structure. $\mathrm{C_4H_{10}}$: $2$; $\mathrm{C_5H_{12}}$: $3$.

## Derivatives

| Class | Functional group | Example | Key reactions |
|---|---|---|---|
| Alcohol | $-\mathrm{OH}$ | ethanol $\mathrm{C_2H_5OH}$ | with Na (gives $\mathrm{H_2}$); oxidised to aldehyde (Cu, heat); esterification |
| Aldehyde | $-\mathrm{CHO}$ | ethanal $\mathrm{CH_3CHO}$ | reducing: silver mirror; red $\mathrm{Cu_2O}$ with fresh $\mathrm{Cu(OH)_2}$ |
| Carboxylic acid | $-\mathrm{COOH}$ | acetic acid $\mathrm{CH_3COOH}$ | acidic (with $\mathrm{Na_2CO_3}$ gives $\mathrm{CO_2}$); esterification |
| Ester | $-\mathrm{COO}-$ | ethyl acetate | hydrolysis (acid or base) |

Esterification: $\mathrm{CH_3COOH+C_2H_5OH\rightleftharpoons CH_3COOC_2H_5+H_2O}$ (conc. $\mathrm{H_2SO_4}$, heat). "Acid loses OH, alcohol loses H."

Biomolecules: glucose (reducing sugar), sucrose (non-reducing), starch (turns iodine blue), proteins (denatured by heat, heavy metals).

## Worked examples

**Example 1.** How can you distinguish ethene from methane?

*Solution.* Bubble each through bromine water: ethene decolourises it.

**Example 2.** $0.1$ mol of a hydrocarbon burns to $0.3$ mol $\mathrm{CO_2}$ and $0.4$ mol $\mathrm{H_2O}$. Formula?

*Solution.* C $=3$, H $=8$: $\mathrm{C_3H_8}$.

## Common traps

- Benzene does **not** add bromine from bromine water; it only extracts it.
- Writing esterification as going to completion — it is reversible.
"""

N["redox"] = r"""
## Key ideas

A redox reaction involves **electron transfer**, seen as changes in oxidation states.

| | Electrons | Oxidation state | Itself is | It is a(n) |
|---|---|---|---|---|
| Reducing agent | loses | rises | oxidised | reducing agent |
| Oxidising agent | gains | falls | reduced | oxidising agent |

Memory aid: **OIL RIG** — Oxidation Is Loss, Reduction Is Gain.

- Any reaction involving a free element changing into a compound (or the reverse) is redox. Most double-displacement and many decomposition reactions are not.
- Strength: in a reaction, oxidising agent > oxidised product, and reducing agent > reduced product.
- Common oxidising agents: $\mathrm{O_2,\ Cl_2,\ HNO_3,\ conc.\ H_2SO_4,\ KMnO_4,\ Fe^{3+}}$. Reducing agents: metals, $\mathrm{H_2,\ C,\ CO,\ Fe^{2+},\ I^-,\ S^{2-}}$.
- **Electron bookkeeping:** electrons lost = electrons gained. This also lets you balance equations.
- **Disproportionation:** the same element is both oxidised and reduced ($\mathrm{Cl_2+2NaOH}$).

## Worked examples

**Example 1.** In $\mathrm{2Fe^{3+}+2I^-\rightarrow2Fe^{2+}+I_2}$, identify the agents.

*Solution.* $\mathrm{Fe^{3+}}$ gains electrons: oxidising agent. $\mathrm{I^-}$ loses electrons: reducing agent.

**Example 2.** How many moles of electrons are transferred when $0.2$ mol Al reacts with acid?

*Solution.* Al $0\to+3$: $0.6$ mol.

**Example 3.** Balance $\mathrm{Cu+HNO_3(dil.)\rightarrow Cu(NO_3)_2+NO+H_2O}$.

*Solution.* Cu loses $2e^-$, N ($+5\to+2$) gains $3e^-$: $3$ Cu and $2$ NO. Then $\mathrm{3Cu+8HNO_3\rightarrow3Cu(NO_3)_2+2NO\uparrow+4H_2O}$.

## Common traps

- The oxidising agent is **reduced** (not oxidised).
- In $\mathrm{MnO_2}$ + conc. HCl only half of the HCl acts as reducing agent.
"""

N["ionic-reactions"] = r"""
## Ionic equations

Write **strong** acids, **strong** bases and **soluble** salts as ions; write precipitates, gases, water, weak acids/bases and oxides as formulas. Cancel spectator ions. Check atoms **and** charge.

Example: $\mathrm{CaCO_3+2H^+\rightarrow Ca^{2+}+H_2O+CO_2\uparrow}$ (marble is insoluble, so it stays as a formula).

An ionic reaction happens when a **precipitate**, a **gas** or a **weak electrolyte** (e.g. water) forms.

## Ions that cannot coexist

- $\mathrm{H^+}$ with $\mathrm{OH^-,\ CO_3^{2-},\ HCO_3^-,\ CH_3COO^-}$.
- $\mathrm{OH^-}$ with $\mathrm{NH_4^+,\ Mg^{2+},\ Cu^{2+},\ Fe^{3+},\ HCO_3^-}$.
- $\mathrm{Ba^{2+}}$ with $\mathrm{SO_4^{2-}}$; $\mathrm{Ag^+}$ with $\mathrm{Cl^-}$; $\mathrm{Ca^{2+}}$ with $\mathrm{CO_3^{2-}}$.
- Redox pairs: $\mathrm{Fe^{3+}}$ with $\mathrm{I^-}$; $\mathrm{NO_3^-/H^+}$ with $\mathrm{Fe^{2+}}$.
- "Colourless" excludes $\mathrm{Cu^{2+}}$ (blue), $\mathrm{Fe^{3+}}$ (yellow), $\mathrm{Fe^{2+}}$ (pale green), $\mathrm{MnO_4^-}$ (purple).

## Tests for ions

| Ion | Test | Result |
|---|---|---|
| $\mathrm{Cl^-}$ | $\mathrm{AgNO_3}$ + dilute $\mathrm{HNO_3}$ | white precipitate |
| $\mathrm{SO_4^{2-}}$ | dilute HCl first, then $\mathrm{BaCl_2}$ | white precipitate |
| $\mathrm{CO_3^{2-}}$ | dilute acid; gas into limewater | milky |
| $\mathrm{NH_4^+}$ | NaOH, warm; moist red litmus | turns blue |
| $\mathrm{Fe^{3+}}$ | KSCN | blood red |
| $\mathrm{Cu^{2+}}$ | NaOH | blue precipitate |
| $\mathrm{Na^+}$ / $\mathrm{K^+}$ | flame test | yellow / lilac (cobalt glass) |

## Worked examples

**Example 1.** Write the ionic equation for $\mathrm{BaCl_2+Na_2SO_4}$.

*Solution.* $\mathrm{Ba^{2+}+SO_4^{2-}\rightarrow BaSO_4\downarrow}$.

**Example 2.** Can $\mathrm{K^+,\ H^+,\ NO_3^-,\ CO_3^{2-}}$ coexist?

*Solution.* No: $\mathrm{2H^++CO_3^{2-}\rightarrow H_2O+CO_2\uparrow}$.

## Common traps

- Splitting insoluble substances or weak acids into ions.
- Unbalanced charge ($\mathrm{Fe+Fe^{3+}\rightarrow2Fe^{2+}}$ is wrong).
- Testing for sulfate with $\mathrm{BaCl_2}$ alone.
"""

N["atomic-periodic"] = r"""
## Atomic structure

$^A_Z\mathrm X$: protons $Z$, neutrons $A-Z$, electrons $Z$ (neutral atom). An ion $\mathrm{X^{n+}}$ has $Z-n$ electrons; $\mathrm{X^{n-}}$ has $Z+n$.

**Isotopes** (same $Z$, different $A$) have the same chemistry. Relative atomic mass is the abundance-weighted average of the isotope masses.

**Electron arrangement** (first 20 elements): shells hold $2,8,8,\dots$ e.g. Na $2,8,1$; Cl $2,8,7$; Ca $2,8,8,2$.

## Periodic table

- Period number = number of electron shells. Main-group number = number of outer electrons.
- Down a group: radius increases, metallic character increases, non-metallic character decreases.
- Across a period (left → right): radius decreases, metallic character decreases, non-metallic character and electronegativity increase.

Consequences:

- Basicity of hydroxides: $\mathrm{NaOH>Mg(OH)_2>Al(OH)_3}$; $\mathrm{KOH>NaOH}$.
- Acidity of highest oxyacids: $\mathrm{HClO_4>H_2SO_4>H_3PO_4>H_2SiO_3}$.
- Stability of hydrides: $\mathrm{HF>HCl>HBr>HI}$.
- Reactivity: alkali metals increase down the group; halogens decrease down the group.
- Ion radii: same electron arrangement → more protons, smaller ion ($\mathrm{O^{2-}>F^->Na^+>Mg^{2+}>Al^{3+}}$).

## Worked examples

**Example 1.** An element has $3$ shells and $7$ outer electrons. Identify it.

*Solution.* Period 3, Group VIIA: chlorine.

**Example 2.** Boron has isotopes $^{10}$B and $^{11}$B and $A_r=10.8$. Find the abundance of $^{10}$B.

*Solution.* $10x+11(1-x)=10.8\Rightarrow x=0.2$, i.e. $20\%$.

## Common traps

- Mass number vs relative atomic mass.
- Forgetting to adjust the electron count for ions.
"""

N["bonding"] = r"""
## Chemical bonds

| Bond | Formed between | Example | Properties of the substance |
|---|---|---|---|
| Ionic | active metal + active non-metal (electron transfer) | NaCl, MgO | high melting point; conducts when molten or dissolved |
| Covalent | non-metal atoms (shared pairs) | $\mathrm{H_2O,\ CO_2,\ CH_4}$ | molecular (low m.p.) or network (very high m.p.) |
| Metallic | metal cations + delocalised electrons | Cu, Fe | conducts as a solid, malleable |

- $\mathrm{N\equiv N}$ has a triple bond (3 shared pairs), $\mathrm{O=O}$ a double bond.
- Compounds like NaOH, $\mathrm{NH_4Cl}$, $\mathrm{Na_2O_2}$ contain both ionic and covalent bonds.
- **Polar bonds** join different atoms. A molecule is non-polar if the bond dipoles cancel by symmetry: $\mathrm{CO_2}$ (linear), $\mathrm{CH_4}$ (tetrahedral). $\mathrm{H_2O}$ (bent) and $\mathrm{NH_3}$ (pyramidal) are polar.

## Intermolecular forces

- **Van der Waals forces:** increase with molecular size, so the boiling points of the halogens increase from $\mathrm{F_2}$ to $\mathrm{I_2}$.
- **Hydrogen bonds:** between H on N, O or F and another N, O or F. They explain the high boiling points of $\mathrm{H_2O}$, HF and $\mathrm{NH_3}$, and why ice floats.
- Physical changes (melting, boiling, dissolving molecular substances) overcome intermolecular forces; chemical changes break bonds.

**Crystal types:** ionic (NaCl), molecular (ice, dry ice, iodine), covalent network (diamond, $\mathrm{SiO_2}$), metallic.

## Worked examples

**Example 1.** Which has a higher boiling point, $\mathrm{H_2O}$ or $\mathrm{H_2S}$? Why?

*Solution.* $\mathrm{H_2O}$, because of hydrogen bonding between molecules.

**Example 2.** Which bonds break when NaCl melts?

*Solution.* Ionic bonds (the ions separate).

## Common traps

- Hydrogen bonds are intermolecular forces, not chemical bonds.
- A molecule with polar bonds can be non-polar.
"""

N["rate-equilibrium"] = r"""
## Reaction rate

$v=\dfrac{\Delta c}{\Delta t}$ (mol/(L·s)). For $\mathrm{aA+bB\rightarrow cC}$, rates of different substances are in the ratio $a:b:c$.

Factors that increase the rate: higher **concentration** (or pressure for gases), higher **temperature**, **catalyst** (lowers activation energy), larger **surface area**. A catalyst speeds up the forward and reverse reactions equally.

## Chemical equilibrium

For a reversible reaction in a closed system, equilibrium is reached when $v_{\text{forward}}=v_{\text{reverse}}\ne0$. Concentrations stay **constant** (not necessarily equal). Signs of equilibrium: constant colour, constant pressure (if gas moles change), constant concentrations.

**Le Chatelier's principle:** a system at equilibrium shifts to oppose a change.

| Change | Shift |
|---|---|
| add a reactant / remove a product | to the right |
| increase pressure | toward fewer gas molecules |
| raise temperature | in the endothermic direction |
| catalyst | no shift (faster to reach equilibrium) |

**Equilibrium constant** for $\mathrm{aA+bB\rightleftharpoons cC+dD}$: $$K=\frac{[\mathrm C]^c[\mathrm D]^d}{[\mathrm A]^a[\mathrm B]^b}$$ (solids and pure liquids are left out). $K$ depends only on temperature. Conversion of A $=\dfrac{\text{A reacted}}{\text{A initial}}$.

## Worked examples

**Example 1.** For $\mathrm{N_2+3H_2\rightleftharpoons2NH_3}$ ($\Delta H<0$), how can the yield be increased?

*Solution.* Higher pressure, lower temperature, removing $\mathrm{NH_3}$.

**Example 2.** $[\mathrm{H_2}]=[\mathrm{I_2}]=0.1$, $[\mathrm{HI}]=0.8$ mol/L at equilibrium. Find $K$.

*Solution.* $K=\dfrac{0.64}{0.01}=64$.

## Common traps

- A catalyst changes the rate, not the yield.
- Pressure has no effect when the gas moles are equal on both sides.
- Equilibrium does not mean equal concentrations.
"""

N["electrolytes"] = r"""
## Electrolytes

- **Strong electrolytes** ionise completely: strong acids (HCl, $\mathrm{H_2SO_4}$, $\mathrm{HNO_3}$), strong bases (NaOH, KOH, $\mathrm{Ba(OH)_2}$), most salts.
- **Weak electrolytes** ionise partly (reversibly): weak acids ($\mathrm{CH_3COOH,\ H_2CO_3}$), weak bases ($\mathrm{NH_3\cdot H_2O}$), water.
- **Non-electrolytes:** sucrose, ethanol.
- Dilution increases the degree of ionisation of a weak electrolyte (but lowers its ion concentrations).

## Salt hydrolysis

"Whoever is stronger decides":

| Salt from | Example | Solution |
|---|---|---|
| strong acid + strong base | NaCl, $\mathrm{K_2SO_4}$ | neutral |
| strong acid + weak base | $\mathrm{NH_4Cl}$, $\mathrm{CuSO_4}$ | acidic |
| weak acid + strong base | $\mathrm{Na_2CO_3}$, $\mathrm{CH_3COONa}$ | basic |

e.g. $\mathrm{CO_3^{2-}+H_2O\rightleftharpoons HCO_3^-+OH^-}$.

## Electrochemistry

**Galvanic cell** (chemical → electrical): the more reactive metal is the **negative** electrode and is oxidised (Zn in Cu–Zn cell); electrons flow through the wire to the positive electrode.

**Electrolysis** (electrical → chemical): anode (connected to $+$) = oxidation, cathode = reduction. $\mathrm{CuCl_2}$ solution: Cu at the cathode, $\mathrm{Cl_2}$ at the anode. $\mathrm{Cu^{2+}+2e^-\rightarrow Cu}$: $2$ mol $e^-$ deposit $1$ mol Cu.

**Corrosion** of iron is electrochemical and speeds up in salt water; protect it by painting, galvanising (zinc), or connecting a more reactive metal.

## Worked examples

**Example 1.** Order the pH of $0.1$ mol/L NaCl, $\mathrm{NH_4Cl}$ and $\mathrm{Na_2CO_3}$.

*Solution.* $\mathrm{NH_4Cl}<\mathrm{NaCl}=7<\mathrm{Na_2CO_3}$.

**Example 2.** $0.4$ mol of electrons pass through $\mathrm{CuSO_4}$ solution. Mass of Cu deposited (Cu $64$)?

*Solution.* $0.2$ mol, $12.8$ g.

## Common traps

- "Weak electrolyte" refers to the degree of ionisation, not to solubility.
- The negative electrode of a galvanic cell is the anode (oxidation).
"""

N["lab-safety"] = r"""
## Safety rules

- Wear goggles; tie back hair; never taste chemicals; waft gases toward the nose.
- **Dilute concentrated sulfuric acid by adding acid to water**, slowly, with stirring.
- Test the purity of flammable gases ($\mathrm{H_2}$, CO, $\mathrm{CH_4}$) before lighting them.
- Toxic or smelly gases ($\mathrm{Cl_2,\ SO_2,\ NO_2,\ H_2S}$) in a fume cupboard, with exhaust gas absorbed (e.g. by NaOH solution).
- Spills: acid on skin — rinse with lots of water, then dilute $\mathrm{NaHCO_3}$; base on skin — water, then dilute boric acid. Alcohol fire — damp cloth. Never pour water on burning sodium (use dry sand).
- Prevent suck-back when heating and collecting gases over water: remove the delivery tube from the water **before** removing the flame.

## Apparatus

| Apparatus | Use | Note |
|---|---|---|
| Test tube, evaporating dish, crucible | heated directly | |
| Beaker, flask | heated on a gauze | |
| Measuring cylinder | measuring volumes (±0.1 mL) | never heat or dissolve in it |
| Volumetric flask | making a solution of exact concentration | one fixed volume; never heat |
| Burette | titration (±0.01 mL) | |
| Separating funnel | separating immiscible liquids | |
| Balance | weighing (±0.1 g) | corrosive solids in a beaker |

Reading a meniscus: eye level with the bottom of the meniscus. Looking down gives a reading that is too high for a cylinder.

## Worked examples

**Example 1.** Which operations are wrong: (a) heating a beaker directly; (b) dissolving NaOH in a volumetric flask; (c) lighting a spirit lamp with another lamp?

*Solution.* All three are wrong. Beakers need a gauze; solids are dissolved in a beaker first (dissolving releases heat and the flask is calibrated at room temperature); lamps are lit with a match.

**Example 2.** You collect oxygen over water from heated $\mathrm{KMnO_4}$. In which order do you finish?

*Solution.* First take the delivery tube out of the water, then remove the flame — otherwise cold water is sucked back into the hot tube and cracks it.

**Example 3.** Which apparatus would you use to measure exactly $25.00$ mL of an acid for a titration?

*Solution.* A burette or pipette (reading to $0.01$ mL); a measuring cylinder is only accurate to about $0.1$ mL.

## Common traps

- "Water into acid" — it boils and splashes.
- Heating measuring instruments.
"""

N["gas-preparation"] = r"""
## Common laboratory preparations

| Gas | Reagents | Apparatus type | Collection | Test |
|---|---|---|---|---|
| $\mathrm{O_2}$ | $\mathrm{KMnO_4}$ (heat); $\mathrm{KClO_3}$ + $\mathrm{MnO_2}$ (heat); $\mathrm{H_2O_2}$ + $\mathrm{MnO_2}$ | solid–heat or liquid, no heat | over water or upward air displacement | relights a glowing splint |
| $\mathrm{H_2}$ | Zn + dilute $\mathrm{H_2SO_4}$ | solid + liquid, no heat | over water or downward air displacement | "pop" with a lit splint |
| $\mathrm{CO_2}$ | marble + dilute HCl | solid + liquid, no heat | upward air displacement (dense, soluble) | turns limewater milky |
| $\mathrm{Cl_2}$ | $\mathrm{MnO_2}$ + conc. HCl, heat | solid + liquid, heat | upward air displacement or over saturated brine | moist starch–KI paper turns blue; bleaches |
| $\mathrm{NH_3}$ | $\mathrm{NH_4Cl}$ + $\mathrm{Ca(OH)_2}$, heat | solid–heat | downward air displacement | moist red litmus turns blue |

**Choosing a collection method:** insoluble and unreactive with water → over water. Denser than air ($M>29$) → upward displacement of air; less dense → downward.

**Drying agents:** conc. $\mathrm{H_2SO_4}$ (not for $\mathrm{NH_3}$ or reducing gases), soda lime/CaO (not for acidic gases), anhydrous $\mathrm{CaCl_2}$ (not for $\mathrm{NH_3}$).

**Purification order:** remove other impurities first, **dry last**. E.g. $\mathrm{Cl_2}$: saturated brine (removes HCl) → conc. $\mathrm{H_2SO_4}$.

## Worked examples

**Example 1.** Why is $\mathrm{CO_2}$ not prepared from marble and dilute $\mathrm{H_2SO_4}$?

*Solution.* Insoluble $\mathrm{CaSO_4}$ coats the marble and stops the reaction.

**Example 2.** How is $\mathrm{NH_3}$ dried and collected?

*Solution.* Soda lime; downward displacement of air.

## Common traps

- Drying before washing (the gas picks up water again).
- Collecting $\mathrm{NH_3}$ or HCl over water.
"""

N["separation"] = r"""
## Methods

| Method | Separates | Example |
|---|---|---|
| Filtration | insoluble solid from liquid | sand from salt water |
| Evaporation | dissolved solid from solvent | salt from brine |
| Crystallisation (cooling) | solid whose solubility changes a lot with temperature | $\mathrm{KNO_3}$ from a little NaCl |
| Distillation | liquids with different boiling points; pure water | water from sea water, ethanol from water |
| Extraction + separation | solute more soluble in another, immiscible solvent | iodine from iodine water with $\mathrm{CCl_4}$ |
| Separating funnel | immiscible liquids | oil and water |

**Distillation details:** thermometer bulb at the side arm; cooling water in at the bottom, out at the top; boiling chips to prevent bumping.

**Filtration:** "one paste, two lows, three touches" — paper tight against the funnel; paper below the funnel rim and liquid below the paper edge; beaker touching the glass rod, rod touching the triple layer, funnel tip touching the beaker wall.

## Removing impurities (chemical methods)

Principles: do not add new impurities, do not lose the wanted substance, easy to separate afterwards, add excess reagents in an order that lets later steps remove them.

Examples:

- $\mathrm{CO_2}$ in CO → NaOH solution.
- HCl in $\mathrm{CO_2}$ → saturated $\mathrm{NaHCO_3}$ solution.
- $\mathrm{Na_2SO_4}$ in NaCl → suitable $\mathrm{BaCl_2}$, filter.
- $\mathrm{FeCl_3}$ in $\mathrm{FeCl_2}$ → excess Fe, filter. $\mathrm{FeCl_2}$ in $\mathrm{FeCl_3}$ → $\mathrm{Cl_2}$.
- Purifying crude salt (removing $\mathrm{Ca^{2+},Mg^{2+},SO_4^{2-}}$): add excess $\mathrm{BaCl_2}$ **before** $\mathrm{Na_2CO_3}$ (which also removes the extra $\mathrm{Ba^{2+}}$), NaOH, filter, then HCl.

## Worked examples

**Example 1.** How do you obtain pure, dry salt from a mixture of salt and sand?

*Solution.* Dissolve in water, filter off the sand, evaporate the filtrate (stop heating when most of the water is gone and let the remaining heat dry the crystals).

**Example 2.** Ethanol (b.p. $78^\circ$C) is mixed with water. How do you separate them?

*Solution.* Distillation — they are miscible, so a separating funnel is useless; the ethanol distils first.

**Example 3.** How can HCl gas be removed from $\mathrm{CO_2}$?

*Solution.* Pass the gas through saturated $\mathrm{NaHCO_3}$ solution: $\mathrm{HCO_3^-+H^+\rightarrow H_2O+CO_2}$ removes HCl and even produces more $\mathrm{CO_2}$. NaOH would absorb the $\mathrm{CO_2}$ too.

## Common traps

- Using ethanol as an extraction solvent for water (it mixes with water).
- Choosing a reagent that introduces a new ion.
"""

N["industrial"] = r"""
## Ammonia synthesis (Haber process)

$$\mathrm{N_2(g)+3H_2(g)\rightleftharpoons2NH_3(g)}\qquad\Delta H<0$$

| Condition | Choice | Reason |
|---|---|---|
| Pressure | $10$–$30$ MPa | high pressure favours fewer gas molecules (higher yield) and speeds up the reaction; limited by equipment cost |
| Temperature | $400$–$500^\circ$C | compromise: lower T gives a higher yield but too slow a rate; the catalyst's best temperature |
| Catalyst | iron | faster, no change in yield |
| Recycling | unreacted $\mathrm{N_2,H_2}$ | only ~$15$–$25\%$ converted per pass |

Ammonia is cooled and liquefied to remove it, which shifts the equilibrium further right.

## Sulfuric acid (contact process)

$\mathrm{S}$ or pyrite → $\mathrm{SO_2}$; $\mathrm{2SO_2+O_2\rightleftharpoons2SO_3}$ ($\mathrm{V_2O_5}$ catalyst, about $450^\circ$C, normal pressure because conversion is already high); $\mathrm{SO_3}$ absorbed in **98% $\mathrm{H_2SO_4}$** to avoid acid mist.

## Other processes

- **Chlor-alkali:** electrolysis of saturated brine: $\mathrm{2NaCl+2H_2O\rightarrow2NaOH+H_2\uparrow+Cl_2\uparrow}$.
- **Nitric acid:** $\mathrm{NH_3}$ is oxidised on Pt to NO → $\mathrm{NO_2}$ → absorbed in water.
- **Metal extraction:** reactive metals (Na, Mg, Al) by electrolysis of molten compounds (Al: molten $\mathrm{Al_2O_3}$ with cryolite); middle metals (Fe, Zn, Cu) by reduction with C, CO or $\mathrm{H_2}$ (blast furnace: $\mathrm{Fe_2O_3+3CO\rightarrow2Fe+3CO_2}$); least reactive (Hg, Ag) by heating the oxides.

## Worked examples

**Example 1.** How much $\mathrm{NH_3}$ can be made from $56$ t of $\mathrm{N_2}$ in theory (N $14$, H $1$)?

*Solution.* $2$ mol $\mathrm{NH_3}$ per mol $\mathrm{N_2}$: $56$ t $\times\dfrac{34}{28}=68$ t.

**Example 2.** Why is the contact process run at normal pressure even though higher pressure would favour $\mathrm{SO_3}$?

*Solution.* At normal pressure the conversion is already over 90%, so the extra yield is not worth the cost of high-pressure equipment.

**Example 3.** Why is aluminium not made by heating $\mathrm{Al_2O_3}$ with carbon?

*Solution.* Aluminium is more reactive than carbon, so carbon cannot reduce its oxide; electrolysis of the molten oxide is needed.

## Common traps

- "Exothermic, so use low temperature" ignores the rate.
- A catalyst does not increase the yield.
"""

for k, v in N.items():
    (OUT / f"{k}.md").write_text(v.strip() + "\n", encoding="utf8")
    print("wrote", k)
