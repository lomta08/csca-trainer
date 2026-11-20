"""Writes the printable formula sheets to src/content/formulas/<subject>.md."""
from pathlib import Path

OUT = Path(__file__).resolve().parents[2] / "src" / "content" / "formulas"
OUT.mkdir(parents=True, exist_ok=True)
S = {}

S["math"] = r"""
## Sets & inequalities
- $n$ elements: $2^n$ subsets, $2^n-1$ proper subsets; $|A\cup B|=|A|+|B|-|A\cap B|$
- AM–GM ($a,b>0$): $\frac{a+b}2\ge\sqrt{ab}$, equality iff $a=b$
- $ax^2+bx+c<0$ ($a>0$, roots $x_1<x_2$): $x_1<x<x_2$; $>0$: outside the roots
- $\frac PQ\ge0\iff PQ\ge0,\ Q\ne0$

## Exponents & logarithms
- $a^ma^n=a^{m+n}$, $(a^m)^n=a^{mn}$, $a^{-n}=\frac1{a^n}$, $a^{\frac mn}=\sqrt[n]{a^m}$
- $\log_a(MN)=\log_aM+\log_aN$, $\log_aM^n=n\log_aM$, $\log_ab=\frac{\log_cb}{\log_ca}$, $a^{\log_aN}=N$

## Trigonometry
- $\sin^2\alpha+\cos^2\alpha=1$, $\tan\alpha=\frac{\sin\alpha}{\cos\alpha}$; $180^\circ=\pi$
- $\sin(\alpha\pm\beta)=\sin\alpha\cos\beta\pm\cos\alpha\sin\beta$; $\cos(\alpha\pm\beta)=\cos\alpha\cos\beta\mp\sin\alpha\sin\beta$
- $\sin2\alpha=2\sin\alpha\cos\alpha$; $\cos2\alpha=2\cos^2\alpha-1=1-2\sin^2\alpha$
- $a\sin x+b\cos x=\sqrt{a^2+b^2}\sin(x+\varphi)$; $T=\frac{2\pi}{|\omega|}$
- $\frac a{\sin A}=\frac b{\sin B}=2R$; $c^2=a^2+b^2-2ab\cos C$; $S=\frac12ab\sin C$
- $\sin30^\circ=\frac12$, $\sin45^\circ=\frac{\sqrt2}2$, $\sin60^\circ=\frac{\sqrt3}2$; $\tan30^\circ=\frac{\sqrt3}3$, $\tan60^\circ=\sqrt3$

## Sequences
- Arithmetic: $a_n=a_1+(n-1)d$, $S_n=\frac{n(a_1+a_n)}2=na_1+\frac{n(n-1)}2d$
- Geometric: $a_n=a_1q^{n-1}$, $S_n=\frac{a_1(1-q^n)}{1-q}$ ($q\ne1$)
- $a_n=S_n-S_{n-1}$ ($n\ge2$), $a_1=S_1$

## Derivatives & integrals
- $(x^n)'=nx^{n-1}$, $(\sin x)'=\cos x$, $(\cos x)'=-\sin x$, $(e^x)'=e^x$, $(\ln x)'=\frac1x$, $(a^x)'=a^x\ln a$
- $(uv)'=u'v+uv'$, $\left(\frac uv\right)'=\frac{u'v-uv'}{v^2}$, $[f(g(x))]'=f'(g)g'$
- Tangent: $y-f(x_0)=f'(x_0)(x-x_0)$; $\int_a^bf\,dx=F(b)-F(a)$

## Analytic geometry
- $k=\frac{y_2-y_1}{x_2-x_1}$; $\parallel$: $k_1=k_2$; $\perp$: $k_1k_2=-1$ ($A_1A_2+B_1B_2=0$)
- $d=\frac{|Ax_0+By_0+C|}{\sqrt{A^2+B^2}}$; parallel lines $d=\frac{|C_1-C_2|}{\sqrt{A^2+B^2}}$
- Circle $(x-a)^2+(y-b)^2=r^2$; $x^2+y^2+Dx+Ey+F=0$: centre $(-\frac D2,-\frac E2)$; chord $2\sqrt{r^2-d^2}$
- Ellipse $\frac{x^2}{a^2}+\frac{y^2}{b^2}=1$: $c^2=a^2-b^2$, $e=\frac ca<1$, $|PF_1|+|PF_2|=2a$
- Hyperbola $\frac{x^2}{a^2}-\frac{y^2}{b^2}=1$: $c^2=a^2+b^2$, $e>1$, asymptotes $y=\pm\frac bax$
- Parabola $y^2=2px$: focus $(\frac p2,0)$, directrix $x=-\frac p2$, $|PF|=x_0+\frac p2$

## Vectors & complex numbers
- $\vec a\cdot\vec b=|\vec a||\vec b|\cos\theta=x_1x_2+y_1y_2$; $\perp$: $x_1x_2+y_1y_2=0$; $\parallel$: $x_1y_2-x_2y_1=0$
- $|\vec a\pm\vec b|^2=|\vec a|^2\pm2\vec a\cdot\vec b+|\vec b|^2$
- $i^2=-1$; $|a+bi|=\sqrt{a^2+b^2}$; $\frac{z_1}{z_2}=\frac{z_1\bar z_2}{|z_2|^2}$; $i^n$ has period $4$

## Solid geometry
- $|AB|=\sqrt{\Delta x^2+\Delta y^2+\Delta z^2}$; box diagonal $\sqrt{a^2+b^2+c^2}$
- Prism/cylinder $V=Sh$; cone/pyramid $V=\frac13Sh$; sphere $V=\frac43\pi R^3$, $S=4\pi R^2$; cone lateral $\pi rl$

## Probability & statistics
- $P(A)=\frac mn$; $P(\bar A)=1-P(A)$; $P(A\cup B)=P(A)+P(B)-P(AB)$; independent: $P(AB)=P(A)P(B)$
- $C_n^k=\frac{n!}{k!(n-k)!}$, $A_n^k=\frac{n!}{(n-k)!}$
- $\bar x=\frac1n\sum x_i$, $s^2=\frac1n\sum(x_i-\bar x)^2$; $D(aX+b)=a^2D(X)$, $E(aX+b)=aE(X)+b$
- $N(\mu,\sigma^2)$: symmetric about $\mu$; $\pm\sigma$: $0.6827$, $\pm2\sigma$: $0.9545$, $\pm3\sigma$: $0.9973$
"""

