from qb import *  # noqa: F403

T_ = Bank("physics", "thermodynamics")
O = Bank("physics", "optics")
M = Bank("physics", "modern-physics")
h = 6.63e-34
c = 3e8
e = 1.6e-19
R_gas = 8.31

# ------------------------------------------------------------ thermodynamics
T_.q("p-thm-01", "thermodynamics", 1,
    r"A gas absorbs $500$ J of heat and does $200$ J of work on its surroundings. The change in its internal energy is",
    [r"$+300$ J", r"$+700$ J", r"$-300$ J", r"$-700$ J"],
    r"First law: $\Delta U=Q+W$, where $W$ is work done **on** the gas. Here $Q=+500$ J and $W=-200$ J, so $\Delta U=+300$ J.",
    R(500 + (-200)))

T_.q("p-thm-02", "thermodynamics", 1,
    r"An ideal gas is kept at constant temperature while its pressure is doubled. Its volume becomes",
    [r"half the original", r"twice the original", r"four times the original", r"unchanged"],
    r"Boyle's law (isothermal): $pV=\text{const}$, so doubling $p$ halves $V$.")

T_.q("p-thm-03", "thermodynamics", 2,
    r"A gas at $27^\circ$C is heated at constant pressure until its volume doubles. Its new temperature is",
    [r"$327^\circ$C", r"$54^\circ$C", r"$600^\circ$C", r"$300^\circ$C"],
    r"Use kelvin: $T_1=300$ K. At constant pressure $\dfrac{V}{T}=$ const, so $T_2=600$ K $=327^\circ$C. (Doubling the Celsius value is the classic mistake.)",
    R(2 * (27 + 273) - 273))

T_.q("p-thm-04", "thermodynamics", 2,
    r"A sealed rigid container of gas at $300$ K and $1.0\times10^5$ Pa is heated to $450$ K. The new pressure is",
    [r"$1.5\times10^{5}$ Pa", r"$0.67\times10^{5}$ Pa", r"$1.0\times10^{5}$ Pa", r"$4.5\times10^{5}$ Pa"],
    r"Constant volume: $\dfrac{p}{T}=$ const, $p_2=1.0\times10^5\times\dfrac{450}{300}=1.5\times10^5$ Pa.",
    R(1.0e5 * 450 / 300))

T_.q("p-thm-05", "thermodynamics", 1,
    r"The absolute temperature of an ideal gas is a measure of",
    [r"the average kinetic energy of its molecules", r"the total potential energy of its molecules", r"the number of molecules", r"the size of the molecules"],
    r"Kinetic theory: the average translational kinetic energy of a molecule is proportional to the absolute temperature, $\bar E_k=\tfrac32kT$.")

T_.q("p-thm-06", "thermodynamics", 2,
    r"Using $R=8.31\ \text{J/(mol}\cdot\text{K)}$, the volume of $2$ mol of an ideal gas at $300$ K and $1.0\times10^5$ Pa is about",
    [r"$0.050\ \text{m}^3$", r"$0.025\ \text{m}^3$", r"$5.0\ \text{m}^3$", r"$0.0050\ \text{m}^3$"],
    r"$pV=nRT\Rightarrow V=\dfrac{2\times8.31\times300}{1.0\times10^5}\approx0.050\ \text{m}^3$ (about $50$ L).",
    R(2 * R_gas * 300 / 1.0e5))

T_.q("p-thm-07", "thermodynamics", 2,
    r"A gas is compressed **adiabatically** (no heat exchange). Its temperature",
    [r"rises", r"falls", r"stays the same", r"first falls then rises"],
    r"Adiabatic: $Q=0$. Compression means work is done on the gas ($W>0$), so $\Delta U=W>0$ and the temperature rises (this is why a bicycle pump gets warm).")

T_.q("p-thm-08", "thermodynamics", 1,
    r"Brownian motion of pollen grains in water shows that",
    [r"water molecules are in constant random motion", r"pollen grains are alive", r"the water is flowing", r"molecules attract each other"],
    r"The grains are jostled unevenly by the random impacts of the (invisible) water molecules. Brownian motion is indirect evidence of molecular motion, not the motion of molecules themselves.")

