from qb import *  # noqa: F403

B = Bank("chemistry", "basic-concepts")

# standard relative atomic masses used throughout the site
Ar = {"H": 1, "C": 12, "N": 14, "O": 16, "Na": 23, "Mg": 24, "Al": 27, "S": 32, "Cl": 35.5, "K": 39, "Ca": 40, "Fe": 56, "Cu": 64, "Zn": 65}
NA = 6.02e23
VM = 22.4


def Mr(formula: dict) -> float:
    return sum(Ar[el] * cnt for el, cnt in formula.items())


def masses(*els):
    return "(Relative atomic masses: " + ", ".join(f"{el} ${Ar[el]:g}$" for el in els) + ")"


# --------------------------------------------------- classification & states
B.q("c-mat-01", "matter-classification", 1,
    r"Which of the following is a **pure substance**?",
    [r"Distilled water", r"Air", r"Sea water", r"Steel"],
    r"Distilled water contains only $\mathrm{H_2O}$. Air is a mixture of gases, sea water is a solution of salts, and steel is an alloy (a mixture of iron and carbon, etc.).")

B.q("c-mat-02", "matter-classification", 1,
    r"Which of the following is a **chemical** change?",
    [r"Iron rusting", r"Ice melting", r"Sugar dissolving in water", r"Alcohol evaporating"],
    r"Rusting forms a new substance (hydrated iron(III) oxide). Melting, dissolving and evaporating change only the state or the mixing, not the substances themselves.")

B.q("c-mat-03", "matter-classification", 1,
    r"Which substance is an **element**?",
    [r"$\mathrm{O_3}$", r"$\mathrm{H_2O}$", r"$\mathrm{NaCl}$", r"$\mathrm{CO_2}$"],
    r"Ozone $\mathrm{O_3}$ contains only oxygen atoms, so it is an element (an allotrope of oxygen). The others are compounds of two elements.")

B.q("c-mat-04", "matter-classification", 2,
    r"Which property distinguishes a colloid from a solution?",
    [r"A colloid shows the Tyndall effect", r"A colloid is always coloured", r"A colloid's particles pass through filter paper but a solution's do not", r"A solution is always a liquid"],
    r"Colloid particles ($1$–$100$ nm) scatter a beam of light, making its path visible (the Tyndall effect). Both colloid and solution particles pass through filter paper.")

B.q("c-mat-05", "matter-classification", 2,
    r"Which pair are **allotropes**?",
    [r"Diamond and graphite", r"$^{12}\mathrm{C}$ and $^{14}\mathrm{C}$", r"$\mathrm{H_2O}$ and $\mathrm{H_2O_2}$", r"$\mathrm{CO}$ and $\mathrm{CO_2}$"],
    r"Allotropes are different forms of the **same element**: diamond and graphite are both pure carbon. $^{12}\mathrm C$ and $^{14}\mathrm C$ are isotopes (atoms); the other pairs are different compounds.")

B.q("c-mat-06", "matter-classification", 1,
    r"$\mathrm{Na_2CO_3}$ belongs to which class of compounds?",
    [r"Salt", r"Base", r"Acid", r"Oxide"],
    r"Sodium carbonate is made of a metal cation ($\mathrm{Na^+}$) and an acid anion ($\mathrm{CO_3^{2-}}$), so it is a salt, even though its solution is alkaline (it is commonly called soda ash).")

B.q("c-mat-07", "matter-classification", 2,
    r"Which of the following is an **acidic oxide**?",
    [r"$\mathrm{SO_2}$", r"$\mathrm{Na_2O}$", r"$\mathrm{CaO}$", r"$\mathrm{CO}$"],
    r"$\mathrm{SO_2}$ reacts with bases to give salt and water ($\mathrm{SO_2+2NaOH\rightarrow Na_2SO_3+H_2O}$). $\mathrm{Na_2O}$ and $\mathrm{CaO}$ are basic oxides; $\mathrm{CO}$ is a neutral (non-salt-forming) oxide.")

