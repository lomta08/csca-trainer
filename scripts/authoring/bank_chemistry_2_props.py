from qb import *  # noqa: F403

B = Bank("chemistry", "properties-reactions")
Ar = {"H": 1, "C": 12, "N": 14, "O": 16, "Na": 23, "Mg": 24, "Al": 27, "S": 32, "Cl": 35.5, "K": 39, "Ca": 40, "Fe": 56, "Cu": 64, "Zn": 65, "Ag": 108, "Ba": 137}


def Mr(f):
    return sum(Ar[el] * c for el, c in f.items())


def masses(*els):
    return "(Relative atomic masses: " + ", ".join(f"{el} ${Ar[el]:g}$" for el in els) + ")"


# ------------------------------------------------- common inorganic substances
B.q("c-inor-01", "inorganic", 1,
    r"When a small piece of sodium is put into water containing phenolphthalein, which observation is **not** seen?",
    [r"The sodium sinks to the bottom", r"The sodium melts into a ball", r"The solution turns red (pink)", r"The sodium moves around on the surface"],
    r"Sodium is less dense than water, so it **floats**. The reaction $2\mathrm{Na+2H_2O\rightarrow2NaOH+H_2\uparrow}$ is exothermic (it melts into a ball), the gas pushes it around, and NaOH turns phenolphthalein red.")

B.q("c-inor-02", "inorganic", 1,
    r"Which metal is protected from further corrosion in air by a thin, dense oxide layer?",
    [r"Aluminium", r"Iron", r"Sodium", r"Potassium"],
    r"Aluminium forms a compact $\mathrm{Al_2O_3}$ film that stops further oxidation. Rust on iron is loose and porous, and sodium and potassium react rapidly.")

B.q("c-inor-03", "inorganic", 2,
    r"Which substance reacts with **both** dilute hydrochloric acid and sodium hydroxide solution?",
    [r"$\mathrm{Al(OH)_3}$", r"$\mathrm{Fe(OH)_3}$", r"$\mathrm{Mg(OH)_2}$", r"$\mathrm{Cu(OH)_2}$"],
    r"Aluminium hydroxide is **amphoteric**: $\mathrm{Al(OH)_3+3HCl\rightarrow AlCl_3+3H_2O}$ and $\mathrm{Al(OH)_3+NaOH\rightarrow NaAlO_2+2H_2O}$. The other hydroxides react only with acids.")

B.q("c-inor-04", "inorganic", 2,
    r"Chlorine water is used to disinfect. The substance mainly responsible for its bleaching and disinfecting action is",
    [r"$\mathrm{HClO}$", r"$\mathrm{HCl}$", r"$\mathrm{Cl^-}$", r"$\mathrm{H_2O}$"],
    r"$\mathrm{Cl_2+H_2O\rightleftharpoons HCl+HClO}$. Hypochlorous acid $\mathrm{HClO}$ is a strong oxidising agent and is what bleaches and kills bacteria.")

B.q("c-inor-05", "inorganic", 2,
    r"Concentrated sulfuric acid can be used to dry which gas?",
    [r"$\mathrm{CO_2}$", r"$\mathrm{NH_3}$", r"$\mathrm{H_2S}$", r"$\mathrm{HI}$"],
    r"Concentrated $\mathrm{H_2SO_4}$ is acidic and oxidising: it reacts with the base $\mathrm{NH_3}$ and oxidises reducing gases such as $\mathrm{H_2S}$ and $\mathrm{HI}$. It does not react with $\mathrm{CO_2}$.")

B.q("c-inor-06", "inorganic", 1,
    r"The gas that causes acid rain mainly through its oxidation to sulfuric acid is",
    [r"$\mathrm{SO_2}$", r"$\mathrm{CO_2}$", r"$\mathrm{N_2}$", r"$\mathrm{O_2}$"],
    r"$\mathrm{SO_2}$ (from burning sulfur-containing fuels) is oxidised and dissolves to form $\mathrm{H_2SO_4}$. ($\mathrm{NO_x}$ also contribute, forming $\mathrm{HNO_3}$.) $\mathrm{CO_2}$ gives only weakly acidic rain (pH about $5.6$, regarded as normal).")

