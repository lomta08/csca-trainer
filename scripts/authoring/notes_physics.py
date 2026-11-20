"""Writes physics lesson notes to src/content/notes/physics/*.md. Original explanations."""
from pathlib import Path

OUT = Path(__file__).resolve().parents[2] / "src" / "content" / "notes" / "physics"
OUT.mkdir(parents=True, exist_ok=True)
N = {}

N["kinematics"] = r"""
## Key ideas

- **Displacement** $\vec x$ (vector, straight-line change of position) vs **distance** (path length, scalar).
- **Velocity** $v=\dfrac{\Delta x}{\Delta t}$ (vector) vs **speed** (scalar). Average velocity uses displacement; average speed uses distance.
- **Acceleration** $a=\dfrac{\Delta v}{\Delta t}$, unit $\text{m/s}^2$.

## Uniformly accelerated motion

$$v=v_0+at,\qquad x=v_0t+\tfrac12at^2,\qquad v^2-v_0^2=2ax,\qquad \bar v=\frac{v_0+v}{2}=v_{t/2}.$$

From rest: distances in successive equal times are in the ratio $1:3:5:\dots$; total distances after $t,2t,3t$ are $1:4:9$. Successive equal intervals: $\Delta x=aT^2$.

**Free fall** ($v_0=0$, $a=g$; take $g=10\ \text{m/s}^2$ unless told otherwise): $v=gt$, $h=\tfrac12gt^2$, $v^2=2gh$. Thrown up at $v_0$: max height $\dfrac{v_0^2}{2g}$, time to the top $\dfrac{v_0}g$.

**Projectile thrown horizontally:** horizontal $x=v_0t$ (uniform), vertical $y=\tfrac12gt^2$ (free fall); time depends only on height: $t=\sqrt{2h/g}$.

**Graphs:** slope of $x$–$t$ = velocity; slope of $v$–$t$ = acceleration; area under $v$–$t$ = displacement.

## Worked examples

**Example 1.** A car at $15$ m/s brakes at $3\ \text{m/s}^2$. How far does it go in $6$ s?

*Solution.* It stops after $5$ s, so use $x=\dfrac{v_0^2}{2a}=\dfrac{225}{6}=37.5$ m (not $15\cdot6-\tfrac12\cdot3\cdot36$).

**Example 2.** A ball is thrown horizontally at $8$ m/s from $5$ m ($g=10\ \text{m/s}^2$). Find the range.

*Solution.* $t=\sqrt{2\cdot5/10}=1$ s, $x=8$ m.

**Example 3.** An object starting from rest covers $4$ m in its first $2$ s. Find $a$ and the distance in the 3rd second.

*Solution.* $4=\tfrac12a\cdot4\Rightarrow a=2\ \text{m/s}^2$. Distance in the 3rd second $=\tfrac12\cdot2(9-4)=5$ m.

## Common traps

- Braking problems: check when the object stops before using the time given.
- Mixing up distance and displacement (average speed vs average velocity).
- Choosing a sign convention and sticking to it (up positive, $a=-g$).
"""