B.q("c-mat-08", "matter-classification", 1,
    r"When a substance changes directly from solid to gas (as with dry ice), the process is called",
    [r"sublimation", r"evaporation", r"melting", r"condensation"],
    r"Solid → gas directly is sublimation; gas → solid directly is deposition. Dry ice (solid $\mathrm{CO_2}$) sublimes at atmospheric pressure.")

B.q("c-mat-09", "matter-classification", 3,
    r"Which statement is correct?",
    [r"A substance made of one element can be a mixture", r"All compounds contain oxygen", r"A substance made of one element must be a pure substance", r"Every mixture is a solution"],
    r"A mixture of $\mathrm{O_2}$ and $\mathrm{O_3}$ contains only oxygen but is a mixture of two substances. Many compounds (e.g. $\mathrm{NaCl}$) contain no oxygen, and suspensions and colloids are mixtures that are not solutions.")

# ---------------------------------------------------- notation & equations
B.q("c-eqn-01", "chemical-equations", 2,
    r"In the balanced equation $a\,\mathrm{H_2}+b\,\mathrm{O_2}\rightarrow c\,\mathrm{H_2O}$ with smallest whole numbers, $a+b+c=$",
    [r"$5$", r"$4$", r"$3$", r"$6$"],
    r"$2\mathrm{H_2}+\mathrm{O_2}\rightarrow2\mathrm{H_2O}$ balances H ($4=4$) and O ($2=2$). Sum: $2+1+2=5$.",
    N(sum(sp.solve([2 * a - 2 * k, 2 * b - k, b - 1], [a, b, k]).values())))

_bal = sp.symbols("p q r s", positive=True)
_sol2 = sp.solve([_bal[0] * 4 - _bal[3] * 2, _bal[0] * 1 - _bal[2], _bal[1] * 2 - (_bal[2] * 2 + _bal[3]), _bal[0] - 1], _bal, dict=True)[0]
_scale2 = sp.ilcm(*[sp.fraction(v)[1] for v in _sol2.values()])
_coeffs2 = [int(_sol2[s_] * _scale2) for s_ in _bal]
B.q("c-eqn-02", "chemical-equations", 2,
    r"When methane burns completely, $\mathrm{CH_4}+x\,\mathrm{O_2}\rightarrow\mathrm{CO_2}+y\,\mathrm{H_2O}$. The values of $x$ and $y$ are",
    [r"$x=2,\ y=2$", r"$x=1,\ y=2$", r"$x=2,\ y=1$", r"$x=3,\ y=2$"],
    r"Balance C first ($1$ $\mathrm{CO_2}$), then H: $4$ H gives $2\mathrm{H_2O}$. Oxygen atoms on the right: $2+2=4$, so $2\mathrm{O_2}$: $\mathrm{CH_4+2O_2\rightarrow CO_2+2H_2O}$.",
    Nums(_coeffs2[1], _coeffs2[3]))

B.q("c-eqn-03", "chemical-equations", 1,
    r"The valence (oxidation state) of N in $\mathrm{HNO_3}$ is",
    [r"$+5$", r"$+3$", r"$-3$", r"$+4$"],
    r"The sum of oxidation states is $0$: $(+1)+x+3\times(-2)=0\Rightarrow x=+5$.",
    N(0 - (1 + 3 * -2)))

B.q("c-eqn-04", "chemical-equations", 1,
    r"The reaction $\mathrm{Zn+H_2SO_4\rightarrow ZnSO_4+H_2\uparrow}$ is a",
    [r"displacement (single replacement) reaction", r"combination reaction", r"decomposition reaction", r"double displacement reaction"],
    r"An element ($\mathrm{Zn}$) replaces another element ($\mathrm H$) from a compound: element + compound → new element + new compound.")