T_.q("p-thm-09", "thermodynamics", 3,
    r"An ideal gas expands at constant pressure $2\times10^5$ Pa from $0.01\ \text{m}^3$ to $0.03\ \text{m}^3$ and absorbs $1.0\times10^4$ J of heat. The change in internal energy is",
    [r"$6.0\times10^{3}$ J", r"$1.4\times10^{4}$ J", r"$4.0\times10^{3}$ J", r"$1.0\times10^{4}$ J"],
    r"Work done by the gas: $p\Delta V=2\times10^5\times0.02=4.0\times10^3$ J. $\Delta U=Q-W_{\text{by}}=1.0\times10^4-4.0\times10^3=6.0\times10^3$ J.",
    R(1.0e4 - 2e5 * (0.03 - 0.01)))

T_.q("p-thm-10", "thermodynamics", 2,
    r"For a fixed mass of ideal gas, the state changes from $(p_1,V_1,T_1)=(1\times10^5\ \text{Pa},\ 2\ \text{L},\ 300\ \text{K})$ to $p_2=2\times10^5$ Pa and $V_2=3$ L. Then $T_2=$",
    [r"$900$ K", r"$450$ K", r"$600$ K", r"$200$ K"],
    r"$\dfrac{p_1V_1}{T_1}=\dfrac{p_2V_2}{T_2}\Rightarrow T_2=300\times\dfrac{2\times3}{1\times2}=900$ K.",
    R(300 * (2e5 * 3) / (1e5 * 2)))

T_.q("p-thm-11", "thermodynamics", 2,
    r"Which statement agrees with the second law of thermodynamics?",
    [r"Heat cannot flow spontaneously from a colder body to a hotter body", r"Energy can be created in a heat engine", r"A heat engine can convert all absorbed heat into work", r"Internal energy always decreases"],
    r"The second law (Clausius form): heat does not flow by itself from cold to hot. A consequence is that no heat engine can be 100% efficient. Energy creation would violate the first law.")

T_.q("p-thm-12", "thermodynamics", 1,
    r"$-23^\circ$C on the thermodynamic (Kelvin) scale is",
    [r"$250$ K", r"$296$ K", r"$-250$ K", r"$23$ K"],
    r"$T=t+273=-23+273=250$ K. Kelvin temperatures are never negative.",
    R(-23 + 273))

# ------------------------------------------------------------ optics
O.q("p-opt-01", "reflection-refraction", 1,
    r"A light ray strikes a plane mirror at an angle of incidence of $30^\circ$. The angle between the incident ray and the reflected ray is",
    [r"$60^\circ$", r"$30^\circ$", r"$120^\circ$", r"$90^\circ$"],
    r"Angle of reflection $=$ angle of incidence $=30^\circ$ (both measured from the normal), so the rays are $30^\circ+30^\circ=60^\circ$ apart.",
    R(2 * 30))

O.q("p-opt-02", "reflection-refraction", 1,
    r"Light travels from air into glass of refractive index $1.5$ ($c=3\times10^8$ m/s). Its speed in the glass is",
    [r"$2\times10^{8}$ m/s", r"$4.5\times10^{8}$ m/s", r"$3\times10^{8}$ m/s", r"$1.5\times10^{8}$ m/s"],
    r"$v=\dfrac cn=\dfrac{3\times10^8}{1.5}=2\times10^8$ m/s.",
    R(c / 1.5))

O.q("p-opt-03", "reflection-refraction", 2,
    r"Light passes from air into water at an angle of incidence of $53^\circ$ and the angle of refraction is $37^\circ$ ($\sin53^\circ=0.8$, $\sin37^\circ=0.6$). The refractive index of water is",
    [r"$\dfrac43$", r"$\dfrac34$", r"$1.43$", r"$\dfrac53$"],
    r"Snell's law: $n=\dfrac{\sin i}{\sin r}=\dfrac{0.8}{0.6}=\dfrac43$.",
    N(sp.Rational(8, 10) / sp.Rational(6, 10)))