N["newtons-laws"] = r"""
## The three laws

1. **First law (inertia):** an object stays at rest or moves at constant velocity unless a net force acts. Mass measures inertia.
2. **Second law:** $\vec F_{\text{net}}=m\vec a$ ($1\ \text{N}=1\ \text{kg}\cdot\text{m/s}^2$). The acceleration has the direction of the net force.
3. **Third law:** forces come in equal and opposite pairs acting on **different** bodies, of the same type.

## Common forces

- Weight $G=mg$, vertically down.
- Normal force: perpendicular to the contact surface.
- Kinetic friction $f=\mu N$, opposite to the relative motion; static friction is whatever is needed, up to $f_{\max}=\mu_sN$.
- Spring force $F=kx$ (Hooke's law).

**Inclines** (angle $\theta$): components of gravity $mg\sin\theta$ (along) and $mg\cos\theta$ (perpendicular). Smooth incline: $a=g\sin\theta$. With friction (sliding down): $a=g\sin\theta-\mu g\cos\theta$.

**Lifts:** $N=m(g+a)$ accelerating up (overweight), $N=m(g-a)$ accelerating down (underweight); free fall $N=0$.

**Connected bodies:** first treat the whole system ($a=\dfrac{F_{\text{ext}}}{m_{\text{total}}}$), then isolate one body to find internal forces.

## Worked examples

**Example 1.** A $5$ kg box is pulled by $30$ N horizontally; $\mu=0.4$, $g=10\ \text{m/s}^2$. Find $a$.

*Solution.* $f=0.4\times50=20$ N, $a=\dfrac{30-20}{5}=2\ \text{m/s}^2$.

**Example 2.** $m_1=1$ kg and $m_2=4$ kg hang over a light pulley ($g=10\ \text{m/s}^2$). Find $a$ and the tension.

*Solution.* $a=\dfrac{(4-1)g}{5}=6\ \text{m/s}^2$; for $m_1$: $T-10=1\cdot6$, $T=16$ N.

**Example 3.** Forces of $6$ N and $8$ N act at $90^\circ$ on a $2$ kg mass. Find $a$.

*Solution.* $F=10$ N, $a=5\ \text{m/s}^2$.

## Common traps

- Calling the normal force the "reaction" to weight — they act on the same body.
- Using $f=\mu N$ for static friction when the object does not slide.
- Forgetting that constant velocity means **zero** net force, not zero forces.
"""

N["momentum"] = r"""
## Key ideas

- Momentum $\vec p=m\vec v$ (vector, $\text{kg}\cdot\text{m/s}$).
- Impulse $\vec I=\vec F\Delta t$ ($\text{N}\cdot\text{s}$); area under an $F$–$t$ graph.
- **Impulse–momentum theorem:** $\vec F_{\text{net}}\Delta t=\Delta\vec p=m\vec v-m\vec v_0$.

## Conservation of momentum

If the net **external** force on a system is zero (or negligible during a short collision/explosion):
$$m_1v_1+m_2v_2=m_1v_1'+m_2v_2'.$$

| Collision | Momentum | Kinetic energy |
|---|---|---|
| Elastic | conserved | conserved |
| Inelastic | conserved | partly lost |
| Perfectly inelastic (stick together) | conserved | maximum loss: $v=\dfrac{m_1v_1+m_2v_2}{m_1+m_2}$ |

Elastic collision with a stationary target: $v_1'=\dfrac{m_1-m_2}{m_1+m_2}v_1$, $v_2'=\dfrac{2m_1}{m_1+m_2}v_1$; equal masses exchange velocities.

## Worked examples

**Example 1.** A $0.2$ kg ball moving at $5$ m/s bounces back at $3$ m/s. Contact time $0.02$ s. Find the average force.

*Solution.* $\Delta p=0.2(3-(-5))=1.6\ \text{kg}\cdot\text{m/s}$, $F=\dfrac{1.6}{0.02}=80$ N.

**Example 2.** A $4$ kg gun fires a $0.02$ kg bullet at $400$ m/s. Find the recoil speed.

*Solution.* $4v=0.02\times400$, $v=2$ m/s.

**Example 3.** $1$ kg at $6$ m/s hits a stationary $2$ kg block and they stick. Find the KE lost.

*Solution.* $v=2$ m/s; KE before $18$ J, after $\tfrac12\cdot3\cdot4=6$ J; lost $12$ J.

## Common traps

- Ignoring direction: a rebound reverses the sign of the velocity.
- Expecting kinetic energy to be conserved in every collision.
- Confusing momentum ($mv$) with kinetic energy ($\tfrac12mv^2$).
"""