B.q("c-eqn-05", "chemical-equations", 1,
    r"The correct chemical formula of aluminium sulfate is",
    [r"$\mathrm{Al_2(SO_4)_3}$", r"$\mathrm{AlSO_4}$", r"$\mathrm{Al_3(SO_4)_2}$", r"$\mathrm{Al(SO_4)_3}$"],
    r"$\mathrm{Al^{3+}}$ and $\mathrm{SO_4^{2-}}$: the charges balance with $2\times(+3)=3\times(-2)$, giving $\mathrm{Al_2(SO_4)_3}$.")

B.q("c-eqn-06", "chemical-equations", 2,
    r"In $\mathrm{Fe_2O_3}+3\mathrm{CO}\xrightarrow{\text{high temp}}2\mathrm{Fe}+3\mathrm{CO_2}$, how many grams of iron are produced from $160$ g of $\mathrm{Fe_2O_3}$? " + masses("Fe", "O"),
    [r"$112$ g", r"$56$ g", r"$160$ g", r"$224$ g"],
    r"$M(\mathrm{Fe_2O_3})=2\times56+3\times16=160$ g/mol, so $160$ g is $1$ mol, giving $2$ mol Fe $=112$ g.",
    R(160 / Mr({"Fe": 2, "O": 3}) * 2 * Ar["Fe"]))

B.q("c-eqn-07", "chemical-equations", 2,
    r"In the reaction $2\mathrm{KClO_3}\xrightarrow[\Delta]{\mathrm{MnO_2}}2\mathrm{KCl}+3\mathrm{O_2}\uparrow$, the role of $\mathrm{MnO_2}$ is",
    [r"catalyst", r"reactant", r"oxidising agent", r"product"],
    r"$\mathrm{MnO_2}$ speeds up the decomposition and is unchanged in mass and chemical nature at the end, so it is a catalyst (written above the arrow).")

B.q("c-eqn-08", "chemical-equations", 2,
    r"The relative molecular mass of $\mathrm{CuSO_4\cdot5H_2O}$ is " + masses("Cu", "S", "O", "H"),
    [r"$250$", r"$160$", r"$178$", r"$268$"],
    r"$\mathrm{CuSO_4}=64+32+64=160$ and $5\mathrm{H_2O}=5\times18=90$. Total $250$.",
    N(Mr({"Cu": 1, "S": 1, "O": 4}) + 5 * Mr({"H": 2, "O": 1})))

B.q("c-eqn-09", "chemical-equations", 3,
    r"The mass fraction of nitrogen in ammonium nitrate, $\mathrm{NH_4NO_3}$, is " + masses("N", "H", "O"),
    [r"$35\%$", r"$17.5\%$", r"$28\%$", r"$46.7\%$"],
    r"$M=14+4+14+48=80$. Nitrogen: $2\times14=28$. Fraction $=\dfrac{28}{80}=35\%$. (Counting only one N gives $17.5\%$.)",
    R(100 * 2 * Ar["N"] / Mr({"N": 2, "H": 4, "O": 3})))

# ------------------------------------------------ concentration & pH
B.q("c-con-01", "concentration-ph", 2,
    r"$4.0$ g of NaOH is dissolved in water to make $500$ mL of solution. The concentration is " + masses("Na", "O", "H"),
    [r"$0.2$ mol/L", r"$0.1$ mol/L", r"$8$ mol/L", r"$2$ mol/L"],
    r"$n=\dfrac{4.0}{40}=0.1$ mol; $c=\dfrac nV=\dfrac{0.1}{0.5}=0.2$ mol/L. Remember to convert mL to L.",
    R(4.0 / Mr({"Na": 1, "O": 1, "H": 1}) / 0.5))

B.q("c-con-02", "concentration-ph", 1,
    r"The pH of $0.01$ mol/L hydrochloric acid is",
    [r"$2$", r"$1$", r"$0.01$", r"$12$"],
    r"HCl is a strong acid, fully ionised: $[\mathrm{H^+}]=10^{-2}$ mol/L, so $\mathrm{pH}=-\lg10^{-2}=2$.",
    N(-sp.log(sp.Rational(1, 100), 10)))