O.q("p-opt-04", "reflection-refraction", 2,
    r"The critical angle for light going from glass ($n=\sqrt2$) into air is",
    [r"$45^\circ$", r"$30^\circ$", r"$60^\circ$", r"$90^\circ$"],
    r"$\sin C=\dfrac1n=\dfrac1{\sqrt2}$, so $C=45^\circ$.",
    R(sp.asin(1 / sp.sqrt(2)) * 180 / sp.pi))

O.q("p-opt-05", "reflection-refraction", 1,
    r"Total internal reflection can happen only when light travels",
    [r"from an optically denser medium to a less dense one, at an angle of incidence at least the critical angle", r"from air into glass", r"along the normal", r"from a less dense medium into a denser one"],
    r"Both conditions are needed: denser → less dense (e.g. glass → air), and incidence angle $\ge$ the critical angle. Optical fibres use this.")

O.q("p-opt-06", "reflection-refraction", 2,
    r"When light passes from air into glass, which quantity does **not** change?",
    [r"Frequency", r"Speed", r"Wavelength", r"Direction (for oblique incidence)"],
    r"The frequency is fixed by the source. The speed drops to $c/n$, so the wavelength shortens ($\lambda=v/f$), and an oblique ray bends toward the normal.")

O.q("p-opt-07", "reflection-refraction", 3,
    r"A coin lies at the bottom of a pool $2$ m deep. Seen from directly above, with water's refractive index $\tfrac43$, the coin appears to be at a depth of about",
    [r"$1.5$ m", r"$2.67$ m", r"$2$ m", r"$1$ m"],
    r"For near-normal viewing, apparent depth $=\dfrac{\text{real depth}}{n}=\dfrac{2}{4/3}=1.5$ m. Pools look shallower than they are.",
    R(2 / sp.Rational(4, 3)))

O.q("p-opt-08", "reflection-refraction", 1,
    r"White light passing through a prism splits into colours. Violet light is deviated the most because",
    [r"glass has a larger refractive index for violet light", r"violet light has the longest wavelength", r"violet light travels fastest in glass", r"violet light is reflected inside the prism"],
    r"Dispersion: the refractive index of glass increases with frequency, so violet (highest frequency, shortest wavelength) bends most and travels slowest in glass.")

O.q("p-opt-09", "reflection-refraction", 2,
    r"A ray enters a glass block ($n=\sqrt3$) from air with an angle of incidence of $60^\circ$. The angle of refraction is",
    [r"$30^\circ$", r"$45^\circ$", r"$60^\circ$", r"$35^\circ$"],
    r"$\sin r=\dfrac{\sin60^\circ}{\sqrt3}=\dfrac{\sqrt3/2}{\sqrt3}=\dfrac12$, so $r=30^\circ$.",
    R(sp.asin(sp.sin(sp.pi / 3) / sp.sqrt(3)) * 180 / sp.pi))

O.q("p-opt-10", "reflection-refraction", 1,
    r"A person stands $2$ m in front of a plane mirror. The distance between the person and their image is",
    [r"$4$ m", r"$2$ m", r"$1$ m", r"$8$ m"],
    r"A plane mirror forms a virtual image as far behind the mirror as the object is in front: $2+2=4$ m.",
    R(2 * 2))

O.q("p-int-01", "interference-diffraction", 1,
    r"In Young's double-slit experiment, the fringe spacing is $\Delta x=\dfrac{L}{d}\lambda$. If the slit separation $d$ is doubled, the fringe spacing",
    [r"halves", r"doubles", r"stays the same", r"becomes four times as large"],
    r"$\Delta x\propto\dfrac1d$, so doubling $d$ halves the spacing.")

O.q("p-int-02", "interference-diffraction", 2,
    r"In a double-slit experiment, $d=0.5$ mm, $L=1$ m and $\lambda=600$ nm. The fringe spacing is",
    [r"$1.2$ mm", r"$0.3$ mm", r"$12$ mm", r"$0.12$ mm"],
    r"$\Delta x=\dfrac{L\lambda}{d}=\dfrac{1\times600\times10^{-9}}{0.5\times10^{-3}}=1.2\times10^{-3}$ m $=1.2$ mm.",
    R(1 * 600e-9 / 0.5e-3 * 1000))

