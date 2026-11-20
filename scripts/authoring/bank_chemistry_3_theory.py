import math

from qb import *  # noqa: F403

TH = Bank("chemistry", "theories-laws")
EX = Bank("chemistry", "experiments")

# ------------------------------------------------ atomic structure & periodic law
TH.q("c-atom-01", "atomic-periodic", 2,
    r"The atom $^{37}_{17}\mathrm{Cl}$ contains",
    [r"$17$ protons, $20$ neutrons, $17$ electrons", r"$17$ protons, $37$ neutrons, $17$ electrons", r"$20$ protons, $17$ neutrons, $20$ electrons", r"$37$ protons, $17$ neutrons, $37$ electrons"],
    r"Proton number $Z=17$ (also the electron number in a neutral atom); neutrons $=A-Z=37-17=20$.",
    Nums(17, 37 - 17, 17))

TH.q("c-atom-02", "atomic-periodic", 1,
    r"$^{12}\mathrm{C}$ and $^{14}\mathrm{C}$ are",
    [r"isotopes", r"allotropes", r"isomers", r"different elements"],
    r"Same proton number ($6$), different neutron numbers ($6$ and $8$): isotopes of carbon. They have the same chemical properties.")

TH.q("c-atom-03", "atomic-periodic", 2,
    r"An element has electron arrangement $2,8,6$. Its position in the periodic table is",
    [r"Period 3, Group VIA", r"Period 6, Group IIIA", r"Period 3, Group VIIIA", r"Period 2, Group VIA"],
    r"Three electron shells → Period 3; six outer electrons → Group VIA. The element is sulfur ($Z=16$).")

TH.q("c-atom-04", "atomic-periodic", 2,
    r"Across Period 3 from Na to Cl, which property **decreases**?",
    [r"Atomic radius", r"Non-metallic character", r"Electronegativity", r"Number of outer electrons"],
    r"Nuclear charge increases while the number of shells stays $3$, so electrons are pulled closer: the radius decreases. Electronegativity, non-metallic character and outer-electron count increase.")

TH.q("c-atom-05", "atomic-periodic", 2,
    r"Which hydroxide is the strongest base?",
    [r"$\mathrm{KOH}$", r"$\mathrm{NaOH}$", r"$\mathrm{Mg(OH)_2}$", r"$\mathrm{Al(OH)_3}$"],
    r"Metallic character increases down a group and decreases across a period, so K is the most metallic of K, Na, Mg, Al and KOH is the strongest base.")

TH.q("c-atom-06", "atomic-periodic", 2,
    r"Which acid is the strongest?",
    [r"$\mathrm{HClO_4}$", r"$\mathrm{H_2SO_4}$", r"$\mathrm{H_3PO_4}$", r"$\mathrm{H_2SiO_3}$"],
    r"The acidity of the highest oxyacids rises with non-metallic character across Period 3: Si < P < S < Cl. Perchloric acid is the strongest.")

TH.q("c-atom-07", "atomic-periodic", 1,
    r"The number of electrons in $\mathrm{Mg^{2+}}$ is ($Z(\mathrm{Mg})=12$)",
    [r"$10$", r"$12$", r"$14$", r"$2$"],
    r"Mg loses $2$ electrons to form $\mathrm{Mg^{2+}}$: $12-2=10$ electrons (the same as Ne).",
    N(12 - 2))

TH.q("c-atom-08", "atomic-periodic", 3,
    r"Chlorine has two isotopes, $^{35}\mathrm{Cl}$ and $^{37}\mathrm{Cl}$, and its relative atomic mass is $35.5$. The percentage abundance of $^{35}\mathrm{Cl}$ is",
    [r"$75\%$", r"$50\%$", r"$25\%$", r"$66.7\%$"],
    r"Let the fraction of $^{35}\mathrm{Cl}$ be $x$: $35x+37(1-x)=35.5\Rightarrow2x=1.5\Rightarrow x=0.75$, i.e. $75\%$.",
    R(100 * sp.solve(35 * x + 37 * (1 - x) - sp.Rational(71, 2), x)[0]))

TH.q("c-atom-09", "atomic-periodic", 1,
    r"The elements in the same **group** of the main groups have the same",
    [r"number of outer-shell electrons", r"number of electron shells", r"atomic radius", r"relative atomic mass"],
    r"Main-group elements in one group share the same number of valence (outer) electrons, which explains their similar chemistry. Elements in the same **period** have the same number of shells.")