S["physics"] = r"""
## Kinematics ($g=10\ \text{m/s}^2$)
- $v=v_0+at$, $x=v_0t+\frac12at^2$, $v^2-v_0^2=2ax$, $\bar v=\frac{v_0+v}2$, $\Delta x=aT^2$
- Free fall: $v=gt$, $h=\frac12gt^2$; thrown up: $h_{\max}=\frac{v_0^2}{2g}$
- Horizontal projectile: $x=v_0t$, $y=\frac12gt^2$

## Forces & Newton's laws
- $F=ma$; $G=mg$; $f=\mu N$; $F=kx$
- Incline: $mg\sin\theta$ along, $mg\cos\theta$ perpendicular; lift: $N=m(g\pm a)$

## Momentum
- $p=mv$, $I=Ft=\Delta p$; $m_1v_1+m_2v_2=m_1v_1'+m_2v_2'$

## Work & energy
- $W=Fs\cos\theta$, $P=\frac Wt=Fv$; $E_k=\frac12mv^2$, $E_p=mgh$, $E_{\text{spring}}=\frac12kx^2$
- $W_{\text{net}}=\Delta E_k$; no friction: $E_k+E_p=$ const; $v_{\max}=\frac Pf$

## Circular motion & gravitation
- $v=\omega r=\frac{2\pi r}T$, $a=\frac{v^2}r=\omega^2r$, $F=\frac{mv^2}r$
- $F=\frac{GMm}{r^2}$, $GM=gR^2$, $v=\sqrt{\frac{GM}r}$, $T=2\pi\sqrt{\frac{r^3}{GM}}$; $v_1=7.9$ km/s

## Oscillations & waves
- Spring $T=2\pi\sqrt{\frac mk}$; pendulum $T=2\pi\sqrt{\frac Lg}$; $v_{\max}=A\omega$
- $v=f\lambda=\frac\lambda T$, $\omega=2\pi f$

## Electrostatics
- $F=k\frac{q_1q_2}{r^2}$ ($k=9\times10^9$); $E=\frac Fq$, $E=\frac{kQ}{r^2}$, $E=\frac Ud$
- $U_{AB}=\frac{W_{AB}}q$; $qU=\frac12mv^2$; $C=\frac QU$, $C\propto\frac Sd$

## DC circuits
- $I=\frac UR$, $R=\rho\frac LS$; series $R=R_1+R_2$; parallel $\frac1R=\frac1{R_1}+\frac1{R_2}$
- $P=UI=I^2R=\frac{U^2}R$; $I=\frac E{R+r}$, $U=E-Ir$; $P_{\text{out,max}}=\frac{E^2}{4r}$ at $R=r$

## Magnetism & induction
- $F=BIL$; $F=qvB$; $r=\frac{mv}{qB}$, $T=\frac{2\pi m}{qB}$; $\Phi=BS$
- $E=n\frac{\Delta\Phi}{\Delta t}$, $E=BLv$; transformer $\frac{U_1}{U_2}=\frac{n_1}{n_2}$, $P_{\text{loss}}=I^2R$

## Heat
- $T=t+273$; $\frac{p_1V_1}{T_1}=\frac{p_2V_2}{T_2}$; $pV=nRT$ ($R=8.31$); $\Delta U=Q+W$

## Optics
- $n=\frac{\sin i}{\sin r}=\frac cv$; $\sin C=\frac1n$; apparent depth $=\frac{h}n$
- Double slit $\Delta x=\frac Ld\lambda$; bright: $\delta=k\lambda$, dark: $\delta=(2k+1)\frac\lambda2$

## Modern physics
- $E=h\nu=\frac{hc}\lambda$ ($h=6.63\times10^{-34}$ J·s); $E_k=h\nu-W_0$, $W_0=h\nu_0$, $eU_c=E_k$
- $E_n=\frac{-13.6\ \text{eV}}{n^2}$; $h\nu=E_m-E_n$; lines from level $n$: $C_n^2$
- $\alpha$: $A-4$, $Z-2$; $\beta^-$: $Z+1$; $N=N_0(\frac12)^{t/T}$; $\Delta E=\Delta mc^2$
- $c=3\times10^8$ m/s; $e=1.6\times10^{-19}$ C; $1$ eV $=1.6\times10^{-19}$ J
"""

