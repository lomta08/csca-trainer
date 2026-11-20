from qb import *  # noqa: F403

B = Bank("physics", "electromagnetism")
kC = 9e9
e = 1.6e-19


def par(*rs):
    return 1 / sum(sp.Rational(1) / r_ for r_ in rs)


# ------------------------------------------------------------ electrostatics
B.q("p-es-01", "electrostatics", 2,
    r"Two point charges of $2\times10^{-6}$ C and $3\times10^{-6}$ C are $0.3$ m apart. Using $k=9\times10^9\ \text{N}\cdot\text{m}^2/\text{C}^2$, the force between them is",
    [r"$0.6$ N", r"$0.2$ N", r"$1.8$ N", r"$6$ N"],
    r"$F=k\dfrac{q_1q_2}{r^2}=9\times10^9\times\dfrac{6\times10^{-12}}{0.09}=0.6$ N (repulsive, since both are positive).",
    R(kC * 2e-6 * 3e-6 / 0.3 ** 2))

B.q("p-es-02", "electrostatics", 1,
    r"If the distance between two point charges is halved, the Coulomb force between them becomes",
    [r"$4$ times as large", r"$2$ times as large", r"half as large", r"unchanged"],
    r"$F\propto\dfrac1{r^2}$: halving $r$ multiplies $F$ by $2^2=4$.")

B.q("p-es-03", "electrostatics", 2,
    r"A charge of $2\times10^{-8}$ C placed at a point in an electric field experiences a force of $4\times10^{-4}$ N. The field strength there is",
    [r"$2\times10^{4}$ N/C", r"$8\times10^{-12}$ N/C", r"$5\times10^{-5}$ N/C", r"$2\times10^{-4}$ N/C"],
    r"$E=\dfrac Fq=\dfrac{4\times10^{-4}}{2\times10^{-8}}=2\times10^4$ N/C. The field strength does not depend on the test charge.",
    R(4e-4 / 2e-8))

B.q("p-es-04", "electrostatics", 2,
    r"The electric field strength at a distance of $0.2$ m from a point charge $Q=4\times10^{-9}$ C is ($k=9\times10^9\ \text{N}\cdot\text{m}^2/\text{C}^2$)",
    [r"$900$ N/C", r"$180$ N/C", r"$1800$ N/C", r"$90$ N/C"],
    r"$E=\dfrac{kQ}{r^2}=\dfrac{9\times10^9\times4\times10^{-9}}{0.04}=900$ N/C.",
    R(kC * 4e-9 / 0.2 ** 2))

B.q("p-es-05", "electrostatics", 2,
    r"Moving a charge of $3\times10^{-6}$ C from point $A$ to point $B$, the electric field does $6\times10^{-4}$ J of work. The potential difference $U_{AB}$ is",
    [r"$200$ V", r"$18\times10^{-10}$ V", r"$5\times10^{-3}$ V", r"$-200$ V"],
    r"$U_{AB}=\dfrac{W_{AB}}{q}=\dfrac{6\times10^{-4}}{3\times10^{-6}}=200$ V. Positive work on a positive charge means $A$ is at the higher potential.",
    R(6e-4 / 3e-6))

B.q("p-es-06", "electrostatics", 2,
    r"Two parallel plates $0.02$ m apart have a potential difference of $100$ V. The uniform field between them is",
    [r"$5000$ V/m", r"$2$ V/m", r"$200$ V/m", r"$50$ V/m"],
    r"In a uniform field $E=\dfrac Ud=\dfrac{100}{0.02}=5000$ V/m.",
    R(100 / 0.02))

B.q("p-es-07", "electrostatics", 1,
    r"Electric field lines",
    [r"point from positive charges toward negative charges", r"can cross each other", r"show the path of every charged particle", r"are closer together where the field is weaker"],
    r"Field lines start on positive charges and end on negative ones, never cross (the field has one direction at each point), and are denser where the field is stronger. A particle's path generally does not follow a field line.")