O.q("p-int-03", "interference-diffraction", 2,
    r"In a double-slit experiment, red light is replaced by blue light with everything else unchanged. The fringes",
    [r"become closer together", r"become farther apart", r"do not change", r"disappear"],
    r"Blue light has a shorter wavelength, and $\Delta x=\dfrac Ld\lambda$, so the fringe spacing decreases.")

O.q("p-int-04", "interference-diffraction", 2,
    r"At a point on the screen of a double-slit experiment, the path difference from the two slits is $1.5\lambda$. The point is",
    [r"a dark fringe", r"a bright fringe", r"the central bright fringe", r"half bright"],
    r"Bright where the path difference is a whole number of wavelengths ($n\lambda$); dark where it is an odd number of half-wavelengths: $1.5\lambda=3\cdot\tfrac\lambda2$, so dark.")

O.q("p-int-05", "interference-diffraction", 1,
    r"The colours seen on a soap bubble are caused by",
    [r"thin-film interference", r"diffraction", r"dispersion by refraction", r"polarisation"],
    r"Light reflected from the front and back surfaces of the thin film interferes; different thicknesses reinforce different wavelengths, giving colours.")

O.q("p-int-06", "interference-diffraction", 2,
    r"Diffraction of light is most noticeable when",
    [r"the size of the opening is comparable to the wavelength", r"the opening is much larger than the wavelength", r"the light is very bright", r"the light is white"],
    r"Obvious diffraction requires an obstacle or slit with size close to (or smaller than) the wavelength. Light's wavelength is tiny, so we usually do not notice light diffracting.")

O.q("p-int-07", "interference-diffraction", 1,
    r"Interference and diffraction of light show that light",
    [r"behaves as a wave", r"consists of particles only", r"travels only in straight lines", r"has no energy"],
    r"Interference and diffraction are characteristic wave phenomena. (The photoelectric effect shows the particle side of light.)")

O.q("p-int-08", "interference-diffraction", 3,
    r"In a double-slit experiment, the distance between the $1$st and the $5$th bright fringes on the same side is $6.0$ mm. The fringe spacing is",
    [r"$1.5$ mm", r"$1.2$ mm", r"$6.0$ mm", r"$3.0$ mm"],
    r"Between the 1st and 5th bright fringes there are $5-1=4$ spacings: $\Delta x=\dfrac{6.0}{4}=1.5$ mm. (Dividing by $5$ is the usual slip.)",
    R(6.0 / (5 - 1)))

O.q("p-int-09", "interference-diffraction", 2,
    r"For interference fringes to be stable, the two light sources must",
    [r"be coherent: same frequency and constant phase difference", r"have the same brightness only", r"be white light", r"be placed far apart"],
    r"Only coherent sources (same frequency, fixed phase relationship) give a stable pattern. That is why Young split one source into two slits.")

# ------------------------------------------------------------ modern physics
M.q("p-pe-01", "photoelectric", 1,
    r"The energy of a photon of frequency $5\times10^{14}$ Hz is ($h=6.63\times10^{-34}\ \text{J}\cdot\text{s}$)",
    [r"$3.3\times10^{-19}$ J", r"$1.3\times10^{-48}$ J", r"$7.5\times10^{47}$ J", r"$3.3\times10^{-20}$ J"],
    r"$E=h\nu=6.63\times10^{-34}\times5\times10^{14}\approx3.3\times10^{-19}$ J.",
    R(h * 5e14))

M.q("p-pe-02", "photoelectric", 2,
    r"A metal has work function $2.0$ eV. Light with photons of energy $3.5$ eV falls on it. The maximum kinetic energy of the photoelectrons is",
    [r"$1.5$ eV", r"$5.5$ eV", r"$2.0$ eV", r"$3.5$ eV"],
    r"Einstein's equation: $E_{k\max}=h\nu-W_0=3.5-2.0=1.5$ eV.",
    R(3.5 - 2.0))