B.q("c-inor-07", "inorganic", 2,
    r"When copper reacts with **dilute** nitric acid, the gas produced is",
    [r"$\mathrm{NO}$", r"$\mathrm{H_2}$", r"$\mathrm{NO_2}$", r"$\mathrm{N_2}$"],
    r"$3\mathrm{Cu+8HNO_3(dilute)\rightarrow3Cu(NO_3)_2+2NO\uparrow+4H_2O}$. With **concentrated** nitric acid the product is $\mathrm{NO_2}$. Nitric acid never releases $\mathrm{H_2}$ with metals, because the nitrate is the oxidising agent.")

B.q("c-inor-08", "inorganic", 1,
    r"Which substance is used to make optical fibres?",
    [r"$\mathrm{SiO_2}$", r"$\mathrm{Si}$", r"$\mathrm{Na_2SiO_3}$", r"$\mathrm{CaCO_3}$"],
    r"Optical fibres are made from very pure silicon dioxide. Elemental silicon is a semiconductor used in chips and solar cells.")

B.q("c-inor-09", "inorganic", 2,
    r"$\mathrm{Fe^{3+}}$ in solution can be identified by adding",
    [r"KSCN solution, which turns blood red", r"$\mathrm{BaCl_2}$ solution, which gives a white precipitate", r"$\mathrm{AgNO_3}$ solution, which gives a white precipitate", r"starch solution, which turns blue"],
    r"$\mathrm{Fe^{3+}+3SCN^-\rightarrow Fe(SCN)_3}$ (blood red). $\mathrm{BaCl_2}$ tests for sulfate, $\mathrm{AgNO_3}$ for chloride and starch for iodine.")

B.q("c-inor-10", "inorganic", 3,
    r"To change $\mathrm{FeCl_3}$ solution into $\mathrm{FeCl_2}$ solution **without adding new impurities**, add excess",
    [r"iron powder", r"chlorine gas", r"zinc powder", r"copper powder"],
    r"$2\mathrm{FeCl_3+Fe\rightarrow3FeCl_2}$; excess iron can be filtered off. Zinc would add $\mathrm{Zn^{2+}}$, copper would add $\mathrm{Cu^{2+}}$, and chlorine would oxidise $\mathrm{Fe^{2+}}$ back to $\mathrm{Fe^{3+}}$.")

B.q("c-inor-11", "inorganic", 2,
    r"$4.6$ g of sodium burns completely in oxygen to form $\mathrm{Na_2O_2}$. The mass of $\mathrm{Na_2O_2}$ formed is " + masses("Na", "O"),
    [r"$7.8$ g", r"$6.2$ g", r"$15.6$ g", r"$3.9$ g"],
    r"$n(\mathrm{Na})=\dfrac{4.6}{23}=0.2$ mol, giving $0.1$ mol $\mathrm{Na_2O_2}$ ($M=78$ g/mol): $7.8$ g. ($6.2$ g would be $\mathrm{Na_2O}$.)",
    R(4.6 / Ar["Na"] / 2 * Mr({"Na": 2, "O": 2})))

B.q("c-inor-12", "inorganic", 1,
    r"Ammonia gas turns moist red litmus paper",
    [r"blue", r"white", r"colourless", r"it stays red"],
    r"$\mathrm{NH_3+H_2O\rightleftharpoons NH_3\cdot H_2O\rightleftharpoons NH_4^++OH^-}$: the solution is alkaline, so red litmus turns blue. This is the standard test for ammonia.")