N["work-energy"] = r"""
## Key ideas

- Work $W=Fs\cos\theta$ (scalar, J). $\theta=90^\circ$ → no work; $\theta>90^\circ$ → negative work.
- Power $P=\dfrac Wt$, and $P=Fv$ for a force along the velocity.
- Kinetic energy $E_k=\tfrac12mv^2$; gravitational PE $E_p=mgh$; elastic PE $\tfrac12kx^2$.

## Theorems

**Work–energy theorem:** the total work done by all forces equals the change in kinetic energy: $W_{\text{net}}=\Delta E_k$.

**Conservation of mechanical energy:** if only gravity (and spring forces) do work,
$$E_{k1}+E_{p1}=E_{k2}+E_{p2}.$$
Example: falling from height $h$ along any smooth path gives $v=\sqrt{2gh}$.

When friction acts: work done against friction = loss of mechanical energy (heat produced $=f\cdot s_{\text{relative}}$).

**Vehicles at constant power:** $F=\dfrac Pv$; maximum speed when $F=f_{\text{resistance}}$: $v_{\max}=\dfrac P f$.

## Worked examples

**Example 1.** A $2$ kg block slides from rest down a smooth slope of height $1.8$ m ($g=10\ \text{m/s}^2$). Find its speed at the bottom.

*Solution.* $v=\sqrt{2\cdot10\cdot1.8}=6$ m/s.

**Example 2.** A pump lifts $300$ kg of water $10$ m in $1$ min. Find its power.

*Solution.* $W=300\cdot10\cdot10=3\times10^4$ J, $P=\dfrac{3\times10^4}{60}=500$ W.

**Example 3.** A $1$ kg ball at $10$ m/s slides $5$ m on a rough floor and stops. Find the friction force.

*Solution.* $-f\cdot5=0-50$, $f=10$ N.

## Common traps

- Forgetting the $\cos\theta$ in $W=Fs\cos\theta$.
- Using conservation of mechanical energy when friction or air resistance does work.
- Gravity does no work in a horizontal motion or a circular orbit.
"""

N["circular-gravitation"] = r"""
## Circular motion

$$v=\frac{2\pi r}{T}=\omega r,\qquad \omega=\frac{2\pi}{T}=2\pi n,\qquad a=\frac{v^2}r=\omega^2r,\qquad F=\frac{mv^2}{r}=m\omega^2r.$$

The centripetal force is not a new force: it is the **net** force toward the centre (tension, gravity, friction, normal force, …). Points on a rotating rigid body share $\omega$; points on a belt share $v$.

**Vertical circles:** top of a hump: $mg-N=\dfrac{mv^2}r$; bottom of a dip: $N-mg=\dfrac{mv^2}{r}$. Ball on a string at the top: minimum speed $\sqrt{gr}$.

## Universal gravitation

$$F=G\frac{m_1m_2}{r^2},\qquad G=6.67\times10^{-11}\ \text{N}\cdot\text{m}^2/\text{kg}^2.$$

- Surface gravity: $mg=\dfrac{GMm}{R^2}\Rightarrow GM=gR^2$.
- Circular orbit of radius $r$: $\dfrac{GMm}{r^2}=\dfrac{mv^2}{r}$ ⇒ $v=\sqrt{\dfrac{GM}r}$, $T=2\pi\sqrt{\dfrac{r^3}{GM}}$. Higher orbit → slower, longer period.
- First cosmic velocity $7.9$ km/s; escape velocity $11.2$ km/s.
- Geostationary satellites: above the equator, period $24$ h.

## Worked examples

**Example 1.** A $1000$ kg car rounds a flat bend of radius $50$ m at $10$ m/s. What friction is needed?

*Solution.* $F=\dfrac{1000\cdot100}{50}=2000$ N.

**Example 2.** Two satellites orbit with radii $r$ and $9r$. Ratio of periods?

*Solution.* $T\propto r^{3/2}$: $1:27$.

**Example 3.** At what height above the Earth's surface is $g$ one quarter of its surface value?

*Solution.* $g\propto\dfrac1{r^2}$, so $r=2R$: height $=R$.

## Common traps

- Drawing a separate "centripetal force" on force diagrams.
- Using the height above the surface instead of the distance from the centre in $F=\dfrac{GMm}{r^2}$.
- Thinking faster satellites are in higher orbits.
"""