B.q("p-es-08", "electrostatics", 2,
    r"An electron is accelerated from rest through a potential difference of $100$ V. Its gain in kinetic energy is ($e=1.6\times10^{-19}$ C)",
    [r"$1.6\times10^{-17}$ J", r"$1.6\times10^{-19}$ J", r"$6.25\times10^{20}$ J", r"$1.6\times10^{-21}$ J"],
    r"$E_k=eU=1.6\times10^{-19}\times100=1.6\times10^{-17}$ J (that is, $100$ eV).",
    R(e * 100))

B.q("p-es-09", "electrostatics", 2,
    r"A capacitor of capacitance $10\ \mu\text{F}$ is connected to a $6$ V supply. The charge stored is",
    [r"$6\times10^{-5}$ C", r"$60$ C", r"$1.67\times10^{-6}$ C", r"$6\times10^{-6}$ C"],
    r"$Q=CU=10\times10^{-6}\times6=6\times10^{-5}$ C. Remember $1\ \mu\text{F}=10^{-6}$ F.",
    R(10e-6 * 6))

B.q("p-es-10", "electrostatics", 3,
    r"A parallel-plate capacitor stays connected to a battery while the distance between its plates is doubled. Which statement is correct?",
    [r"The charge on the plates is halved", r"The voltage between the plates is halved", r"The capacitance doubles", r"The field between the plates is unchanged"],
    r"""Connected to the battery, $U$ stays constant. $C=\dfrac{\varepsilon S}{4\pi kd}$ halves when $d$ doubles, so $Q=CU$ halves, and $E=\dfrac Ud$ also halves.""")

B.q("p-es-11", "electrostatics", 2,
    r"A positive charge moves along an electric field line in the direction of the field. Its electric potential energy",
    [r"decreases", r"increases", r"stays the same", r"first increases then decreases"],
    r"The field does positive work on a positive charge moving along the field, so its potential energy decreases (it moves to lower potential). For a negative charge it would increase.")

B.q("p-es-12", "electrostatics", 3,
    r"A small ball of mass $2\times10^{-3}$ kg and charge $1\times10^{-6}$ C hangs at rest in a uniform **vertical** electric field, with no string " + r"(take $g=10\ \text{m/s}^2$). The field strength is",
    [r"$2\times10^{4}$ N/C", r"$2\times10^{-2}$ N/C", r"$5\times10^{-5}$ N/C", r"$2\times10^{3}$ N/C"],
    r"Balance: $qE=mg\Rightarrow E=\dfrac{2\times10^{-3}\times10}{1\times10^{-6}}=2\times10^4$ N/C, directed upward (for a positive charge).",
    R(2e-3 * 10 / 1e-6))

# ------------------------------------------------------------ DC circuits
B.q("p-dc-01", "dc-circuits", 1,
    r"A $6$ V supply drives a current of $0.5$ A through a resistor. The resistance is",
    [r"$12\ \Omega$", r"$3\ \Omega$", r"$0.083\ \Omega$", r"$6.5\ \Omega$"],
    r"Ohm's law: $R=\dfrac UI=\dfrac{6}{0.5}=12\ \Omega$.",
    R(6 / 0.5))

B.q("p-dc-02", "dc-circuits", 1,
    r"Resistors of $4\ \Omega$ and $6\ \Omega$ are connected in series. The total resistance is",
    [r"$10\ \Omega$", r"$2.4\ \Omega$", r"$24\ \Omega$", r"$2\ \Omega$"],
    r"In series, resistances add: $4+6=10\ \Omega$.",
    R(4 + 6))

B.q("p-dc-03", "dc-circuits", 1,
    r"Resistors of $4\ \Omega$ and $6\ \Omega$ are connected in parallel. The total resistance is",
    [r"$2.4\ \Omega$", r"$10\ \Omega$", r"$5\ \Omega$", r"$0.42\ \Omega$"],
    r"$\dfrac1R=\dfrac14+\dfrac16=\dfrac5{12}\Rightarrow R=2.4\ \Omega$ (or $\dfrac{R_1R_2}{R_1+R_2}=\dfrac{24}{10}$). A parallel combination is always smaller than the smallest branch.",
    R(par(4, 6)))