B.q("c-con-03", "concentration-ph", 2,
    r"The pH of $0.001$ mol/L NaOH solution at $25^\circ$C is",
    [r"$11$", r"$3$", r"$10$", r"$14$"],
    r"$[\mathrm{OH^-}]=10^{-3}$, so $[\mathrm{H^+}]=\dfrac{10^{-14}}{10^{-3}}=10^{-11}$ and $\mathrm{pH}=11$.",
    N(-sp.log(sp.Rational(10) ** -14 / sp.Rational(1, 1000), 10)))

B.q("c-con-04", "concentration-ph", 2,
    r"$100$ mL of $2$ mol/L $\mathrm{H_2SO_4}$ is diluted with water to $500$ mL. The new concentration is",
    [r"$0.4$ mol/L", r"$10$ mol/L", r"$0.8$ mol/L", r"$1$ mol/L"],
    r"The amount of solute is unchanged on dilution: $c_1V_1=c_2V_2\Rightarrow c_2=\dfrac{2\times100}{500}=0.4$ mol/L.",
    R(2 * 100 / 500))

B.q("c-con-05", "concentration-ph", 2,
    r"$20$ g of salt is dissolved in $80$ g of water. The mass fraction of salt in the solution is",
    [r"$20\%$", r"$25\%$", r"$80\%$", r"$16\%$"],
    r"Mass fraction $=\dfrac{\text{solute}}{\text{solution}}=\dfrac{20}{20+80}=20\%$. (Dividing by the water only gives $25\%$.)",
    R(100 * 20 / (20 + 80)))

B.q("c-con-06", "concentration-ph", 3,
    r"The concentration of $\mathrm{Cl^-}$ in $0.5$ mol/L $\mathrm{CaCl_2}$ solution is",
    [r"$1$ mol/L", r"$0.5$ mol/L", r"$0.25$ mol/L", r"$1.5$ mol/L"],
    r"Each $\mathrm{CaCl_2}$ gives $2\,\mathrm{Cl^-}$: $c(\mathrm{Cl^-})=2\times0.5=1$ mol/L. The volume of solution does not matter.",
    R(2 * 0.5))

B.q("c-con-07", "concentration-ph", 2,
    r"Solutions with pH $3$ and pH $5$ are compared. The $[\mathrm{H^+}]$ of the first is how many times that of the second?",
    [r"$100$", r"$2$", r"$\dfrac{5}{3}$", r"$1000$"],
    r"Each pH unit is a factor of $10$: $\dfrac{10^{-3}}{10^{-5}}=10^2=100$.",
    N(sp.Rational(10) ** -3 / sp.Rational(10) ** -5))

B.q("c-con-08", "concentration-ph", 3,
    r"$50$ mL of $0.2$ mol/L HCl is mixed with $50$ mL of $0.1$ mol/L NaOH (assume volumes add). The pH of the mixture is about",
    [r"$1.3$", r"$1$", r"$7$", r"$2$"],
    r"$n(\mathrm{H^+})=0.01$ mol, $n(\mathrm{OH^-})=0.005$ mol. Excess $\mathrm{H^+}=0.005$ mol in $0.1$ L: $0.05$ mol/L. $\mathrm{pH}=-\lg0.05\approx1.3$.",
    R(-sp.log((0.05 * 0.2 - 0.05 * 0.1) / 0.1, 10), rel=0.03))

B.q("c-con-09", "concentration-ph", 1,
    r"At $25^\circ$C a solution with pH $=9$ is",
    [r"alkaline (basic)", r"acidic", r"neutral", r"strongly acidic"],
    r"At $25^\circ$C, pH $<7$ is acidic, $=7$ neutral, $>7$ alkaline. pH $9$ means $[\mathrm{OH^-}]>[\mathrm{H^+}]$.")