TH.q("c-atom-10", "atomic-periodic", 2,
    r"Which halogen is the most reactive non-metal?",
    [r"$\mathrm{F_2}$", r"$\mathrm{Cl_2}$", r"$\mathrm{Br_2}$", r"$\mathrm{I_2}$"],
    r"Down Group VIIA the atoms grow larger and attract electrons less strongly, so reactivity decreases: F > Cl > Br > I. Fluorine is the most reactive non-metal.")

TH.q("c-atom-11", "atomic-periodic", 3,
    r"$\mathrm{X^{2-}}$ has $18$ electrons and its nucleus contains $16$ neutrons. The mass number of X is",
    [r"$32$", r"$34$", r"$36$", r"$30$"],
    r"$\mathrm{X^{2-}}$ has gained $2$ electrons, so the neutral atom has $16$ electrons and $Z=16$. $A=Z+N=16+16=32$ (it is $^{32}\mathrm S$).",
    N((18 - 2) + 16))

# --------------------------------------------- chemical bonds & intermolecular forces
TH.q("c-bond-01", "bonding", 1,
    r"Which compound contains **ionic** bonds?",
    [r"$\mathrm{NaCl}$", r"$\mathrm{HCl}$", r"$\mathrm{CO_2}$", r"$\mathrm{CH_4}$"],
    r"Sodium (an active metal) transfers an electron to chlorine, forming $\mathrm{Na^+}$ and $\mathrm{Cl^-}$ held by an ionic bond. The others are molecules with covalent bonds between non-metals.")

TH.q("c-bond-02", "bonding", 2,
    r"Which molecule is **non-polar** although it contains polar bonds?",
    [r"$\mathrm{CO_2}$", r"$\mathrm{H_2O}$", r"$\mathrm{NH_3}$", r"$\mathrm{HCl}$"],
    r"$\mathrm{CO_2}$ is linear ($\mathrm{O=C=O}$), so its two bond dipoles cancel. $\mathrm{H_2O}$ (bent) and $\mathrm{NH_3}$ (pyramidal) are polar, and HCl has a single polar bond.")

TH.q("c-bond-03", "bonding", 2,
    r"Water has an unusually high boiling point compared with $\mathrm{H_2S}$ mainly because",
    [r"hydrogen bonds form between water molecules", r"the O–H bond is stronger than the S–H bond", r"water molecules are heavier", r"water is an ionic compound"],
    r"Boiling separates molecules, so it depends on intermolecular forces, not on the bonds inside a molecule. Water molecules hydrogen-bond strongly to each other; $\mathrm{H_2S}$ molecules cannot.")

TH.q("c-bond-04", "bonding", 2,
    r"The number of shared electron pairs in a nitrogen molecule, $\mathrm{N\equiv N}$, is",
    [r"$3$", r"$1$", r"$2$", r"$6$"],
    r"Each N has $5$ outer electrons and needs $3$ more for an octet, so the atoms share $3$ pairs: a triple bond (one $\sigma$ and two $\pi$ bonds).",
    N(8 - 5))

TH.q("c-bond-05", "bonding", 2,
    r"Which substance contains **both** ionic and covalent bonds?",
    [r"$\mathrm{NaOH}$", r"$\mathrm{NaCl}$", r"$\mathrm{H_2O}$", r"$\mathrm{MgCl_2}$"],
    r"$\mathrm{NaOH}$ consists of $\mathrm{Na^+}$ and $\mathrm{OH^-}$ (ionic bond), and the O–H bond inside the hydroxide ion is covalent. NaCl and $\mathrm{MgCl_2}$ are purely ionic; water is purely covalent.")

TH.q("c-bond-06", "bonding", 2,
    r"Which substance is a covalent network (atomic) crystal with a very high melting point?",
    [r"Diamond", r"Dry ice ($\mathrm{CO_2}$)", r"Iodine", r"Sodium chloride"],
    r"In diamond every carbon is covalently bonded to four others in a giant 3D network. Dry ice and iodine are molecular crystals (weak forces, low melting points); NaCl is ionic.")

TH.q("c-bond-07", "bonding", 3,
    r"The boiling points of the halogens increase from $\mathrm{F_2}$ to $\mathrm{I_2}$ because",
    [r"van der Waals forces increase with molecular size", r"the covalent bond inside the molecule gets stronger", r"hydrogen bonding increases", r"the molecules become ionic"],
    r"Larger molecules with more electrons have stronger dispersion (van der Waals) forces, so more energy is needed to separate them. The X–X bond actually gets weaker down the group (apart from $\mathrm F_2$).")