B.q("p-dc-04", "dc-circuits", 2,
    r"A $1000$ W kettle runs for $3$ minutes. The electrical energy it uses is",
    [r"$1.8\times10^{5}$ J", r"$3000$ J", r"$333$ J", r"$1.8\times10^{4}$ J"],
    r"$W=Pt=1000\times180=1.8\times10^5$ J. Convert minutes to seconds first.",
    R(1000 * 3 * 60))

B.q("p-dc-05", "dc-circuits", 2,
    r"A battery of EMF $3$ V and internal resistance $1\ \Omega$ is connected to a $5\ \Omega$ resistor. The terminal voltage is",
    [r"$2.5$ V", r"$3$ V", r"$0.5$ V", r"$0.6$ V"],
    r"$I=\dfrac{E}{R+r}=\dfrac36=0.5$ A, so $U=IR=0.5\times5=2.5$ V. The remaining $0.5$ V is lost across the internal resistance.",
    R(3 / (5 + 1) * 5))

B.q("p-dc-06", "dc-circuits", 2,
    r"A $2\ \Omega$ resistor carries a current of $3$ A. The power dissipated is",
    [r"$18$ W", r"$6$ W", r"$12$ W", r"$1.5$ W"],
    r"$P=I^2R=9\times2=18$ W.",
    R(3 ** 2 * 2))

B.q("p-dc-07", "dc-circuits", 2,
    r"A lamp is rated “$6$ V, $3$ W”. Its resistance when working normally is",
    [r"$12\ \Omega$", r"$2\ \Omega$", r"$18\ \Omega$", r"$0.5\ \Omega$"],
    r"$P=\dfrac{U^2}{R}\Rightarrow R=\dfrac{36}{3}=12\ \Omega$. (Its rated current is $\dfrac PU=0.5$ A.)",
    R(6 ** 2 / 3))

B.q("p-dc-08", "dc-circuits", 3,
    r"A $3\ \Omega$ resistor is connected in series with a parallel pair of $6\ \Omega$ resistors, across a $12$ V supply with negligible internal resistance. The current from the supply is",
    [r"$2$ A", r"$0.8$ A", r"$4$ A", r"$1.33$ A"],
    r"Parallel pair: $\dfrac{6\times6}{12}=3\ \Omega$. Total $3+3=6\ \Omega$, so $I=\dfrac{12}{6}=2$ A.",
    R(12 / (3 + par(6, 6))))

B.q("p-dc-09", "dc-circuits", 3,
    r"In a circuit with a battery (EMF $E$, internal resistance $r$) and a variable resistor $R$, as $R$ is increased the terminal voltage",
    [r"increases and the current decreases", r"decreases and the current increases", r"stays equal to $E$", r"decreases and the current decreases"],
    r"$I=\dfrac{E}{R+r}$ decreases as $R$ grows, so the internal voltage drop $Ir$ shrinks and the terminal voltage $U=E-Ir$ increases toward $E$.")

B.q("p-dc-10", "dc-circuits", 2,
    r"A copper wire has resistance $R$. It is stretched uniformly to twice its length (its volume is unchanged). Its new resistance is",
    [r"$4R$", r"$2R$", r"$R$", r"$\dfrac R2$"],
    r"$R=\rho\dfrac LS$. Doubling $L$ at constant volume halves the cross-section $S$, so $R'=\rho\dfrac{2L}{S/2}=4R$.")

B.q("p-dc-11", "dc-circuits", 1,
    r"Two resistors are connected in parallel. Which quantity is the same for both?",
    [r"The voltage across them", r"The current through them", r"The power in them", r"Their resistance"],
    r"Parallel components are connected across the same two points, so they have the same potential difference. Currents divide in inverse proportion to resistance.")