N["shm-waves"] = r"""
## Simple harmonic motion

Restoring force $F=-kx$. Displacement $x=A\sin(\omega t+\varphi)$, with $\omega=2\pi f=\dfrac{2\pi}T$.

- Spring oscillator: $T=2\pi\sqrt{\dfrac mk}$. Simple pendulum (small angles): $T=2\pi\sqrt{\dfrac Lg}$ (independent of mass and amplitude).
- At equilibrium: speed maximum ($v_{\max}=A\omega$), acceleration zero. At the extremes: speed zero, acceleration maximum.
- Energy swaps between kinetic and potential; the total is constant (no damping).
- **Resonance:** maximum amplitude when the driving frequency equals the natural frequency.

## Mechanical waves

A wave transfers energy, not matter; particles oscillate about fixed positions.

- **Transverse:** vibration ⟂ travel direction (string). **Longitudinal:** vibration ∥ travel direction (sound).
- $$v=f\lambda=\frac\lambda T.$$ The medium sets $v$; the source sets $f$. At a boundary $f$ stays the same.
- Wavelength = distance between adjacent crests (or compressions).
- Interference (superposition) and diffraction are typical wave behaviours; obvious diffraction needs a gap comparable to $\lambda$.

## Worked examples

**Example 1.** A pendulum has period $2$ s. Its length is quadrupled. New period?

*Solution.* $T\propto\sqrt L$: $4$ s.

**Example 2.** A wave has $\lambda=0.6$ m and travels at $3$ m/s. Find $f$ and $T$.

*Solution.* $f=5$ Hz, $T=0.2$ s.

**Example 3.** A $0.5$ kg mass on a spring with $k=50$ N/m. Find $T$.

*Solution.* $T=2\pi\sqrt{0.01}=0.2\pi\approx0.63$ s.

## Common traps

- Thinking a heavier pendulum bob swings more slowly.
- Thinking the wave's particles travel with the wave.
- Changing $f$ when a wave enters a new medium (only $v$ and $\lambda$ change).
"""

N["electrostatics"] = r"""
## Key ideas

- Charge is conserved; like charges repel; $e=1.6\times10^{-19}$ C.
- **Coulomb's law:** $F=k\dfrac{q_1q_2}{r^2}$, $k=9\times10^9\ \text{N}\cdot\text{m}^2/\text{C}^2$.
- **Field strength:** $E=\dfrac Fq$ (N/C or V/m), the force per unit positive charge. Point charge: $E=\dfrac{kQ}{r^2}$. Fields add as vectors.
- Field lines go from $+$ to $-$, never cross, and are denser where $E$ is larger.

## Potential and potential difference

- $U_{AB}=\varphi_A-\varphi_B=\dfrac{W_{AB}}q$ (volts).
- Field lines point from high to low potential.
- Work done by the field $W=qU$ equals the **decrease** in potential energy.
- Uniform field: $E=\dfrac Ud$.
- Accelerating a charge from rest: $qU=\tfrac12mv^2$; $1$ eV $=1.6\times10^{-19}$ J.

## Capacitors

$$C=\frac QU,\qquad C=\frac{\varepsilon S}{4\pi kd}\ (\text{parallel plates}).$$

- Still connected to the battery: $U$ is constant.
- Disconnected: $Q$ is constant (then $E$ does not change when $d$ changes).

## Worked examples

**Example 1.** Two $+2\ \mu\text{C}$ charges are $0.3$ m apart. Find the force.

*Solution.* $F=9\times10^9\cdot\dfrac{4\times10^{-12}}{0.09}=0.4$ N (repulsive).

**Example 2.** $W_{AB}=-4\times10^{-5}$ J for $q=2\times10^{-6}$ C. Find $U_{AB}$.

*Solution.* $U_{AB}=-20$ V, so $B$ is $20$ V higher than $A$.

**Example 3.** Plates $5$ mm apart at $200$ V. Find $E$.

*Solution.* $E=\dfrac{200}{0.005}=4\times10^4$ V/m.

## Common traps

- Signs: a negative charge moving along the field **gains** potential energy.
- $E$ does not depend on the test charge.
- Mixing up "connected to the battery" and "isolated" capacitor problems.
"""