# ---------------------------------------------------- basic organic compounds
B.q("c-org-01", "organic", 1,
    r"Which compound can decolourise bromine water by an **addition** reaction?",
    [r"Ethene, $\mathrm{CH_2=CH_2}$", r"Methane, $\mathrm{CH_4}$", r"Benzene, $\mathrm{C_6H_6}$", r"Ethanol, $\mathrm{C_2H_5OH}$"],
    r"The $\mathrm{C=C}$ double bond adds bromine: $\mathrm{CH_2=CH_2+Br_2\rightarrow CH_2BrCH_2Br}$. Methane and ethanol do not react; benzene only extracts bromine (a physical change).")

B.q("c-org-02", "organic", 2,
    r"The number of structural isomers with formula $\mathrm{C_4H_{10}}$ is",
    [r"$2$", r"$1$", r"$3$", r"$4$"],
    r"Butane $\mathrm{CH_3CH_2CH_2CH_3}$ and methylpropane (isobutane) $\mathrm{CH_3CH(CH_3)CH_3}$: two isomers.")

B.q("c-org-03", "organic", 2,
    r"The number of structural isomers with formula $\mathrm{C_5H_{12}}$ is",
    [r"$3$", r"$2$", r"$4$", r"$5$"],
    r"Pentane (straight chain), 2-methylbutane and 2,2-dimethylpropane: three isomers. The longest chain can have $5$, $4$ or $3$ carbons.")

B.q("c-org-04", "organic", 1,
    r"The functional group of ethanol is",
    [r"$-\mathrm{OH}$ (hydroxyl)", r"$-\mathrm{COOH}$ (carboxyl)", r"$-\mathrm{CHO}$ (aldehyde)", r"$\mathrm{C=C}$"],
    r"Ethanol, $\mathrm{CH_3CH_2OH}$, is an alcohol: its functional group is the hydroxyl group $-\mathrm{OH}$. Acetic acid has $-\mathrm{COOH}$ and acetaldehyde $-\mathrm{CHO}$.")

B.q("c-org-05", "organic", 2,
    r"Ethanol and acetic acid are heated with concentrated sulfuric acid. The organic product is",
    [r"ethyl acetate, $\mathrm{CH_3COOCH_2CH_3}$", r"ethene", r"acetaldehyde", r"diethyl ether only"],
    r"Esterification: $\mathrm{CH_3COOH+CH_3CH_2OH\underset{\Delta}{\overset{\text{conc. }H_2SO_4}{\rightleftharpoons}}CH_3COOCH_2CH_3+H_2O}$. Concentrated $\mathrm{H_2SO_4}$ is the catalyst and absorbs water.")

B.q("c-org-06", "organic", 2,
    r"Methane reacts with chlorine in light. This reaction is a",
    [r"substitution reaction", r"addition reaction", r"polymerisation reaction", r"neutralisation reaction"],
    r"A hydrogen atom is replaced by chlorine: $\mathrm{CH_4+Cl_2\xrightarrow{light}CH_3Cl+HCl}$ (and further substitution). Alkanes have no double bonds, so they cannot undergo addition.")

B.q("c-org-07", "organic", 2,
    r"The mass of $\mathrm{CO_2}$ formed when $0.1$ mol of ethanol, $\mathrm{C_2H_5OH}$, burns completely is " + masses("C", "O"),
    [r"$8.8$ g", r"$4.4$ g", r"$13.2$ g", r"$2.2$ g"],
    r"Each ethanol molecule has $2$ C atoms, so $0.1$ mol gives $0.2$ mol $\mathrm{CO_2}$ $=0.2\times44=8.8$ g.",
    R(0.1 * 2 * Mr({"C": 1, "O": 2})))

B.q("c-org-08", "organic", 1,
    r"Which polymer is made by addition polymerisation of ethene?",
    [r"Polyethylene", r"Polyester", r"Protein", r"Starch"],
    r"$n\,\mathrm{CH_2=CH_2}\rightarrow\mathrm{-[CH_2-CH_2]_n-}$ (polyethylene). Polyesters, proteins and starch are condensation polymers.")