S["chemistry"] = r"""
## Amount of substance
- $n=\frac N{N_A}=\frac mM=\frac V{V_m}=cV$; $N_A=6.02\times10^{23}\ \text{mol}^{-1}$; $V_m=22.4$ L/mol (STP, gases only)
- $c_1V_1=c_2V_2$ (dilution); $w=\frac{m_{\text{solute}}}{m_{\text{solution}}}$; $M=22.4\rho$ (STP)
- Same $T,p$: $\frac{V_1}{V_2}=\frac{n_1}{n_2}$, $\frac{\rho_1}{\rho_2}=\frac{M_1}{M_2}$; $pV=nRT$

## pH (25 °C)
- $\text{pH}=-\lg[\mathrm{H^+}]$; $[\mathrm{H^+}][\mathrm{OH^-}]=10^{-14}$

## Relative atomic masses
- H 1, C 12, N 14, O 16, Na 23, Mg 24, Al 27, S 32, Cl 35.5, K 39, Ca 40, Fe 56, Cu 64, Zn 65, Ag 108, Ba 137

## Redox
- Oxidising agent: gains $e^-$, is reduced; reducing agent: loses $e^-$, is oxidised
- Electrons lost = electrons gained

## Ion tests
- $\mathrm{Cl^-}$: $\mathrm{AgNO_3}$/$\mathrm{HNO_3}$ white ppt; $\mathrm{SO_4^{2-}}$: HCl then $\mathrm{BaCl_2}$ white ppt
- $\mathrm{NH_4^+}$: NaOH, heat, red litmus → blue; $\mathrm{Fe^{3+}}$: KSCN red; $\mathrm{Cu^{2+}}$: NaOH blue ppt
- $\mathrm{CO_2}$: limewater milky; $\mathrm{O_2}$: relights splint; $\mathrm{H_2}$: pop; $\mathrm{Cl_2}$: starch–KI blue
- Flames: Na yellow, K lilac, Ca brick red, Cu blue-green

## Key reactions
- $\mathrm{2Na+2H_2O\rightarrow2NaOH+H_2}$; $\mathrm{2Na_2O_2+2CO_2\rightarrow2Na_2CO_3+O_2}$
- $\mathrm{Al(OH)_3+NaOH\rightarrow NaAlO_2+2H_2O}$; $\mathrm{2FeCl_3+Fe\rightarrow3FeCl_2}$
- $\mathrm{Cl_2+H_2O\rightleftharpoons HCl+HClO}$; $\mathrm{Cl_2+2NaOH\rightarrow NaCl+NaClO+H_2O}$
- $\mathrm{3Cu+8HNO_3(dil.)\rightarrow3Cu(NO_3)_2+2NO+4H_2O}$; $\mathrm{Cu+4HNO_3(conc.)\rightarrow Cu(NO_3)_2+2NO_2+2H_2O}$
- $\mathrm{MnO_2+4HCl(conc.)\xrightarrow{\Delta}MnCl_2+Cl_2+2H_2O}$; $\mathrm{CaCO_3+2HCl\rightarrow CaCl_2+H_2O+CO_2}$
- $\mathrm{2NH_4Cl+Ca(OH)_2\xrightarrow{\Delta}CaCl_2+2NH_3+2H_2O}$

## Organic
- Alkanes $\mathrm{C_nH_{2n+2}}$ (substitution); alkenes $\mathrm{C_nH_{2n}}$ (addition); benzene $\mathrm{C_6H_6}$
- $-\mathrm{OH}$ alcohol, $-\mathrm{CHO}$ aldehyde, $-\mathrm{COOH}$ acid, $-\mathrm{COO-}$ ester
- $\mathrm{CH_3COOH+C_2H_5OH\rightleftharpoons CH_3COOC_2H_5+H_2O}$ (conc. $\mathrm{H_2SO_4}$, heat)

## Periodic trends
- Across a period: radius ↓, non-metallic character ↑; down a group: radius ↑, metallic character ↑
- Acids $\mathrm{HClO_4>H_2SO_4>H_3PO_4>H_2SiO_3}$; bases $\mathrm{KOH>NaOH>Mg(OH)_2>Al(OH)_3}$

## Rate & equilibrium
- $v=\frac{\Delta c}{\Delta t}$, rates ∝ coefficients; $K=\frac{[\mathrm C]^c[\mathrm D]^d}{[\mathrm A]^a[\mathrm B]^b}$ (depends only on $T$)
- Le Chatelier: pressure ↑ → fewer gas moles; temperature ↑ → endothermic side; catalyst: no shift

## Electrochemistry & hydrolysis
- Galvanic: active metal = negative electrode (oxidation); electrolysis: anode oxidation, cathode reduction
- Salts: strong acid + weak base → acidic ($\mathrm{NH_4Cl}$); weak acid + strong base → basic ($\mathrm{Na_2CO_3}$)

## Industry
- Haber: $\mathrm{N_2+3H_2\rightleftharpoons2NH_3}$, Fe, 400–500 °C, 10–30 MPa, recycle
- Contact: $\mathrm{2SO_2+O_2\rightleftharpoons2SO_3}$, $\mathrm{V_2O_5}$; absorb in 98% $\mathrm{H_2SO_4}$
- Chlor-alkali: $\mathrm{2NaCl+2H_2O\rightarrow2NaOH+H_2+Cl_2}$
"""

for k, v in S.items():
    (OUT / f"{k}.md").write_text(v.strip() + "\n", encoding="utf8")
    print("wrote", k)