B.q("p-dc-12", "dc-circuits", 3,
    r"A battery of EMF $6$ V and internal resistance $2\ \Omega$ powers a variable resistor $R$. The maximum power that can be delivered to $R$ is",
    [r"$4.5$ W", r"$18$ W", r"$9$ W", r"$3$ W"],
    r"The output power $P=\dfrac{E^2R}{(R+r)^2}$ is largest when $R=r=2\ \Omega$: $P_{\max}=\dfrac{E^2}{4r}=\dfrac{36}{8}=4.5$ W.",
    R(sp.maximum(36 * x / (x + 2) ** 2, x, sp.Interval(0, sp.oo))))

# ------------------------------------------------------------ magnetic fields
B.q("p-mag-01", "magnetic-fields", 1,
    r"A straight wire $0.5$ m long carries $2$ A perpendicular to a uniform magnetic field of $0.4$ T. The magnetic (Ampère) force on it is",
    [r"$0.4$ N", r"$1.6$ N", r"$0.1$ N", r"$4$ N"],
    r"$F=BIL=0.4\times2\times0.5=0.4$ N.",
    R(0.4 * 2 * 0.5))

B.q("p-mag-02", "magnetic-fields", 1,
    r"A current-carrying wire placed **parallel** to a uniform magnetic field experiences a magnetic force of",
    [r"zero", r"$BIL$", r"$\dfrac{BIL}{2}$", r"a maximum value"],
    r"$F=BIL\sin\theta$ with $\theta=0^\circ$ between the current and the field, so $F=0$.")

B.q("p-mag-03", "magnetic-fields", 2,
    r"A proton ($q=1.6\times10^{-19}$ C) moves at $2\times10^{6}$ m/s perpendicular to a $0.5$ T magnetic field. The Lorentz force on it is",
    [r"$1.6\times10^{-13}$ N", r"$6.4\times10^{-13}$ N", r"$1.6\times10^{-19}$ N", r"$3.2\times10^{-14}$ N"],
    r"$F=qvB=1.6\times10^{-19}\times2\times10^6\times0.5=1.6\times10^{-13}$ N.",
    R(e * 2e6 * 0.5))

B.q("p-mag-04", "magnetic-fields", 2,
    r"The Lorentz force on a charged particle moving in a magnetic field",
    [r"does no work on the particle", r"increases the particle's speed", r"is parallel to the velocity", r"is independent of the charge"],
    r"$\vec F=q\vec v\times\vec B$ is always perpendicular to the velocity, so it changes the direction of motion but never the speed: it does no work.")

B.q("p-mag-05", "magnetic-fields", 3,
    r"A particle of mass $m$ and charge $q$ moves at speed $v$ perpendicular to a uniform field $B$. The radius of its circular path is",
    [r"$\dfrac{mv}{qB}$", r"$\dfrac{qB}{mv}$", r"$\dfrac{mv^2}{qB}$", r"$\dfrac{qvB}{m}$"],
    r"The magnetic force provides the centripetal force: $qvB=\dfrac{mv^2}{r}\Rightarrow r=\dfrac{mv}{qB}$.")

B.q("p-mag-06", "magnetic-fields", 3,
    r"In a uniform magnetic field, the period of the circular motion of a charged particle",
    [r"does not depend on its speed", r"is proportional to its speed", r"is inversely proportional to its speed", r"is proportional to the radius"],
    r"$T=\dfrac{2\pi r}{v}=\dfrac{2\pi m}{qB}$: the speed cancels. Faster particles move on bigger circles in the same time (the principle of the cyclotron).")

B.q("p-mag-07", "magnetic-fields", 1,
    r"The SI unit of magnetic induction (magnetic flux density) $B$ is the",
    [r"tesla (T)", r"weber (Wb)", r"henry (H)", r"newton per coulomb (N/C)"],
    r"$B$ is measured in teslas: $1\ \text{T}=1\ \text{N/(A}\cdot\text{m)}$. The weber is the unit of magnetic **flux** $\Phi=BS$.")

B.q("p-mag-08", "magnetic-fields", 2,
    r"Two long parallel wires carry currents in the **same** direction. The wires",
    [r"attract each other", r"repel each other", r"exert no force on each other", r"twist to become perpendicular"],
    r"Each wire sits in the magnetic field of the other; applying the left-hand rule shows parallel currents attract and antiparallel currents repel.")