M.q("p-pe-03", "photoelectric", 2,
    r"Increasing the **intensity** of light (above the threshold frequency) falling on a metal increases",
    [r"the number of photoelectrons emitted per second", r"the maximum kinetic energy of the photoelectrons", r"the threshold frequency", r"the work function"],
    r"More intense light means more photons per second, hence more electrons. Each photon's energy $h\nu$ is unchanged, so the maximum kinetic energy is unchanged.")

M.q("p-pe-04", "photoelectric", 2,
    r"The threshold frequency of a metal is $6\times10^{14}$ Hz. Its work function is about ($h=6.63\times10^{-34}\ \text{J}\cdot\text{s}$)",
    [r"$4.0\times10^{-19}$ J", r"$1.1\times10^{-48}$ J", r"$4.0\times10^{-20}$ J", r"$9.0\times10^{47}$ J"],
    r"At the threshold the photon energy just equals the work function: $W_0=h\nu_0=6.63\times10^{-34}\times6\times10^{14}\approx4.0\times10^{-19}$ J.",
    R(h * 6e14))

M.q("p-pe-05", "photoelectric", 1,
    r"Light of frequency below the threshold frequency shines on a metal. Then",
    [r"no photoelectrons are emitted, however intense the light", r"electrons are emitted after a delay", r"electrons are emitted if the light is bright enough", r"electrons are emitted with zero speed"],
    r"Each electron absorbs one photon. If $h\nu<W_0$, no single photon can free an electron, so intensity and exposure time do not help.")

M.q("p-pe-06", "photoelectric", 3,
    r"In a photoelectric experiment the stopping voltage is $2$ V. The maximum kinetic energy of the photoelectrons is ($e=1.6\times10^{-19}$ C)",
    [r"$3.2\times10^{-19}$ J", r"$1.6\times10^{-19}$ J", r"$2$ J", r"$8\times10^{-20}$ J"],
    r"The stopping voltage removes all the kinetic energy: $E_{k\max}=eU_c=1.6\times10^{-19}\times2=3.2\times10^{-19}$ J ($=2$ eV).",
    R(e * 2))

M.q("p-pe-07", "photoelectric", 2,
    r"$1$ eV is equal to ($e=1.6\times10^{-19}$ C)",
    [r"$1.6\times10^{-19}$ J", r"$1$ J", r"$6.25\times10^{18}$ J", r"$1.6\times10^{19}$ J"],
    r"$1$ eV is the energy gained by one electron crossing $1$ V: $1.6\times10^{-19}\ \text{C}\times1\ \text{V}=1.6\times10^{-19}$ J.",
    R(e * 1))

M.q("p-pe-08", "photoelectric", 3,
    r"Light of wavelength $300$ nm falls on a metal with work function $3.0$ eV. Using $h=6.63\times10^{-34}\ \text{J}\cdot\text{s}$, $c=3\times10^8$ m/s and $1\ \text{eV}=1.6\times10^{-19}$ J, the maximum kinetic energy of the photoelectrons is about",
    [r"$1.1$ eV", r"$4.1$ eV", r"$3.0$ eV", r"$0.4$ eV"],
    r"Photon energy $E=\dfrac{hc}{\lambda}=\dfrac{6.63\times10^{-34}\times3\times10^8}{3\times10^{-7}}=6.63\times10^{-19}$ J $\approx4.1$ eV. $E_{k\max}=4.1-3.0\approx1.1$ eV.",
    R(h * c / 300e-9 / e - 3.0, rel=0.05))

M.q("p-pe-09", "photoelectric", 1,
    r"The photoelectric effect provides evidence that light",
    [r"has a particle nature (photons)", r"is a longitudinal wave", r"travels slower in a vacuum", r"needs a medium"],
    r"Instant emission, a threshold frequency and $E_{k\max}$ depending on frequency (not intensity) can only be explained if light energy comes in quanta $h\nu$ — photons.")

M.q("p-atm-01", "atomic-structure", 1,
    r"In Rutherford's $\alpha$-particle scattering experiment, a few $\alpha$ particles bounced back. This showed that",
    [r"the atom has a tiny, dense, positively charged nucleus", r"electrons orbit in fixed shells", r"the atom is a uniform positive sphere", r"atoms are indivisible"],
    r"Most $\alpha$ particles passed straight through (the atom is mostly empty), but a few were turned back by something small, massive and positive: the nucleus.")