N["dc-circuits"] = r"""
## Key ideas

- Current $I=\dfrac qt$; Ohm's law $I=\dfrac UR$; resistance $R=\rho\dfrac LS$.
- **Series:** same current; $R=R_1+R_2+\dots$; voltages divide in proportion to $R$.
- **Parallel:** same voltage; $\dfrac1R=\dfrac1{R_1}+\dfrac1{R_2}+\dots$ (two resistors: $\dfrac{R_1R_2}{R_1+R_2}$); currents divide in inverse proportion.
- Power $P=UI=I^2R=\dfrac{U^2}R$; energy $W=Pt$ ($1$ kW·h $=3.6\times10^6$ J).

## EMF and internal resistance

$$I=\frac{E}{R+r},\qquad U_{\text{terminal}}=E-Ir.$$

- Larger external $R$ → smaller $I$ → larger terminal voltage.
- Short circuit: $I=E/r$. Open circuit: $U=E$.
- Output power is maximum when $R=r$: $P_{\max}=\dfrac{E^2}{4r}$.

Rated values "$6$ V, $3$ W" give $R=\dfrac{U^2}{P}=12\ \Omega$ and $I=\dfrac PU=0.5$ A.

## Worked examples

**Example 1.** $6\ \Omega$ and $3\ \Omega$ in parallel, in series with $1\ \Omega$, across $9$ V. Find the current.

*Solution.* Parallel $=2\ \Omega$; total $3\ \Omega$; $I=3$ A.

**Example 2.** $E=12$ V, $r=1\ \Omega$, $R=5\ \Omega$. Find $I$ and $U$.

*Solution.* $I=2$ A, $U=10$ V.

**Example 3.** A wire is stretched to $3$ times its length. New resistance?

*Solution.* $L\times3$, $S\div3$, so $R\times9$.

## Common traps

- Assuming the terminal voltage always equals the EMF.
- Adding parallel resistances directly.
- Forgetting that stretching a wire also reduces its cross-section.
"""

N["magnetic-fields"] = r"""
## Key ideas

- Magnetic induction (flux density) $B$, unit tesla (T). Flux $\Phi=BS_\perp$ (weber, Wb).
- Field of a straight current: concentric circles (right-hand grip rule). Solenoid: like a bar magnet.
- Parallel currents attract; antiparallel currents repel.

## Forces

**Ampère force** on a wire: $F=BIL\sin\theta$ (maximum $BIL$ when the wire ⟂ $B$, zero when parallel). Direction: left-hand rule.

**Lorentz force** on a moving charge: $F=qvB\sin\theta$, always ⟂ $v$, so it **does no work** and never changes the speed.

Charged particle moving ⟂ to a uniform field: uniform circular motion with
$$qvB=\frac{mv^2}r\Rightarrow r=\frac{mv}{qB},\qquad T=\frac{2\pi m}{qB}\ (\text{independent of }v).$$

## Worked examples

**Example 1.** A $0.2$ m wire carries $5$ A perpendicular to $0.3$ T. Find the force.

*Solution.* $F=0.3\cdot5\cdot0.2=0.3$ N.

**Example 2.** A proton ($m=1.67\times10^{-27}$ kg) moves at $10^6$ m/s ⟂ to $0.1$ T. Find $r$.

*Solution.* $r=\dfrac{1.67\times10^{-27}\cdot10^6}{1.6\times10^{-19}\cdot0.1}\approx0.10$ m.

**Example 3.** How does the period change if the proton's speed doubles?

*Solution.* $T=\dfrac{2\pi m}{qB}$ is unchanged; the radius doubles.

## Common traps

- Using the right hand instead of the left hand for the force direction.
- For negative charges, reverse the direction given by the left-hand rule.
- Thinking the magnetic force can speed a particle up.
"""

N["em-induction"] = r"""
## Key ideas

An EMF is induced whenever the **magnetic flux through a circuit changes**.

**Faraday's law:** $$E=n\frac{\Delta\Phi}{\Delta t}\qquad(\Phi=BS\text{ for } B\perp S).$$
If $B$ changes: $E=nS\dfrac{\Delta B}{\Delta t}$. **Motional EMF** of a rod cutting field lines: $E=BLv$ ($B$, $L$, $v$ mutually ⟂).

**Lenz's law:** the induced current opposes the **change** that causes it ("come — repel, go — attract"). This is energy conservation: you must do work against the induced force.

Rod on rails: $I=\dfrac{BLv}{R}$, retarding force $F=BIL=\dfrac{B^2L^2v}R$, power $=Fv=\dfrac{E^2}R$.

## Transformers and transmission

Ideal transformer: $\dfrac{U_1}{U_2}=\dfrac{n_1}{n_2}$, $\dfrac{I_1}{I_2}=\dfrac{n_2}{n_1}$, $P_1=P_2$. Transmission loss $P_{\text{loss}}=I^2R_{\text{line}}$ with $I=P/U$, so raising $U$ by a factor $k$ cuts the loss by $k^2$.

## Worked examples

**Example 1.** A $200$-turn coil's flux falls from $0.05$ Wb to $0.01$ Wb in $0.2$ s. Find $E$.

*Solution.* $E=200\cdot\dfrac{0.04}{0.2}=40$ V.

**Example 2.** A $0.4$ m rod moves at $5$ m/s in $0.5$ T; $R=2\ \Omega$. Find $I$.

*Solution.* $E=1$ V, $I=0.5$ A.

**Example 3.** A transformer has $n_1:n_2=10:1$ and $U_1=220$ V. Find $U_2$.

*Solution.* $22$ V.

## Common traps

- A large but **steady** flux induces nothing.
- Lenz's law opposes the **change**, not the field itself.
- Transformers do not work with steady DC.
"""