B.q("c-con-10", "concentration-ph", 3,
    r"To prepare $250$ mL of $0.1$ mol/L $\mathrm{Na_2CO_3}$ solution, the mass of anhydrous $\mathrm{Na_2CO_3}$ needed is " + masses("Na", "C", "O"),
    [r"$2.65$ g", r"$10.6$ g", r"$26.5$ g", r"$1.06$ g"],
    r"$n=cV=0.1\times0.25=0.025$ mol; $M=2\times23+12+48=106$ g/mol; $m=0.025\times106=2.65$ g.",
    R(0.1 * 0.25 * Mr({"Na": 2, "C": 1, "O": 3})))

# ------------------------------------------------------ amount of substance
B.q("c-mol-01", "mole-calculations", 2,
    r"The amount of substance in $36$ g of water is " + masses("H", "O"),
    [r"$2$ mol", r"$36$ mol", r"$1$ mol", r"$0.5$ mol"],
    r"$M(\mathrm{H_2O})=18$ g/mol; $n=\dfrac mM=\dfrac{36}{18}=2$ mol.",
    R(36 / Mr({"H": 2, "O": 1})))

B.q("c-mol-02", "mole-calculations", 2,
    r"The number of molecules in $0.5$ mol of $\mathrm{CO_2}$ is ($N_A=6.02\times10^{23}\ \text{mol}^{-1}$)",
    [r"$3.01\times10^{23}$", r"$6.02\times10^{23}$", r"$1.204\times10^{24}$", r"$9.03\times10^{23}$"],
    r"$N=nN_A=0.5\times6.02\times10^{23}=3.01\times10^{23}$.",
    R(0.5 * NA))

B.q("c-mol-03", "mole-calculations", 2,
    r"The number of atoms in $0.5$ mol of $\mathrm{CO_2}$ is ($N_A=6.02\times10^{23}\ \text{mol}^{-1}$)",
    [r"$9.03\times10^{23}$", r"$3.01\times10^{23}$", r"$1.806\times10^{24}$", r"$6.02\times10^{23}$"],
    r"Each molecule has $3$ atoms: $0.5\times3=1.5$ mol of atoms, i.e. $1.5\times6.02\times10^{23}=9.03\times10^{23}$.",
    R(0.5 * 3 * NA))

B.q("c-mol-04", "mole-calculations", 1,
    r"The molar mass of $\mathrm{H_2SO_4}$ is " + masses("H", "S", "O"),
    [r"$98$ g/mol", r"$98$ g", r"$49$ g/mol", r"$96$ g/mol"],
    r"$2\times1+32+4\times16=98$, so $M=98$ g/mol. Molar mass has units of g/mol (not g).",
    Fn(lambda o: "g/mol" in o and abs(first_number(o) - Mr({"H": 2, "S": 1, "O": 4})) < 1e-9, "98 g/mol"))

B.q("c-mol-05", "mole-calculations", 3,
    r"$5.6$ g of iron reacts completely with excess dilute hydrochloric acid ($\mathrm{Fe+2HCl\rightarrow FeCl_2+H_2\uparrow}$). The volume of hydrogen at STP is " + masses("Fe") + r" (molar volume at STP $22.4$ L/mol)",
    [r"$2.24$ L", r"$4.48$ L", r"$1.12$ L", r"$22.4$ L"],
    r"$n(\mathrm{Fe})=\dfrac{5.6}{56}=0.1$ mol, giving $0.1$ mol $\mathrm{H_2}$, i.e. $0.1\times22.4=2.24$ L.",
    R(5.6 / Ar["Fe"] * 1 * VM))

B.q("c-mol-06", "mole-calculations", 2,
    r"$2.3$ g of sodium reacts completely with water ($2\mathrm{Na+2H_2O\rightarrow2NaOH+H_2\uparrow}$). The mass of hydrogen produced is " + masses("Na", "H"),
    [r"$0.1$ g", r"$0.2$ g", r"$0.05$ g", r"$1$ g"],
    r"$n(\mathrm{Na})=0.1$ mol, giving $0.05$ mol $\mathrm{H_2}$, i.e. $0.05\times2=0.1$ g.",
    R(2.3 / Ar["Na"] / 2 * 2 * Ar["H"]))