B.q("c-org-09", "organic", 3,
    r"Which test distinguishes glucose from sucrose?",
    [r"Heating with fresh $\mathrm{Cu(OH)_2}$ suspension: glucose gives a brick-red precipitate", r"Adding water: only glucose dissolves", r"Burning: only glucose produces $\mathrm{CO_2}$", r"Adding iodine: glucose turns blue"],
    r"Glucose contains an aldehyde group and is a reducing sugar, so it reduces $\mathrm{Cu(OH)_2}$ to red $\mathrm{Cu_2O}$. Sucrose is not reducing. Both dissolve and both burn to $\mathrm{CO_2}$; iodine tests for starch.")

B.q("c-org-10", "organic", 1,
    r"The general formula of the alkanes is",
    [r"$\mathrm{C_nH_{2n+2}}$", r"$\mathrm{C_nH_{2n}}$", r"$\mathrm{C_nH_{2n-2}}$", r"$\mathrm{C_nH_{2n-6}}$"],
    r"Alkanes are saturated chains: $\mathrm{C_nH_{2n+2}}$ (methane $\mathrm{CH_4}$, ethane $\mathrm{C_2H_6}$). $\mathrm{C_nH_{2n}}$ is for alkenes, $\mathrm{C_nH_{2n-2}}$ for alkynes and $\mathrm{C_nH_{2n-6}}$ for the benzene series.")