TH.q("c-bond-08", "bonding", 1,
    r"Metals conduct electricity well because they contain",
    [r"delocalised (free) electrons", r"free ions", r"many protons", r"hydrogen bonds"],
    r"In metallic bonding, metal cations sit in a sea of delocalised electrons. These electrons can flow when a voltage is applied.")

TH.q("c-bond-09", "bonding", 3,
    r"Which change involves breaking **covalent** bonds?",
    [r"Heating $\mathrm{HI}$ until it decomposes into $\mathrm{H_2}$ and $\mathrm{I_2}$", r"Iodine subliming", r"Melting ice", r"Dissolving sugar in water"],
    r"A chemical change breaks bonds within molecules: H–I bonds break when HI decomposes. Sublimation, melting and dissolving sugar only overcome intermolecular forces.")

# -------------------------------------------------- reaction rate & equilibrium
TH.q("c-eq-01", "rate-equilibrium", 1,
    r"Which change does **not** increase the rate of the reaction of zinc granules with dilute sulfuric acid?",
    [r"Adding water to the acid", r"Using zinc powder instead of granules", r"Warming the acid", r"Using more concentrated acid"],
    r"Adding water dilutes the acid, lowering $[\mathrm{H^+}]$ and the rate. A larger surface area, higher temperature and higher concentration all increase the rate.")

TH.q("c-eq-02", "rate-equilibrium", 2,
    r"In a $2$ L container, the amount of a reactant falls from $1.0$ mol to $0.4$ mol in $10$ s. Its average rate of reaction is",
    [r"$0.03\ \text{mol/(L}\cdot\text{s)}$", r"$0.06\ \text{mol/(L}\cdot\text{s)}$", r"$0.3\ \text{mol/(L}\cdot\text{s)}$", r"$0.6\ \text{mol/(L}\cdot\text{s)}$"],
    r"$\Delta c=\dfrac{1.0-0.4}{2}=0.3$ mol/L, so $v=\dfrac{0.3}{10}=0.03\ \text{mol/(L}\cdot\text{s)}$. Forgetting to divide by the volume gives $0.06$.",
    R((1.0 - 0.4) / 2 / 10))

TH.q("c-eq-03", "rate-equilibrium", 2,
    r"For $\mathrm{N_2(g)+3H_2(g)\rightleftharpoons2NH_3(g)}$, if $v(\mathrm{N_2})=0.1\ \text{mol/(L}\cdot\text{min)}$, then $v(\mathrm{NH_3})=$",
    [r"$0.2\ \text{mol/(L}\cdot\text{min)}$", r"$0.1\ \text{mol/(L}\cdot\text{min)}$", r"$0.3\ \text{mol/(L}\cdot\text{min)}$", r"$0.05\ \text{mol/(L}\cdot\text{min)}$"],
    r"Rates are in the ratio of the coefficients: $v(\mathrm{N_2}):v(\mathrm{NH_3})=1:2$, so $v(\mathrm{NH_3})=0.2\ \text{mol/(L}\cdot\text{min)}$.",
    R(0.1 * 2 / 1))

TH.q("c-eq-04", "rate-equilibrium", 1,
    r"A catalyst speeds up a reaction because it",
    [r"lowers the activation energy", r"increases the enthalpy change", r"shifts the equilibrium towards the products", r"increases the concentration of reactants"],
    r"A catalyst provides a pathway with lower activation energy, so more collisions succeed. It speeds up the forward and reverse reactions equally, so it does not move the equilibrium position.")

TH.q("c-eq-05", "rate-equilibrium", 3,
    r"For $\mathrm{2SO_2(g)+O_2(g)\rightleftharpoons2SO_3(g)}$ ($\Delta H<0$), which change shifts the equilibrium to the right?",
    [r"Increasing the pressure", r"Raising the temperature", r"Adding a catalyst", r"Removing some $\mathrm{O_2}$"],
    r"The forward reaction decreases the number of gas molecules ($3\to2$), so higher pressure favours it (Le Chatelier). It is exothermic, so heating shifts it left. A catalyst has no effect on the position, and removing a reactant shifts it left.")

TH.q("c-eq-06", "rate-equilibrium", 2,
    r"For $\mathrm{H_2(g)+I_2(g)\rightleftharpoons2HI(g)}$ at equilibrium, increasing the pressure by compressing the container",
    [r"does not shift the equilibrium, but the colour darkens", r"shifts the equilibrium to the right", r"shifts the equilibrium to the left", r"makes the colour lighter"],
    r"Both sides have $2$ mol of gas, so pressure does not move the equilibrium. Compression raises the concentration of the violet $\mathrm{I_2}$, so the colour still darkens.")