B.q("c-mol-07", "mole-calculations", 3,
    r"$4$ g of $\mathrm{H_2}$ and $32$ g of $\mathrm{O_2}$ react to form water. The mass of water formed is " + masses("H", "O"),
    [r"$36$ g", r"$18$ g", r"$72$ g", r"$34$ g"],
    r"$n(\mathrm{H_2})=2$ mol, $n(\mathrm{O_2})=1$ mol, exactly the $2:1$ ratio of $2\mathrm{H_2+O_2\rightarrow2H_2O}$. So $2$ mol water $=36$ g (mass is conserved).",
    R(min(4 / 2, 32 / 32 * 2) * 18))

B.q("c-mol-08", "mole-calculations", 3,
    r"$10$ g of $\mathrm{H_2}$ is mixed with $64$ g of $\mathrm{O_2}$ and ignited. The mass of water formed is " + masses("H", "O"),
    [r"$72$ g", r"$74$ g", r"$90$ g", r"$64$ g"],
    r"$n(\mathrm{H_2})=5$ mol, $n(\mathrm{O_2})=2$ mol. $2$ mol $\mathrm{O_2}$ needs only $4$ mol $\mathrm{H_2}$, so $\mathrm{O_2}$ is limiting: $4$ mol water $=72$ g. ($74$ g wrongly assumes everything reacts.)",
    R(min(10 / 2 / 2, 64 / 32) * 2 * 18))

B.q("c-mol-09", "mole-calculations", 2,
    r"Which contains the **largest number of molecules**? " + masses("H", "O", "C", "N"),
    [r"$4$ g of $\mathrm{H_2}$", r"$32$ g of $\mathrm{O_2}$", r"$44$ g of $\mathrm{CO_2}$", r"$28$ g of $\mathrm{N_2}$"],
    r"Compare amounts: $\mathrm{H_2}$: $\dfrac42=2$ mol; $\mathrm{O_2}$, $\mathrm{CO_2}$ and $\mathrm{N_2}$: $1$ mol each. More moles means more molecules.",
    Fn(lambda o: max([(4 / 2, "H_2"), (32 / 32, "O_2"), (44 / 44, "CO_2"), (28 / 28, "N_2")])[1] in o and "4" in o, "max moles"))

B.q("c-mol-10", "mole-calculations", 2,
    r"$1$ mol of a substance has a mass of $44$ g. $0.25$ mol of it has mass",
    [r"$11$ g", r"$44$ g", r"$176$ g", r"$22$ g"],
    r"$m=nM=0.25\times44=11$ g.",
    R(0.25 * 44))

B.q("c-mol-11", "mole-calculations", 3,
    r"$10$ g of $\mathrm{CaCO_3}$ reacts with excess hydrochloric acid ($\mathrm{CaCO_3+2HCl\rightarrow CaCl_2+H_2O+CO_2\uparrow}$). The mass of $\mathrm{CO_2}$ produced is " + masses("Ca", "C", "O"),
    [r"$4.4$ g", r"$2.2$ g", r"$10$ g", r"$8.8$ g"],
    r"$M(\mathrm{CaCO_3})=100$ g/mol, so $n=0.1$ mol, giving $0.1$ mol $\mathrm{CO_2}$ $=4.4$ g.",
    R(10 / Mr({"Ca": 1, "C": 1, "O": 3}) * Mr({"C": 1, "O": 2})))

# --------------------------------------------------------------- gas laws
B.q("c-gas-01", "gas-law", 2,
    r"The volume of $0.5$ mol of $\mathrm{O_2}$ at standard temperature and pressure (STP) is (molar volume $22.4$ L/mol)",
    [r"$11.2$ L", r"$22.4$ L", r"$44.8$ L", r"$16$ L"],
    r"$V=nV_m=0.5\times22.4=11.2$ L.",
    R(0.5 * VM))