B.q("c-org-11", "organic", 3,
    r"$1$ mol of a hydrocarbon burns completely to give $3$ mol $\mathrm{CO_2}$ and $3$ mol $\mathrm{H_2O}$. Its molecular formula is",
    [r"$\mathrm{C_3H_6}$", r"$\mathrm{C_3H_8}$", r"$\mathrm{C_3H_3}$", r"$\mathrm{C_6H_6}$"],
    r"Carbon: $3$ mol $\mathrm{CO_2}$ → $3$ C atoms per molecule. Hydrogen: $3$ mol $\mathrm{H_2O}$ contains $6$ mol H → $6$ H atoms. Formula $\mathrm{C_3H_6}$ (propene or cyclopropane).",
    # C atoms = mol CO2 per mol fuel; H atoms = 2 x mol H2O per mol fuel
    T(r"\mathrm{C_%dH_%d}" % (3 // 1, 2 * 3 // 1)))

# ---------------------------------------------------------------- redox
B.q("c-redox-01", "redox", 2,
    r"In $\mathrm{CuO+H_2\xrightarrow{\Delta}Cu+H_2O}$, the reducing agent is",
    [r"$\mathrm{H_2}$", r"$\mathrm{CuO}$", r"$\mathrm{Cu}$", r"$\mathrm{H_2O}$"],
    r"$\mathrm H$ goes from $0$ to $+1$: it loses electrons, is oxidised, and is therefore the reducing agent. $\mathrm{Cu}$ goes from $+2$ to $0$, so $\mathrm{CuO}$ is the oxidising agent.")

B.q("c-redox-02", "redox", 1,
    r"Which reaction is **not** a redox reaction?",
    [r"$\mathrm{CaCO_3\xrightarrow{high\ temp}CaO+CO_2\uparrow}$", r"$\mathrm{Zn+CuSO_4\rightarrow ZnSO_4+Cu}$", r"$\mathrm{2H_2+O_2\rightarrow2H_2O}$", r"$\mathrm{Cl_2+2KI\rightarrow2KCl+I_2}$"],
    r"In the decomposition of $\mathrm{CaCO_3}$ no oxidation state changes (Ca $+2$, C $+4$, O $-2$ throughout). In the other three, an element changes from or to the free state.")

B.q("c-redox-03", "redox", 2,
    r"In $\mathrm{MnO_2+4HCl(conc.)\xrightarrow{\Delta}MnCl_2+Cl_2\uparrow+2H_2O}$, the ratio of HCl acting as reducing agent to HCl acting as acid is",
    [r"$1:1$", r"$1:2$", r"$1:3$", r"$2:1$"],
    r"Of the $4$ HCl, $2$ are oxidised to $\mathrm{Cl_2}$ (reducing agent) and $2$ end up as $\mathrm{Cl^-}$ in $\mathrm{MnCl_2}$ (acting as an acid). Ratio $2:2=1:1$.",
    T(f"{2 // 2}:{(4 - 2) // 2}"))

B.q("c-redox-04", "redox", 2,
    r"In $2\mathrm{Fe^{3+}+Cu\rightarrow2Fe^{2+}+Cu^{2+}}$, the number of moles of electrons transferred when $1$ mol of Cu reacts is",
    [r"$2$ mol", r"$1$ mol", r"$3$ mol", r"$4$ mol"],
    r"Cu goes from $0$ to $+2$, losing $2$ electrons per atom: $2$ mol of electrons for $1$ mol Cu (each $\mathrm{Fe^{3+}}$ gains one).",
    N(1 * (2 - 0)))

B.q("c-redox-05", "redox", 2,
    r"The oxidation state of Cr in $\mathrm{K_2Cr_2O_7}$ is",
    [r"$+6$", r"$+7$", r"$+3$", r"$+12$"],
    r"$2(+1)+2x+7(-2)=0\Rightarrow2x=12\Rightarrow x=+6$.",
    N(sp.solve(2 * 1 + 2 * x + 7 * (-2), x)[0]))

B.q("c-redox-06", "redox", 2,
    r"Given the reactions $\mathrm{2Fe^{3+}+2I^-\rightarrow2Fe^{2+}+I_2}$ and $\mathrm{Cl_2+2Fe^{2+}\rightarrow2Fe^{3+}+2Cl^-}$, the order of oxidising strength is",
    [r"$\mathrm{Cl_2>Fe^{3+}>I_2}$", r"$\mathrm{I_2>Fe^{3+}>Cl_2}$", r"$\mathrm{Fe^{3+}>Cl_2>I_2}$", r"$\mathrm{Cl_2>I_2>Fe^{3+}}$"],
    r"In each reaction the oxidising agent is stronger than the oxidised product: first reaction $\mathrm{Fe^{3+}>I_2}$, second $\mathrm{Cl_2>Fe^{3+}}$. Combined: $\mathrm{Cl_2>Fe^{3+}>I_2}$.")

B.q("c-redox-07", "redox", 1,
    r"In a redox reaction, the oxidising agent",
    [r"gains electrons and is reduced", r"loses electrons and is oxidised", r"gains electrons and is oxidised", r"neither gains nor loses electrons"],
    r"The oxidising agent takes electrons from another species: it gains electrons, its oxidation state falls and it is reduced. (Mnemonic: OIL RIG — oxidation is loss, reduction is gain.)")

B.q("c-redox-08", "redox", 3,
    r"When $3.2$ g of copper reacts completely with concentrated nitric acid ($\mathrm{Cu+4HNO_3\rightarrow Cu(NO_3)_2+2NO_2\uparrow+2H_2O}$), the amount of electrons transferred is " + masses("Cu"),
    [r"$0.1$ mol", r"$0.05$ mol", r"$0.2$ mol", r"$0.4$ mol"],
    r"$n(\mathrm{Cu})=\dfrac{3.2}{64}=0.05$ mol; each Cu loses $2$ electrons, so $0.1$ mol of electrons are transferred (matching $0.1$ mol $\mathrm{NO_2}$, each N gaining one electron).",
    R(3.2 / Ar["Cu"] * 2))

B.q("c-redox-09", "redox", 3,
    r"In $\mathrm{Cl_2+2NaOH\rightarrow NaCl+NaClO+H_2O}$, chlorine",
    [r"is both oxidised and reduced", r"is only oxidised", r"is only reduced", r"is neither oxidised nor reduced"],
    r"One Cl atom goes $0\to-1$ (reduced, in NaCl) and the other $0\to+1$ (oxidised, in NaClO). This is a disproportionation reaction.")

B.q("c-redox-10", "redox", 2,
    r"In $\mathrm{Fe_2O_3+3CO\rightarrow2Fe+3CO_2}$, the element that is oxidised is",
    [r"carbon", r"iron", r"oxygen", r"no element"],
    r"Carbon goes from $+2$ (in CO) to $+4$ (in $\mathrm{CO_2}$), so it is oxidised and CO is the reducing agent. Iron goes from $+3$ to $0$ (reduced).")

# ---------------------------------------------------- ionic reactions & tests
B.q("c-ion-01", "ionic-reactions", 2,
    r"The ionic equation for the neutralisation of hydrochloric acid by sodium hydroxide is",
    [r"$\mathrm{H^++OH^-\rightarrow H_2O}$", r"$\mathrm{HCl+OH^-\rightarrow Cl^-+H_2O}$", r"$\mathrm{Na^++Cl^-\rightarrow NaCl}$", r"$\mathrm{HCl+NaOH\rightarrow NaCl+H_2O}$"],
    r"Strong acids, strong bases and soluble salts are written as ions; the spectator ions $\mathrm{Na^+}$ and $\mathrm{Cl^-}$ cancel, leaving $\mathrm{H^++OH^-\rightarrow H_2O}$.")

B.q("c-ion-02", "ionic-reactions", 2,
    r"Which group of ions can coexist in large amounts in a colourless, strongly acidic solution?",
    [r"$\mathrm{Na^+,\ K^+,\ SO_4^{2-},\ Cl^-}$", r"$\mathrm{Na^+,\ CO_3^{2-},\ Cl^-,\ K^+}$", r"$\mathrm{Cu^{2+},\ SO_4^{2-},\ Cl^-,\ Na^+}$", r"$\mathrm{Ba^{2+},\ SO_4^{2-},\ Na^+,\ Cl^-}$"],
    r"$\mathrm{CO_3^{2-}}$ reacts with $\mathrm{H^+}$ to give $\mathrm{CO_2}$; $\mathrm{Cu^{2+}}$ is blue (not colourless); $\mathrm{Ba^{2+}}$ and $\mathrm{SO_4^{2-}}$ precipitate $\mathrm{BaSO_4}$. Only the first group works.")

B.q("c-ion-03", "ionic-reactions", 1,
    r"To test a solution for $\mathrm{Cl^-}$, add",
    [r"$\mathrm{AgNO_3}$ solution and dilute $\mathrm{HNO_3}$: a white precipitate forms", r"$\mathrm{BaCl_2}$ solution: a white precipitate forms", r"NaOH solution: a blue precipitate forms", r"KSCN solution: the solution turns red"],
    r"$\mathrm{Ag^++Cl^-\rightarrow AgCl\downarrow}$ (white, insoluble in dilute nitric acid). The nitric acid rules out carbonate, which would also precipitate with silver ions.")

B.q("c-ion-04", "ionic-reactions", 2,
    r"To test for $\mathrm{SO_4^{2-}}$ correctly, the usual procedure is",
    [r"add dilute HCl first (no change), then $\mathrm{BaCl_2}$: a white precipitate forms", r"add $\mathrm{BaCl_2}$ only: a white precipitate forms", r"add $\mathrm{AgNO_3}$: a white precipitate forms", r"add NaOH: a gas forms"],
    r"Acidifying with HCl first removes interference from $\mathrm{CO_3^{2-}}$, $\mathrm{SO_3^{2-}}$ and $\mathrm{Ag^+}$. Then $\mathrm{Ba^{2+}+SO_4^{2-}\rightarrow BaSO_4\downarrow}$ (white).")

B.q("c-ion-05", "ionic-reactions", 2,
    r"Which ionic equation is written correctly?",
    [r"$\mathrm{CaCO_3+2H^+\rightarrow Ca^{2+}+H_2O+CO_2\uparrow}$", r"$\mathrm{CO_3^{2-}+2H^+\rightarrow H_2O+CO_2\uparrow}$ for marble and hydrochloric acid", r"$\mathrm{Fe+Fe^{3+}\rightarrow2Fe^{2+}}$", r"$\mathrm{Cu+2H^+\rightarrow Cu^{2+}+H_2\uparrow}$"],
    r"$\mathrm{CaCO_3}$ (marble) is insoluble and must be written as a formula. $\mathrm{Fe+Fe^{3+}}$ is not charge-balanced (it should be $\mathrm{Fe+2Fe^{3+}\rightarrow3Fe^{2+}}$), and copper does not react with dilute non-oxidising acids.")

B.q("c-ion-06", "ionic-reactions", 1,
    r"Adding NaOH solution to a solution containing $\mathrm{Cu^{2+}}$ gives a",
    [r"blue precipitate", r"reddish-brown precipitate", r"white precipitate", r"green solution only"],
    r"$\mathrm{Cu^{2+}+2OH^-\rightarrow Cu(OH)_2\downarrow}$ (blue). $\mathrm{Fe(OH)_3}$ is reddish-brown, and $\mathrm{Mg(OH)_2}$ is white.")

B.q("c-ion-07", "ionic-reactions", 3,
    r"An excess of $\mathrm{BaCl_2}$ solution is added to $100$ mL of $0.1$ mol/L $\mathrm{Na_2SO_4}$. The mass of $\mathrm{BaSO_4}$ precipitate is " + masses("Ba", "S", "O"),
    [r"$2.33$ g", r"$23.3$ g", r"$1.42$ g", r"$0.233$ g"],
    r"$n(\mathrm{SO_4^{2-}})=0.1\times0.1=0.01$ mol, giving $0.01$ mol $\mathrm{BaSO_4}$ ($M=233$ g/mol): $2.33$ g.",
    R(0.1 * 0.1 * Mr({"Ba": 1, "S": 1, "O": 4})))

B.q("c-ion-08", "ionic-reactions", 2,
    r"To test for $\mathrm{NH_4^+}$ in a solution, add NaOH solution, warm, and test the gas with",
    [r"moist red litmus paper, which turns blue", r"limewater, which turns milky", r"a glowing splint, which relights", r"moist blue litmus paper, which turns red"],
    r"$\mathrm{NH_4^++OH^-\xrightarrow{\Delta}NH_3\uparrow+H_2O}$; ammonia is the only common alkaline gas and turns moist red litmus blue.")

B.q("c-ion-09", "ionic-reactions", 3,
    r"Which pair of solutions gives **no** reaction when mixed?",
    [r"$\mathrm{KNO_3}$ and $\mathrm{NaCl}$", r"$\mathrm{AgNO_3}$ and $\mathrm{NaCl}$", r"$\mathrm{Na_2CO_3}$ and $\mathrm{HCl}$", r"$\mathrm{CuSO_4}$ and NaOH"],
    r"An ionic reaction needs a precipitate, a gas or a weak electrolyte (such as water) to form. $\mathrm{KNO_3}$ + NaCl would only give the soluble $\mathrm{KCl}$ and $\mathrm{NaNO_3}$, so nothing happens.")

B.q("c-ion-10", "ionic-reactions", 1,
    r"A flame test on a solution gives a yellow flame. The solution contains",
    [r"$\mathrm{Na^+}$", r"$\mathrm{K^+}$", r"$\mathrm{Cu^{2+}}$", r"$\mathrm{Ca^{2+}}$"],
    r"Sodium gives a persistent yellow flame. Potassium gives lilac (seen through blue cobalt glass), copper blue-green and calcium brick red.")