B.q("p-mag-09", "magnetic-fields", 2,
    r"An electron with speed $1\times10^{7}$ m/s moves perpendicular to a $2\times10^{-3}$ T field. Using $m_e=9.1\times10^{-31}$ kg and $e=1.6\times10^{-19}$ C, the radius of its path is about",
    [r"$2.8\times10^{-2}$ m", r"$2.8\times10^{-5}$ m", r"$3.5\times10^{1}$ m", r"$1.1\times10^{-2}$ m"],
    r"$r=\dfrac{mv}{eB}=\dfrac{9.1\times10^{-31}\times10^7}{1.6\times10^{-19}\times2\times10^{-3}}\approx2.8\times10^{-2}$ m.",
    R(9.1e-31 * 1e7 / (e * 2e-3)))

B.q("p-mag-10", "magnetic-fields", 1,
    r"The magnetic field lines around a long straight current-carrying wire are",
    [r"concentric circles around the wire", r"straight lines parallel to the wire", r"straight lines pointing away from the wire", r"absent"],
    r"The field circles the wire; its direction follows the right-hand (screw) rule: thumb along the current, fingers curl in the direction of $B$.")

B.q("p-mag-11", "magnetic-fields", 2,
    r"A rectangular coil of area $0.02\ \text{m}^2$ is placed perpendicular to a uniform field of $0.5$ T. The magnetic flux through it is",
    [r"$0.01$ Wb", r"$0.1$ Wb", r"$25$ Wb", r"$0.04$ Wb"],
    r"$\Phi=BS=0.5\times0.02=0.01$ Wb (the field is perpendicular to the coil's plane).",
    R(0.5 * 0.02))

B.q("p-mag-12", "magnetic-fields", 3,
    r"A $0.2$ m long, $0.05$ kg rod hangs horizontally from two light wires in a horizontal magnetic field of $0.5$ T perpendicular to the rod " + r"(take $g=10\ \text{m/s}^2$). The current needed for the wires to become slack is",
    [r"$5$ A", r"$0.5$ A", r"$2.5$ A", r"$50$ A"],
    r"The upward Ampère force must balance the weight: $BIL=mg\Rightarrow I=\dfrac{0.05\times10}{0.5\times0.2}=5$ A.",
    R(0.05 * 10 / (0.5 * 0.2)))

# ---------------------------------------------------- electromagnetic induction
B.q("p-ind-01", "em-induction", 2,
    r"The flux through a $100$-turn coil changes uniformly from $0.02$ Wb to $0.06$ Wb in $0.4$ s. The induced EMF is",
    [r"$10$ V", r"$0.1$ V", r"$1$ V", r"$40$ V"],
    r"Faraday's law: $E=n\dfrac{\Delta\Phi}{\Delta t}=100\times\dfrac{0.04}{0.4}=10$ V.",
    R(100 * (0.06 - 0.02) / 0.4))

B.q("p-ind-02", "em-induction", 1,
    r"A $0.5$ m rod moves at $4$ m/s perpendicular to a $0.2$ T magnetic field, cutting the field lines. The induced EMF is",
    [r"$0.4$ V", r"$0.1$ V", r"$10$ V", r"$1.6$ V"],
    r"Motional EMF: $E=BLv=0.2\times0.5\times4=0.4$ V.",
    R(0.2 * 0.5 * 4))

B.q("p-ind-03", "em-induction", 1,
    r"Lenz's law states that the induced current",
    [r"opposes the change in magnetic flux that produces it", r"always flows clockwise", r"strengthens the change in flux", r"is independent of the change in flux"],
    r"The induced current creates a magnetic field that opposes the **change** in flux — a consequence of energy conservation.")

B.q("p-ind-04", "em-induction", 2,
    r"A magnet's north pole is pushed toward a closed coil. The induced current makes the end of the coil facing the magnet",
    [r"a north pole, repelling the magnet", r"a south pole, attracting the magnet", r"a south pole, repelling the magnet", r"unmagnetised"],
    r"By Lenz's law the coil opposes the approach, so the near face becomes a north pole and repels the incoming north pole. You must do work to push the magnet in, and that work becomes electrical energy.")