M.q("p-atm-02", "atomic-structure", 2,
    r"A hydrogen atom drops from the $n=3$ energy level ($-1.51$ eV) to the $n=2$ level ($-3.40$ eV). The energy of the emitted photon is",
    [r"$1.89$ eV", r"$4.91$ eV", r"$3.40$ eV", r"$1.51$ eV"],
    r"$h\nu=E_3-E_2=-1.51-(-3.40)=1.89$ eV (a red line of the Balmer series).",
    R(-1.51 - (-3.40)))

M.q("p-atm-03", "atomic-structure", 2,
    r"Hydrogen atoms in the $n=4$ state return to the ground state. The maximum number of different spectral lines they can emit is",
    [r"$6$", r"$4$", r"$3$", r"$10$"],
    r"Any pair of the levels $1,2,3,4$ gives a line: $C_4^2=\dfrac{4\times3}2=6$.",
    N(len([(i, j) for i in range(1, 5) for j in range(1, 5) if i > j])))

M.q("p-atm-04", "atomic-structure", 1,
    r"According to Bohr's model, an atom emits light when an electron",
    [r"jumps from a higher energy level to a lower one", r"moves in a stable orbit", r"jumps from a lower level to a higher one", r"leaves the nucleus"],
    r"Electrons in stationary orbits do not radiate. A photon with $h\nu=E_m-E_n$ is emitted when an electron jumps down; absorbing a photon makes it jump up.")

M.q("p-atm-05", "atomic-structure", 2,
    r"The ground-state energy of hydrogen is $-13.6$ eV. The minimum energy needed to ionise a hydrogen atom in the ground state is",
    [r"$13.6$ eV", r"$-13.6$ eV", r"$3.4$ eV", r"$10.2$ eV"],
    r"Ionisation means raising the electron to $E=0$ ($n=\infty$): $0-(-13.6)=13.6$ eV.",
    R(0 - (-13.6)))

M.q("p-atm-06", "atomic-structure", 3,
    r"A hydrogen atom is in its ground state ($E_1=-13.6$ eV, $E_2=-3.4$ eV, $E_3=-1.51$ eV). Which photon can it absorb?",
    [r"$10.2$ eV", r"$11.0$ eV", r"$5.0$ eV", r"$2.0$ eV"],
    r"A photon is absorbed only if its energy exactly matches a level difference: $E_2-E_1=10.2$ eV ✔, $E_3-E_1=12.09$ eV. The other values match no transition (and are below $13.6$ eV, so they cannot ionise).",
    R(-3.4 - (-13.6), rel=0.001))

M.q("p-atm-07", "atomic-structure", 1,
    r"The line spectrum of a gas is evidence that",
    [r"atomic energy levels are discrete", r"atoms have no structure", r"electrons can have any energy", r"light is a longitudinal wave"],
    r"Only certain photon energies (sharp lines) appear, so only certain energy differences — and thus only certain energy levels — exist inside the atom.")

M.q("p-atm-08", "atomic-structure", 2,
    r"The energy levels of hydrogen are $E_n=\dfrac{-13.6}{n^2}$ eV. The energy of the $n=2$ level is",
    [r"$-3.4$ eV", r"$-6.8$ eV", r"$-27.2$ eV", r"$-1.51$ eV"],
    r"$E_2=\dfrac{-13.6}{4}=-3.4$ eV. Divide by $n^2$, not by $n$.",
    R(-13.6 / 2 ** 2))

M.q("p-nuc-01", "nuclear", 1,
    r"The nucleus $^{235}_{92}\text{U}$ contains",
    [r"$92$ protons and $143$ neutrons", r"$92$ protons and $235$ neutrons", r"$143$ protons and $92$ neutrons", r"$235$ protons and $92$ neutrons"],
    r"The lower number is the proton number $Z=92$; the upper is the mass number $A=235$. Neutrons: $A-Z=143$.",
    Nums(92, 235 - 92))