N["thermodynamics"] = r"""
## Kinetic theory

- Matter is made of molecules in constant random motion (evidence: diffusion, Brownian motion).
- **Temperature** measures the average kinetic energy of the molecules: $T(\text{K})=t(^\circ\text{C})+273$.
- Gas pressure comes from molecules colliding with the walls.
- Internal energy of an **ideal gas** depends only on its temperature.

## Gas laws (fixed mass of ideal gas, kelvin temperatures)

$$\frac{p_1V_1}{T_1}=\frac{p_2V_2}{T_2},\qquad pV=nRT\ (R=8.31\ \text{J/(mol}\cdot\text{K)}).$$

| Process | Law |
|---|---|
| Isothermal | $pV=$ const (Boyle) |
| Isobaric | $V/T=$ const (Charles) |
| Isochoric | $p/T=$ const (Gay-Lussac) |

## First law of thermodynamics

$$\Delta U=Q+W$$
$Q>0$: heat absorbed; $W>0$: work done **on** the gas (compression). Expansion at constant pressure: work by the gas $=p\Delta V$.

- Adiabatic ($Q=0$): compression heats the gas, expansion cools it.
- Isothermal ideal gas: $\Delta U=0$, so $Q=-W$.

**Second law:** heat does not flow spontaneously from cold to hot; no heat engine is 100% efficient.

## Worked examples

**Example 1.** A gas absorbs $300$ J and has $100$ J of work done on it. Find $\Delta U$.

*Solution.* $\Delta U=300+100=400$ J.

**Example 2.** A gas at $27^\circ$C and $2\times10^5$ Pa is heated at constant volume to $127^\circ$C. Find $p$.

*Solution.* $p=2\times10^5\cdot\dfrac{400}{300}\approx2.67\times10^5$ Pa.

**Example 3.** At constant temperature, $p$ falls from $3$ atm to $1$ atm. How does $V$ change?

*Solution.* It triples.

## Common traps

- Using Celsius in gas laws.
- Sign of $W$: work done **by** the gas is negative in $\Delta U=Q+W$.
- Brownian motion is the motion of the particles, not of the molecules themselves.
"""

N["reflection-refraction"] = r"""
## Reflection

Angle of incidence = angle of reflection, both measured from the **normal**. A plane mirror forms an upright, virtual image the same size and as far behind the mirror as the object is in front.

## Refraction

**Snell's law** (from air or vacuum into a medium): $$n=\frac{\sin i}{\sin r}=\frac cv,\qquad n>1.$$

- Into a denser medium the ray bends **toward** the normal; out of it, away from the normal.
- Frequency stays the same; speed and wavelength decrease: $\lambda=\dfrac{\lambda_0}n$.
- Apparent depth (viewing from above) $=\dfrac{\text{real depth}}n$.

## Total internal reflection

Happens when light goes **from a denser to a less dense** medium and the angle of incidence is at least the **critical angle** $C$: $$\sin C=\frac1n.$$
Uses: optical fibres, prisms in binoculars, sparkle of diamonds.

**Dispersion:** $n$ is larger for violet than for red light, so a prism spreads white light; violet bends most.

## Worked examples

**Example 1.** Light enters glass ($n=1.5$) at $i=30^\circ$. Find $\sin r$.

*Solution.* $\sin r=\dfrac{0.5}{1.5}=\dfrac13$.

**Example 2.** Find the critical angle for water ($n=\tfrac43$).

*Solution.* $\sin C=\tfrac34$, $C\approx49^\circ$.

**Example 3.** The speed of light in a medium is $2.25\times10^8$ m/s. Find $n$.

*Solution.* $n=\dfrac{3\times10^8}{2.25\times10^8}=\dfrac43$.

## Common traps

- Measuring angles from the surface instead of the normal.
- Expecting total internal reflection when light goes into a denser medium.
- Thinking the frequency or colour changes in a new medium.
"""