TH.q("c-eq-07", "rate-equilibrium", 3,
    r"For $\mathrm{N_2(g)+3H_2(g)\rightleftharpoons2NH_3(g)}$, the equilibrium concentrations are $[\mathrm{N_2}]=1$ mol/L, $[\mathrm{H_2}]=2$ mol/L and $[\mathrm{NH_3}]=2$ mol/L. The equilibrium constant $K$ is",
    [r"$0.5$", r"$1$", r"$2$", r"$0.25$"],
    r"$K=\dfrac{[\mathrm{NH_3}]^2}{[\mathrm{N_2}][\mathrm{H_2}]^3}=\dfrac{2^2}{1\times2^3}=\dfrac48=0.5$ (units omitted).",
    N(sp.Rational(2 ** 2, 1 * 2 ** 3)))

TH.q("c-eq-08", "rate-equilibrium", 1,
    r"Which statement about a reaction at chemical equilibrium is correct?",
    [r"The forward and reverse rates are equal and not zero", r"The reaction has stopped", r"The concentrations of reactants and products are equal", r"All the reactants have been used up"],
    r"Equilibrium is dynamic: both reactions continue at equal rates, so concentrations stay **constant** — but not necessarily equal to each other.")

TH.q("c-eq-09", "rate-equilibrium", 3,
    r"$2$ mol $\mathrm{SO_2}$ and $1$ mol $\mathrm{O_2}$ are put in a $1$ L vessel. At equilibrium, $1.6$ mol $\mathrm{SO_3}$ has formed ($\mathrm{2SO_2+O_2\rightleftharpoons2SO_3}$). The conversion (percentage reacted) of $\mathrm{SO_2}$ is",
    [r"$80\%$", r"$40\%$", r"$60\%$", r"$20\%$"],
    r"$1.6$ mol $\mathrm{SO_3}$ formed means $1.6$ mol $\mathrm{SO_2}$ reacted (ratio $2:2$). Conversion $=\dfrac{1.6}{2}=80\%$.",
    R(100 * 1.6 * (2 / 2) / 2))

TH.q("c-eq-10", "rate-equilibrium", 2,
    r"For the endothermic reaction $\mathrm{N_2O_4(g)\rightleftharpoons2NO_2(g)}$ (colourless ⇌ brown), when the mixture is heated",
    [r"the colour darkens", r"the colour fades", r"the colour does not change", r"the gas becomes colourless"],
    r"The forward reaction is endothermic, so heating shifts the equilibrium to the right, producing more brown $\mathrm{NO_2}$.")