M.q("p-nuc-02", "nuclear", 2,
    r"$^{238}_{92}\text{U}$ undergoes one $\alpha$ decay. The product nucleus is",
    [r"$^{234}_{90}\text{Th}$", r"$^{234}_{92}\text{U}$", r"$^{238}_{93}\text{Np}$", r"$^{236}_{90}\text{Th}$"],
    r"An $\alpha$ particle is $^4_2\text{He}$: the mass number falls by $4$ and the charge number by $2$: $^{238}_{92}\text{U}\to{}^{234}_{90}\text{Th}+{}^4_2\text{He}$.",
    Fn(lambda o: re.findall(r"\^\{(\d+)\}_\{(\d+)\}", o) == [(str(238 - 4), str(92 - 2))], "alpha decay A-4, Z-2"))

M.q("p-nuc-03", "nuclear", 2,
    r"In $\beta^-$ decay, the nucleus",
    [r"keeps its mass number and its charge number increases by $1$", r"loses $4$ from its mass number", r"keeps its charge number and its mass number increases by $1$", r"emits a proton"],
    r"In $\beta^-$ decay a neutron turns into a proton and an electron is emitted: $A$ unchanged, $Z\to Z+1$.")

M.q("p-nuc-04", "nuclear", 2,
    r"A radioactive sample has a half-life of $5$ days. After $15$ days, the fraction of the original nuclei remaining is",
    [r"$\dfrac18$", r"$\dfrac13$", r"$\dfrac14$", r"$\dfrac1{16}$"],
    r"$15$ days is $3$ half-lives: $\left(\dfrac12\right)^3=\dfrac18$.",
    N(sp.Rational(1, 2) ** (15 // 5)))

M.q("p-nuc-05", "nuclear", 3,
    r"$16$ g of a radioactive isotope decays to $1$ g in $20$ hours. Its half-life is",
    [r"$5$ h", r"$4$ h", r"$10$ h", r"$1.25$ h"],
    r"$\dfrac{1}{16}=\left(\dfrac12\right)^4$, so $4$ half-lives passed in $20$ h: $T_{1/2}=5$ h.",
    R(20 / sp.log(16, 2)))

M.q("p-nuc-06", "nuclear", 1,
    r"The half-life of a radioactive substance",
    [r"is not changed by temperature or pressure", r"doubles when the temperature doubles", r"depends on the amount of substance", r"decreases when it is made into a compound"],
    r"Radioactive decay is a nuclear process; its half-life is unaffected by physical or chemical conditions and by the sample size.")

M.q("p-nuc-07", "nuclear", 2,
    r"In the reaction $^{2}_{1}\text{H}+{}^{3}_{1}\text{H}\to{}^{4}_{2}\text{He}+X$, the particle $X$ is",
    [r"a neutron", r"a proton", r"an electron", r"an $\alpha$ particle"],
    r"Conserve mass number: $2+3=4+A\Rightarrow A=1$; charge: $1+1=2+Z\Rightarrow Z=0$. $^1_0n$ is a neutron. (This is a fusion reaction.)",
    Fn(lambda o: "neutron" in o and (2 + 3 - 4, 1 + 1 - 2) == (1, 0), "A=1,Z=0"))

M.q("p-nuc-08", "nuclear", 3,
    r"In a nuclear reaction the mass decreases by $1\times10^{-29}$ kg. The energy released is ($c=3\times10^8$ m/s)",
    [r"$9\times10^{-13}$ J", r"$3\times10^{-21}$ J", r"$9\times10^{-29}$ J", r"$3\times10^{-13}$ J"],
    r"$\Delta E=\Delta mc^2=1\times10^{-29}\times9\times10^{16}=9\times10^{-13}$ J.",
    R(1e-29 * c ** 2))

M.q("p-nuc-09", "nuclear", 1,
    r"Which radiation is the most penetrating?",
    [r"$\gamma$ rays", r"$\alpha$ particles", r"$\beta$ particles", r"They are all equal"],
    r"$\alpha$ is stopped by paper, $\beta$ by a few mm of aluminium; $\gamma$ rays (high-energy photons, no charge) need thick lead or concrete. $\alpha$ is the most strongly ionising.")