N["interference-diffraction"] = r"""
## Interference

Two **coherent** sources (same frequency, constant phase difference) superpose:

- bright fringe where the path difference $\delta=k\lambda$;
- dark fringe where $\delta=(2k+1)\dfrac\lambda2$.

**Young's double slit:** fringe spacing $$\Delta x=\frac{L}{d}\lambda$$ ($L$ = slit-to-screen distance, $d$ = slit separation). Longer wavelength (red) → wider fringes. The spacing between bright fringe $1$ and bright fringe $n$ is $(n-1)\Delta x$.

**Thin films** (soap bubbles, oil on water, coated lenses): light reflected from the two surfaces interferes, giving colours.

## Diffraction

Waves spread around obstacles and through openings. It is noticeable when the opening or obstacle is comparable to or smaller than the wavelength. Single-slit pattern: a wide, bright central band.

Interference and diffraction show the **wave nature** of light; the photoelectric effect shows its **particle nature** (wave–particle duality).

## Worked examples

**Example 1.** $d=0.2$ mm, $L=1$ m, $\Delta x=3$ mm. Find $\lambda$.

*Solution.* $\lambda=\dfrac{\Delta x\,d}{L}=\dfrac{3\times10^{-3}\cdot2\times10^{-4}}{1}=6\times10^{-7}$ m $=600$ nm.

**Example 2.** The path difference at a point is $2.5\lambda$. Bright or dark?

*Solution.* $2.5\lambda=5\cdot\tfrac\lambda2$ (odd number of half wavelengths): dark.

**Example 3.** The screen is moved twice as far away. What happens to $\Delta x$?

*Solution.* It doubles.

## Common traps

- Dividing by $n$ instead of $n-1$ when counting fringe spacings.
- Thinking that any two light bulbs produce stable interference fringes.
"""

N["photoelectric"] = r"""
## Key ideas

Light energy comes in **photons**: $$E=h\nu=\frac{hc}{\lambda},\qquad h=6.63\times10^{-34}\ \text{J}\cdot\text{s}.$$

**Photoelectric effect:** light ejects electrons from a metal.

- Each electron absorbs one photon.
- Emission happens only if $\nu\ge\nu_0$ (threshold frequency), however intense the light.
- **Einstein's equation:** $$E_{k\max}=h\nu-W_0,\qquad W_0=h\nu_0.$$
- Higher frequency → larger $E_{k\max}$; greater intensity → more electrons (larger current), same $E_{k\max}$.
- Stopping voltage: $eU_c=E_{k\max}$.
- Emission is practically instantaneous.

Units: $1\ \text{eV}=1.6\times10^{-19}$ J.

## Worked examples

**Example 1.** Find the energy of a photon with $\nu=6\times10^{14}$ Hz.

*Solution.* $E=6.63\times10^{-34}\cdot6\times10^{14}\approx4.0\times10^{-19}$ J $\approx2.5$ eV.

**Example 2.** $W_0=2.3$ eV and photons have $3.0$ eV. Find $E_{k\max}$ and $U_c$.

*Solution.* $E_{k\max}=0.7$ eV, $U_c=0.7$ V.

**Example 3.** Which light ejects electrons from a metal with $\nu_0=5\times10^{14}$ Hz: bright red ($4\times10^{14}$ Hz) or dim violet ($7.5\times10^{14}$ Hz)?

*Solution.* Only the violet light — frequency matters, not brightness.

## Common traps

- Believing brighter light gives faster electrons.
- Forgetting to convert between eV and J.
"""