B.q("c-gas-02", "gas-law", 2,
    r"At STP, $4.48$ L of $\mathrm{CO_2}$ has a mass of " + masses("C", "O") + r" (molar volume $22.4$ L/mol)",
    [r"$8.8$ g", r"$4.4$ g", r"$17.6$ g", r"$2.2$ g"],
    r"$n=\dfrac{4.48}{22.4}=0.2$ mol; $m=0.2\times44=8.8$ g.",
    R(4.48 / VM * Mr({"C": 1, "O": 2})))

B.q("c-gas-03", "gas-law", 2,
    r"At the same temperature and pressure, equal volumes of $\mathrm{H_2}$ and $\mathrm{O_2}$ have",
    [r"the same number of molecules", r"the same mass", r"the same density", r"the same number of atoms and different numbers of molecules"],
    r"Avogadro's law: equal volumes of gases at the same $T$ and $p$ contain equal numbers of molecules. Their masses differ ($\mathrm{O_2}$ is $16$ times heavier).")

B.q("c-gas-04", "gas-law", 3,
    r"The density of a gas at STP is $1.25$ g/L. Its molar mass is (molar volume $22.4$ L/mol)",
    [r"$28$ g/mol", r"$17.9$ g/mol", r"$1.25$ g/mol", r"$56$ g/mol"],
    r"$M=\rho V_m=1.25\times22.4=28$ g/mol (for example $\mathrm{N_2}$ or $\mathrm{CO}$).",
    R(1.25 * VM))

B.q("c-gas-05", "gas-law", 2,
    r"At the same temperature and pressure, the ratio of the densities of $\mathrm{SO_2}$ and $\mathrm{O_2}$ is " + masses("S", "O"),
    [r"$2:1$", r"$1:2$", r"$1:1$", r"$4:1$"],
    r"At equal $T$ and $p$, density is proportional to molar mass: $64:32=2:1$.",
    T(f"{int(Mr({'S': 1, 'O': 2}) / Mr({'O': 2}))}:1"))

B.q("c-gas-06", "gas-law", 3,
    r"A gas mixture at STP contains $0.2$ mol $\mathrm{N_2}$ and $0.3$ mol $\mathrm{O_2}$. Its total volume is (molar volume $22.4$ L/mol)",
    [r"$11.2$ L", r"$22.4$ L", r"$4.48$ L", r"$6.72$ L"],
    r"The molar volume applies to the total amount of gas, whatever the mixture: $(0.2+0.3)\times22.4=11.2$ L.",
    R((0.2 + 0.3) * VM))

B.q("c-gas-07", "gas-law", 2,
    r"Using $pV=nRT$ with $R=8.31\ \text{J/(mol}\cdot\text{K)}$, the pressure of $1$ mol of gas in $0.0249\ \text{m}^3$ at $300$ K is about",
    [r"$1.0\times10^{5}$ Pa", r"$1.0\times10^{3}$ Pa", r"$2.5\times10^{5}$ Pa", r"$1.0\times10^{7}$ Pa"],
    r"$p=\dfrac{nRT}{V}=\dfrac{1\times8.31\times300}{0.0249}\approx1.0\times10^5$ Pa — about atmospheric pressure.",
    R(1 * 8.31 * 300 / 0.0249))

B.q("c-gas-08", "gas-law", 1,
    r"Which statement about the molar volume of a gas is correct?",
    [r"At STP it is about $22.4$ L/mol for any gas", r"It is always $22.4$ L/mol", r"It applies to liquids at STP", r"It depends on which gas it is, at the same conditions"],
    r"The molar volume depends on temperature and pressure, and is about $22.4$ L/mol only at STP ($0^\circ$C, $101$ kPa). It applies to gases only (not to water at STP, for example).")