TH.q("c-eq-11", "rate-equilibrium", 2,
    r"A reaction rate doubles for every $10^\circ$C rise in temperature. Raising the temperature from $20^\circ$C to $50^\circ$C multiplies the rate by",
    [r"$8$", r"$6$", r"$3$", r"$4$"],
    r"$50-20=30^\circ$C is three $10^\circ$C steps: $2^3=8$.",
    N(2 ** ((50 - 20) // 10)))

# ---------------------------------------------------------- electrolyte solutions
TH.q("c-elec-01", "electrolytes", 1,
    r"Which substance is a **weak** electrolyte?",
    [r"Acetic acid, $\mathrm{CH_3COOH}$", r"Hydrochloric acid", r"Sodium hydroxide", r"Sodium chloride"],
    r"Acetic acid is only partly ionised in water: $\mathrm{CH_3COOH\rightleftharpoons CH_3COO^-+H^+}$. Strong acids, strong bases and most salts ionise completely.")

TH.q("c-elec-02", "electrolytes", 2,
    r"Which substance is a non-electrolyte?",
    [r"Sucrose (table sugar)", r"$\mathrm{KNO_3}$", r"$\mathrm{H_2SO_4}$", r"$\mathrm{NH_3\cdot H_2O}$"],
    r"Sucrose dissolves as whole molecules and does not conduct. $\mathrm{KNO_3}$ and $\mathrm{H_2SO_4}$ are strong electrolytes, and ammonia solution is a weak electrolyte.")

TH.q("c-elec-03", "electrolytes", 2,
    r"An aqueous solution of $\mathrm{Na_2CO_3}$ is",
    [r"alkaline, because $\mathrm{CO_3^{2-}}$ is hydrolysed", r"neutral, because it is a salt", r"acidic, because it contains carbon", r"neutral, because $\mathrm{Na^+}$ is not hydrolysed"],
    r"$\mathrm{CO_3^{2-}+H_2O\rightleftharpoons HCO_3^-+OH^-}$: the salt of a strong base and a weak acid gives an alkaline solution.")

TH.q("c-elec-04", "electrolytes", 3,
    r"The solution of which salt is **acidic**?",
    [r"$\mathrm{NH_4Cl}$", r"$\mathrm{NaCl}$", r"$\mathrm{CH_3COONa}$", r"$\mathrm{K_2SO_4}$"],
    r"$\mathrm{NH_4^++H_2O\rightleftharpoons NH_3\cdot H_2O+H^+}$: the salt of a weak base and a strong acid is acidic. NaCl and $\mathrm{K_2SO_4}$ are neutral; $\mathrm{CH_3COONa}$ is alkaline.")

TH.q("c-elec-05", "electrolytes", 1,
    r"In the copper–zinc galvanic cell with dilute sulfuric acid, the negative electrode is",
    [r"zinc, which is oxidised", r"copper, which is oxidised", r"zinc, which is reduced", r"copper, which is reduced"],
    r"The more reactive metal, zinc, loses electrons ($\mathrm{Zn-2e^-\rightarrow Zn^{2+}}$): it is the negative electrode (anode). Hydrogen is released at the copper surface.")

TH.q("c-elec-06", "electrolytes", 3,
    r"In the electrolysis of $\mathrm{CuCl_2}$ solution with inert electrodes, the product at the **anode** is",
    [r"chlorine gas", r"copper", r"oxygen gas", r"hydrogen gas"],
    r"Anions migrate to the anode and are oxidised: $\mathrm{2Cl^--2e^-\rightarrow Cl_2\uparrow}$. Copper is deposited at the cathode ($\mathrm{Cu^{2+}+2e^-\rightarrow Cu}$).")

TH.q("c-elec-07", "electrolytes", 3,
    r"During electrolysis of $\mathrm{CuSO_4}$ solution, $0.2$ mol of electrons pass through the circuit. The mass of copper deposited at the cathode is (Relative atomic mass: Cu $64$)",
    [r"$6.4$ g", r"$12.8$ g", r"$3.2$ g", r"$64$ g"],
    r"$\mathrm{Cu^{2+}+2e^-\rightarrow Cu}$: $0.2$ mol of electrons deposit $0.1$ mol Cu, i.e. $6.4$ g.",
    R(0.2 / 2 * 64))

TH.q("c-elec-08", "electrolytes", 2,
    r"Diluting a $0.1$ mol/L acetic acid solution tenfold",
    [r"increases its degree of ionisation", r"decreases its degree of ionisation", r"makes it a strong acid", r"increases $[\mathrm{H^+}]$"],
    r"Dilution shifts the ionisation equilibrium to the right (more particles in solution), so the **fraction** ionised increases, although $[\mathrm{H^+}]$ itself decreases.")

TH.q("c-elec-09", "electrolytes", 1,
    r"Iron rusts fastest when it is",
    [r"in contact with moist air and salt water", r"in dry air", r"in boiled, oil-covered water", r"coated with zinc"],
    r"Rusting is electrochemical corrosion and needs water and oxygen; dissolved salt (an electrolyte) speeds it up. A zinc coating protects iron sacrificially.")

# ------------------------------------------------------- lab safety & apparatus
EX.q("c-lab-01", "lab-safety", 1,
    r"When diluting concentrated sulfuric acid, you should",
    [r"slowly pour the acid into water while stirring", r"slowly pour water into the acid", r"pour both quickly into a beaker at the same time", r"dilute it in a measuring cylinder"],
    r"Dilution releases a lot of heat. Adding acid to water (never water to acid) lets the larger volume of water absorb the heat and prevents violent boiling and splashing.")

EX.q("c-lab-02", "lab-safety", 1,
    r"A small alcohol fire on the laboratory bench should be put out by",
    [r"covering it with a damp cloth", r"pouring water on it", r"blowing it out", r"fanning it"],
    r"A damp cloth cuts off the oxygen. Water would spread the burning alcohol (which floats and mixes) and blowing can spread the flames.")

EX.q("c-lab-03", "lab-safety", 2,
    r"Which apparatus can be heated **directly** over a flame?",
    [r"Test tube", r"Beaker", r"Measuring cylinder", r"Volumetric flask"],
    r"Test tubes, evaporating dishes and crucibles may be heated directly. Beakers and flasks need a gauze. Measuring cylinders and volumetric flasks must never be heated, because their volumes would change.")

EX.q("c-lab-04", "lab-safety", 2,
    r"To make exactly $250$ mL of a solution of known concentration, the essential apparatus is a",
    [r"$250$ mL volumetric flask", r"$250$ mL beaker", r"$250$ mL measuring cylinder", r"$250$ mL conical flask"],
    r"A volumetric flask is calibrated to contain one exact volume at its mark. Beakers and conical flasks are only roughly graduated, and a cylinder is not accurate enough for standard solutions.")

EX.q("c-lab-05", "lab-safety", 1,
    r"If concentrated sodium hydroxide solution splashes onto your skin, you should first",
    [r"rinse with plenty of water, then apply dilute boric acid solution", r"apply concentrated sulfuric acid to neutralise it", r"wipe it with a dry cloth and do nothing else", r"cover it with a bandage"],
    r"Wash with lots of water first, then apply a weak acid (boric acid). Never use a strong acid to neutralise on skin — the reaction releases heat and the acid itself burns.")

EX.q("c-lab-06", "lab-safety", 2,
    r"Before igniting hydrogen, you must",
    [r"test its purity", r"dry it with concentrated sulfuric acid", r"mix it with air", r"cool it"],
    r"A mixture of hydrogen and air explodes when ignited. Collecting a small tube and testing it (a quiet “pop” means pure) prevents explosions.")

EX.q("c-lab-07", "lab-safety", 3,
    r"A student reads a measuring cylinder by looking **down** on the meniscus from above. The reading recorded is",
    [r"larger than the true volume", r"smaller than the true volume", r"equal to the true volume", r"always zero"],
    r"Viewed from above, the line of sight meets the scale above the bottom of the meniscus, so the reading is too high. The eye must be level with the bottom of the meniscus.")

EX.q("c-lab-08", "lab-safety", 1,
    r"The correct way to smell a gas in the laboratory is to",
    [r"gently waft the gas towards your nose with your hand", r"put your nose directly over the container", r"breathe in deeply from the tube", r"taste it"],
    r"Wafting a small amount towards the nose avoids inhaling a large dose of a possibly toxic gas.")

# ------------------------------------------------ preparation & identification of gases
EX.q("c-gasp-01", "gas-preparation", 1,
    r"$\mathrm{CO_2}$ is usually prepared in the laboratory from",
    [r"marble (or limestone) and dilute hydrochloric acid", r"marble and dilute sulfuric acid", r"burning charcoal", r"sodium carbonate and concentrated sulfuric acid"],
    r"$\mathrm{CaCO_3+2HCl\rightarrow CaCl_2+H_2O+CO_2\uparrow}$ gives a steady stream. With dilute $\mathrm{H_2SO_4}$, insoluble $\mathrm{CaSO_4}$ coats the marble and stops the reaction.")

EX.q("c-gasp-02", "gas-preparation", 1,
    r"A gas turns limewater milky. The gas is",
    [r"$\mathrm{CO_2}$", r"$\mathrm{O_2}$", r"$\mathrm{H_2}$", r"$\mathrm{N_2}$"],
    r"$\mathrm{CO_2+Ca(OH)_2\rightarrow CaCO_3\downarrow+H_2O}$: the white precipitate makes limewater milky.")

EX.q("c-gasp-03", "gas-preparation", 2,
    r"Ammonia is collected by",
    [r"downward displacement of air (mouth of the tube pointing down)", r"displacement of water", r"upward displacement of air", r"collecting over concentrated sulfuric acid"],
    r"$\mathrm{NH_3}$ is very soluble in water and less dense than air ($M=17<29$), so it is collected in an inverted container by downward displacement of air.")

EX.q("c-gasp-04", "gas-preparation", 2,
    r"Which drying agent is suitable for ammonia?",
    [r"Soda lime (CaO + NaOH)", r"Concentrated sulfuric acid", r"Anhydrous $\mathrm{CaCl_2}$", r"Phosphorus pentoxide"],
    r"Ammonia is basic, so it reacts with acidic drying agents ($\mathrm{H_2SO_4}$, $\mathrm{P_2O_5}$) and forms a complex with $\mathrm{CaCl_2}$. A basic drying agent such as soda lime is used.")

EX.q("c-gasp-05", "gas-preparation", 1,
    r"A glowing splint relights in a gas. The gas is",
    [r"oxygen", r"carbon dioxide", r"hydrogen", r"nitrogen"],
    r"Oxygen supports combustion strongly, so it relights a glowing splint. Hydrogen gives a squeaky pop with a lit splint.")

EX.q("c-gasp-06", "gas-preparation", 3,
    r"Chlorine prepared from $\mathrm{MnO_2}$ and concentrated HCl contains HCl and water vapour. The correct order of purification is to pass it through",
    [r"saturated NaCl solution, then concentrated $\mathrm{H_2SO_4}$", r"concentrated $\mathrm{H_2SO_4}$, then saturated NaCl solution", r"NaOH solution, then concentrated $\mathrm{H_2SO_4}$", r"water, then soda lime"],
    r"Saturated brine absorbs HCl but very little $\mathrm{Cl_2}$. Drying comes **last**, otherwise water vapour would be picked up again. NaOH and soda lime would absorb the chlorine itself.")

EX.q("c-gasp-07", "gas-preparation", 2,
    r"Which gas can be collected by displacement of water?",
    [r"$\mathrm{O_2}$", r"$\mathrm{NH_3}$", r"$\mathrm{HCl}$", r"$\mathrm{NO_2}$"],
    r"Oxygen is only slightly soluble and does not react with water. $\mathrm{NH_3}$ and HCl are extremely soluble, and $\mathrm{NO_2}$ reacts with water.")

EX.q("c-gasp-08", "gas-preparation", 2,
    r"In the laboratory, oxygen can be prepared by heating potassium permanganate. Which statement is correct?",
    [r"$\mathrm{2KMnO_4\xrightarrow{\Delta}K_2MnO_4+MnO_2+O_2\uparrow}$", r"It needs $\mathrm{MnO_2}$ as a catalyst", r"The products are KCl and $\mathrm{O_2}$", r"It must be done in aqueous solution"],
    r"Potassium permanganate decomposes on heating, without a catalyst, into potassium manganate, manganese dioxide and oxygen. KCl comes from $\mathrm{KClO_3}$.")

# ---------------------------------------------------- separation & purification
EX.q("c-sep-01", "separation", 1,
    r"To separate sand from salt water, the best method is",
    [r"filtration", r"distillation", r"crystallisation", r"chromatography"],
    r"Sand is an insoluble solid; filtration traps it on the filter paper while the solution passes through. (Evaporating the filtrate would then recover the salt.)")

EX.q("c-sep-02", "separation", 1,
    r"To obtain pure water from sea water, use",
    [r"distillation", r"filtration", r"evaporation", r"decanting"],
    r"Distillation boils off the water and condenses it, leaving the dissolved salts behind. Filtration cannot remove dissolved substances.")

EX.q("c-sep-03", "separation", 2,
    r"To extract iodine from iodine water, a suitable solvent is",
    [r"$\mathrm{CCl_4}$", r"ethanol", r"acetic acid", r"sodium chloride solution"],
    r"An extraction solvent must be immiscible with water and dissolve iodine much better than water. $\mathrm{CCl_4}$ fits; ethanol and acetic acid mix with water.")

EX.q("c-sep-04", "separation", 2,
    r"In a distillation, the bulb of the thermometer should be placed",
    [r"at the side arm (outlet) of the distillation flask", r"in the liquid", r"at the end of the condenser", r"at the top of the condenser"],
    r"The thermometer measures the temperature of the vapour leaving the flask, so the bulb sits level with the side arm.")

EX.q("c-sep-05", "separation", 3,
    r"$\mathrm{KNO_3}$ contains a small amount of NaCl. The best way to purify $\mathrm{KNO_3}$ is",
    [r"dissolve in hot water, cool to crystallise, then filter", r"dissolve and evaporate to dryness", r"dissolve and filter", r"distil the solution"],
    r"$\mathrm{KNO_3}$ is much more soluble hot than cold, while NaCl's solubility barely changes. On cooling, $\mathrm{KNO_3}$ crystallises out and NaCl stays in solution.")

EX.q("c-sep-06", "separation", 2,
    r"To remove a small amount of $\mathrm{CO_2}$ from CO gas, pass the mixture through",
    [r"NaOH solution", r"concentrated sulfuric acid", r"water", r"hot copper(II) oxide"],
    r"$\mathrm{CO_2+2NaOH\rightarrow Na_2CO_3+H_2O}$ while CO does not react. Hot CuO would destroy the CO itself ($\mathrm{CO+CuO\rightarrow Cu+CO_2}$).")

EX.q("c-sep-07", "separation", 3,
    r"To remove $\mathrm{Na_2SO_4}$ from NaCl solution, add",
    [r"a suitable amount of $\mathrm{BaCl_2}$ solution, then filter", r"$\mathrm{Ba(NO_3)_2}$ solution, then filter", r"$\mathrm{AgNO_3}$ solution, then filter", r"NaOH solution"],
    r"$\mathrm{Ba^{2+}+SO_4^{2-}\rightarrow BaSO_4\downarrow}$. Using $\mathrm{BaCl_2}$ leaves only NaCl behind; $\mathrm{Ba(NO_3)_2}$ would introduce $\mathrm{NO_3^-}$ as a new impurity, and $\mathrm{AgNO_3}$ would remove the chloride.")

EX.q("c-sep-08", "separation", 1,
    r"Two immiscible liquids such as oil and water are separated with a",
    [r"separating funnel", r"filter funnel", r"condenser", r"burette"],
    r"In a separating funnel the denser layer is run off through the tap at the bottom and the upper layer is poured out from the top.")

# ------------------------------------------------------------ industrial processes
EX.q("c-ind-01", "industrial", 1,
    r"In the industrial synthesis of ammonia, $\mathrm{N_2+3H_2\rightleftharpoons2NH_3}$, the catalyst used is",
    [r"iron", r"platinum", r"vanadium(V) oxide", r"nickel"],
    r"The Haber process uses an iron-based catalyst at about $400$–$500^\circ$C and $10$–$30$ MPa. $\mathrm{V_2O_5}$ is the catalyst for the contact process (sulfuric acid).")

EX.q("c-ind-02", "industrial", 2,
    r"The synthesis of ammonia is exothermic, yet industry operates at about $400$–$500^\circ$C because",
    [r"the rate would be too slow at low temperature and the catalyst works best there", r"high temperature increases the equilibrium yield", r"ammonia decomposes below $400^\circ$C", r"nitrogen does not exist below $400^\circ$C"],
    r"Lower temperature would give a higher equilibrium yield but far too slow a rate. $400$–$500^\circ$C is a compromise between rate and yield, and it is the iron catalyst's working temperature.")

EX.q("c-ind-03", "industrial", 2,
    r"In the ammonia plant, unreacted $\mathrm{N_2}$ and $\mathrm{H_2}$ are",
    [r"recycled back into the reactor", r"released into the air", r"burned as fuel", r"dissolved in water"],
    r"The conversion per pass is only about $15$–$25\%$, so after ammonia is condensed out, the unreacted gases are recycled. This raises the overall yield.")

EX.q("c-ind-04", "industrial", 2,
    r"In the contact process for sulfuric acid, $\mathrm{SO_3}$ is absorbed in",
    [r"$98\%$ concentrated sulfuric acid", r"water", r"dilute sulfuric acid", r"NaOH solution"],
    r"Absorbing $\mathrm{SO_3}$ directly in water produces an acid mist that is hard to collect. It is absorbed in $98\%$ sulfuric acid instead, and then diluted.")

EX.q("c-ind-05", "industrial", 1,
    r"The chlor-alkali industry electrolyses",
    [r"saturated sodium chloride solution", r"molten sodium chloride", r"sea water without purification", r"sodium hydroxide solution"],
    r"$\mathrm{2NaCl+2H_2O\xrightarrow{electrolysis}2NaOH+H_2\uparrow+Cl_2\uparrow}$. Electrolysing molten NaCl instead gives sodium metal and chlorine.")

EX.q("c-ind-06", "industrial", 2,
    r"Aluminium is produced industrially by",
    [r"electrolysis of molten aluminium oxide (with cryolite)", r"reducing $\mathrm{Al_2O_3}$ with carbon", r"electrolysis of $\mathrm{AlCl_3}$ solution", r"heating bauxite in air"],
    r"Aluminium is too reactive to be reduced by carbon, and from aqueous solution water would be reduced instead. Molten $\mathrm{Al_2O_3}$ dissolved in cryolite (which lowers the melting point) is electrolysed.")

EX.q("c-ind-07", "industrial", 1,
    r"In the blast furnace, the main reducing agent that converts iron ore into iron is",
    [r"carbon monoxide", r"carbon dioxide", r"oxygen", r"limestone"],
    r"Coke burns to $\mathrm{CO_2}$, which reacts with more coke to form CO. Then $\mathrm{Fe_2O_3+3CO\rightarrow2Fe+3CO_2}$. Limestone removes impurities as slag.")

EX.q("c-ind-08", "industrial", 3,
    r"An ammonia plant produces $34$ t of $\mathrm{NH_3}$. The minimum mass of $\mathrm{N_2}$ needed is (Relative atomic masses: N $14$, H $1$)",
    [r"$28$ t", r"$14$ t", r"$56$ t", r"$34$ t"],
    r"$\mathrm{N_2+3H_2\rightarrow2NH_3}$: $28$ t of $\mathrm{N_2}$ gives $2\times17=34$ t of $\mathrm{NH_3}$ (all the nitrogen ends up in the ammonia: $34\times\tfrac{14}{17}=28$ t).",
    R(34 / 17 / 2 * 28))