N["atomic-structure"] = r"""
## Models of the atom

- **Rutherford's $\alpha$-scattering:** most $\alpha$ particles pass straight through, a few are deflected strongly, very few bounce back ⇒ a tiny, dense, positive **nucleus** with electrons around it.
- **Bohr model of hydrogen:** electrons occupy only certain orbits (energy levels) and do not radiate while in them.

## Energy levels and spectra

Hydrogen: $$E_n=\frac{-13.6\ \text{eV}}{n^2}\quad(E_1=-13.6,\ E_2=-3.4,\ E_3=-1.51,\ E_4=-0.85\ \text{eV}).$$

- Jumping **down** from $m$ to $n$ emits a photon $h\nu=E_m-E_n$; absorbing a photon of exactly that energy moves it up.
- Ionisation energy from level $n$: $0-E_n$ (from the ground state: $13.6$ eV).
- From level $n$ the number of possible spectral lines is $C_n^2=\dfrac{n(n-1)}2$.
- Line spectra are evidence of **discrete** energy levels; each element has its own "fingerprint" spectrum.

## Worked examples

**Example 1.** Find the photon energy for $n=4\to n=2$.

*Solution.* $-0.85-(-3.4)=2.55$ eV.

**Example 2.** How many lines can atoms excited to $n=3$ emit?

*Solution.* $C_3^2=3$.

**Example 3.** Can a ground-state hydrogen atom absorb a $12.0$ eV photon?

*Solution.* $E_2-E_1=10.2$ eV, $E_3-E_1=12.09$ eV — no exact match and below $13.6$ eV, so no.

## Common traps

- Dividing by $n$ instead of $n^2$.
- Thinking an atom can absorb any photon energy (only exact level differences, or enough to ionise).
"""

N["nuclear"] = r"""
## Nuclear structure

$^A_Z\text{X}$: $Z$ = proton number (atomic number), $A$ = mass number = protons + neutrons; neutrons $N=A-Z$. **Isotopes** have the same $Z$ and different $A$.

## Radioactive decay

| Decay | Emitted | Change |
|---|---|---|
| $\alpha$ | $^4_2\text{He}$ | $A-4$, $Z-2$ |
| $\beta^-$ | $^0_{-1}e$ | $A$ unchanged, $Z+1$ (a neutron becomes a proton) |
| $\gamma$ | photon | no change in $A$ or $Z$ |

Penetration: $\alpha$ (stopped by paper) < $\beta$ (aluminium) < $\gamma$ (thick lead). Ionising power is the reverse.

**Half-life** $T_{1/2}$: the time for half of the nuclei to decay. Remaining $N=N_0\left(\tfrac12\right)^{t/T_{1/2}}$. It is not affected by temperature, pressure or chemical state.

## Nuclear reactions and energy

Nuclear equations conserve **mass number** and **charge number**. Mass–energy: $\Delta E=\Delta mc^2$ ($1$ u ↔ $931.5$ MeV).

- **Fission:** a heavy nucleus ($^{235}$U) splits after absorbing a neutron, releasing energy and more neutrons (chain reaction — nuclear power).
- **Fusion:** light nuclei combine (e.g. $^2_1\text{H}+{}^3_1\text{H}\to{}^4_2\text{He}+{}^1_0n$) — powers the Sun.

## Worked examples

**Example 1.** $^{232}_{90}\text{Th}$ becomes $^{208}_{82}\text{Pb}$. How many $\alpha$ and $\beta$ decays?

*Solution.* $\alpha$: $\dfrac{232-208}{4}=6$ (Z falls by $12$ to $78$); $\beta$: $82-78=4$.

**Example 2.** $80$ g of a nuclide with $T_{1/2}=3$ d. How much remains after $9$ d?

*Solution.* $3$ half-lives: $10$ g.

**Example 3.** A reaction loses $2\times10^{-30}$ kg of mass. Energy released?

*Solution.* $2\times10^{-30}\cdot9\times10^{16}=1.8\times10^{-13}$ J.

## Common traps

- In $\beta^-$ decay the mass number does **not** change.
- Thinking a sample is gone after two half-lives (a quarter remains).
"""

for k, v in N.items():
    (OUT / f"{k}.md").write_text(v.strip() + "\n", encoding="utf8")
    print("wrote", k)