B.q("p-ind-05", "em-induction", 2,
    r"A rod of length $0.5$ m slides at $2$ m/s on rails in a $0.4$ T field (perpendicular to the plane). The circuit's total resistance is $0.2\ \Omega$. The induced current is",
    [r"$2$ A", r"$0.4$ A", r"$0.08$ A", r"$4$ A"],
    r"$E=BLv=0.4\times0.5\times2=0.4$ V, so $I=\dfrac ER=\dfrac{0.4}{0.2}=2$ A.",
    R(0.4 * 0.5 * 2 / 0.2))

B.q("p-ind-06", "em-induction", 3,
    r"For the rod in the previous situation ($B=0.4$ T, $L=0.5$ m, $I=2$ A), the external force needed to keep it moving at constant speed is",
    [r"$0.4$ N", r"$0.2$ N", r"$0.8$ N", r"$4$ N"],
    r"At constant speed the applied force balances the Ampère force on the rod: $F=BIL=0.4\times2\times0.5=0.4$ N.",
    R(0.4 * (0.4 * 0.5 * 2 / 0.2) * 0.5))

B.q("p-ind-07", "em-induction", 1,
    r"An induced current is produced in a closed loop when",
    [r"the magnetic flux through the loop changes", r"the loop is in a strong steady magnetic field", r"the loop is made of copper", r"the loop is moved parallel to field lines in a uniform field"],
    r"Only a **change** in flux induces an EMF. A strong but steady flux, or motion that leaves the flux unchanged, produces no current.")

B.q("p-ind-08", "em-induction", 2,
    r"An ideal transformer has $200$ turns on the primary and $50$ turns on the secondary. With $220$ V on the primary, the secondary voltage is",
    [r"$55$ V", r"$880$ V", r"$220$ V", r"$44$ V"],
    r"$\dfrac{U_1}{U_2}=\dfrac{n_1}{n_2}\Rightarrow U_2=220\times\dfrac{50}{200}=55$ V (a step-down transformer).",
    R(220 * 50 / 200))

B.q("p-ind-09", "em-induction", 2,
    r"A coil of $50$ turns and area $0.01\ \text{m}^2$ is perpendicular to a field that increases uniformly from $0$ to $0.4$ T in $0.2$ s. The induced EMF is",
    [r"$1$ V", r"$0.02$ V", r"$100$ V", r"$0.4$ V"],
    r"$E=nS\dfrac{\Delta B}{\Delta t}=50\times0.01\times\dfrac{0.4}{0.2}=1$ V.",
    R(50 * 0.01 * 0.4 / 0.2))

B.q("p-ind-10", "em-induction", 3,
    r"A conducting ring falls past a fixed bar magnet held vertically. Compared with free fall, the ring's acceleration while it approaches the magnet is",
    [r"less than $g$", r"greater than $g$", r"exactly $g$", r"zero"],
    r"The changing flux induces a current in the ring that opposes the relative motion (Lenz's law), giving an upward magnetic force. So the acceleration is less than $g$ both when approaching and when leaving the magnet.")

B.q("p-ind-11", "em-induction", 2,
    r"A step-up transformer increases the voltage from $10$ kV to $500$ kV for transmission. With the same power transmitted, the power lost in the line becomes",
    [r"$\dfrac{1}{2500}$ of the original", r"$\dfrac{1}{50}$ of the original", r"$50$ times the original", r"unchanged"],
    r"For the same power, $I=\dfrac PU$ falls by a factor of $50$, and the line loss $I^2R$ falls by $50^2=2500$.",
    T(f"\\dfrac{{1}}{{{(500 // 10) ** 2}}} of the original"))

B.q("p-ind-12", "em-induction", 1,
    r"Which device works on the principle of electromagnetic induction?",
    [r"A generator", r"An electric motor", r"An electric heater", r"An electromagnet"],
    r"A generator converts mechanical energy into electrical energy by rotating a coil in a magnetic field, changing the flux. A motor uses the force on a current in a field (the reverse process).")
