from qb import *  # noqa: F403

B = Bank("physics", "mechanics")
g = 10
G10 = r"(take $g=10\ \text{m/s}^2$)"
Gc = 6.67e-11

# ------------------------------------------------------------ momentum
B.q("p-mom-01", "momentum", 1,
    r"The momentum of a $2$ kg ball moving at $3$ m/s is",
    [r"$6\ \text{kg}\cdot\text{m/s}$", r"$9\ \text{kg}\cdot\text{m/s}$", r"$1.5\ \text{kg}\cdot\text{m/s}$", r"$18\ \text{kg}\cdot\text{m/s}$"],
    r"$p=mv=2\times3=6\ \text{kg}\cdot\text{m/s}$. ($9$ J would be the kinetic energy $\tfrac12mv^2$.)",
    R(2 * 3))

B.q("p-mom-02", "momentum", 1,
    r"A constant force of $5$ N acts on an object for $4$ s. The impulse of the force is",
    [r"$20\ \text{N}\cdot\text{s}$", r"$1.25\ \text{N}\cdot\text{s}$", r"$9\ \text{N}\cdot\text{s}$", r"$80\ \text{N}\cdot\text{s}$"],
    r"$I=Ft=5\times4=20\ \text{N}\cdot\text{s}$.",
    R(5 * 4))

B.q("p-mom-03", "momentum", 2,
    r"A $0.5$ kg ball hits a wall at $6$ m/s and rebounds along the same line at $4$ m/s. The magnitude of the change in its momentum is",
    [r"$5\ \text{kg}\cdot\text{m/s}$", r"$1\ \text{kg}\cdot\text{m/s}$", r"$2\ \text{kg}\cdot\text{m/s}$", r"$3\ \text{kg}\cdot\text{m/s}$"],
    r"Take the rebound direction as positive: $\Delta p=0.5\times4-0.5\times(-6)=2+3=5\ \text{kg}\cdot\text{m/s}$. Forgetting that velocity reverses gives $1$.",
    R(abs(0.5 * 4 - 0.5 * (-6))))

B.q("p-mom-04", "momentum", 2,
    r"A $2$ kg cart moving at $3$ m/s collides with a stationary $1$ kg cart and they stick together. Their common speed is",
    [r"$2$ m/s", r"$3$ m/s", r"$1.5$ m/s", r"$1$ m/s"],
    r"Momentum is conserved: $2\times3=(2+1)v\Rightarrow v=2$ m/s.",
    R(sp.Rational(2 * 3, 3)))

B.q("p-mom-05", "momentum", 3,
    r"In the collision above ($2$ kg at $3$ m/s sticking to a stationary $1$ kg cart), the kinetic energy lost is",
    [r"$3$ J", r"$9$ J", r"$6$ J", r"$0$ J"],
    r"Before: $\tfrac12\times2\times9=9$ J. After: $\tfrac12\times3\times2^2=6$ J. Lost: $3$ J — a perfectly inelastic collision always loses kinetic energy.",
    R(sp.Rational(1, 2) * 2 * 9 - sp.Rational(1, 2) * 3 * 2 ** 2))

B.q("p-mom-06", "momentum", 2,
    r"A $60$ kg person standing on smooth ice throws a $2$ kg ball horizontally at $15$ m/s. The person's recoil speed is",
    [r"$0.5$ m/s", r"$15$ m/s", r"$2$ m/s", r"$0.25$ m/s"],
    r"Initial momentum is zero, so $60v=2\times15\Rightarrow v=0.5$ m/s, in the opposite direction.",
    R(2 * 15 / 60))

B.q("p-mom-07", "momentum", 1,
    r"An egg dropped onto a cushion is less likely to break than one dropped onto a stone floor because the cushion",
    [r"increases the time of impact, reducing the force", r"reduces the change in momentum", r"reduces the impulse", r"increases the egg's momentum"],
    r"The change in momentum (and so the impulse) is the same either way. The cushion stretches the stopping time, so $F=\dfrac{\Delta p}{\Delta t}$ is smaller.")

B.q("p-mom-08", "momentum", 2,
    r"A $1000$ kg car's speed increases from $10$ m/s to $20$ m/s in $5$ s. The average net force on it is",
    [r"$2000$ N", r"$4000$ N", r"$1000$ N", r"$10000$ N"],
    r"Impulse–momentum theorem: $F\Delta t=\Delta p=1000\times(20-10)$, so $F=\dfrac{10000}{5}=2000$ N.",
    R(1000 * (20 - 10) / 5))

_v1, _v2 = sp.symbols("v1 v2")
_sol9 = [s_ for s_ in sp.solve([1 * 4 - (1 * _v1 + 1 * _v2), sp.Rational(1, 2) * 16 - (sp.Rational(1, 2) * _v1 ** 2 + sp.Rational(1, 2) * _v2 ** 2)], [_v1, _v2], dict=True) if s_[_v2] != 0][0]
B.q("p-mom-09", "momentum", 3,
    r"A ball of mass $m$ moving at $4$ m/s makes a perfectly **elastic** head-on collision with an identical stationary ball. Afterwards the first ball's speed is",
    [r"$0$ m/s", r"$2$ m/s", r"$4$ m/s", r"$1$ m/s"],
    r"Conserving momentum and kinetic energy for equal masses gives an exchange of velocities: the first ball stops ($0$ m/s) and the second moves off at $4$ m/s.",
    N(abs(_sol9[_v1]), abs_tol=1e-9))

B.q("p-mom-10", "momentum", 2,
    r"Momentum of a system is conserved when",
    [r"the net external force on the system is zero", r"there is no friction inside the system", r"kinetic energy is conserved", r"the objects do not touch"],
    r"Conservation of momentum requires zero net **external** force. Internal forces (including friction between parts of the system) cannot change the total momentum. Kinetic energy may or may not be conserved.")

B.q("p-mom-11", "momentum", 2,
    r"A $0.2$ kg ball falls from rest for $2$ s " + G10 + r". The impulse of gravity on the ball during this time is",
    [r"$4\ \text{N}\cdot\text{s}$", r"$2\ \text{N}\cdot\text{s}$", r"$0.4\ \text{N}\cdot\text{s}$", r"$40\ \text{N}\cdot\text{s}$"],
    r"$I=mgt=0.2\times10\times2=4\ \text{N}\cdot\text{s}$, equal to the momentum gained: $0.2\times20=4\ \text{kg}\cdot\text{m/s}$.",
    R(0.2 * g * 2))

B.q("p-mom-12", "momentum", 3,
    r"A $3$ kg object at rest explodes into two pieces. A $1$ kg piece flies off at $8$ m/s. The speed of the other piece is",
    [r"$4$ m/s", r"$8$ m/s", r"$16$ m/s", r"$2.67$ m/s"],
    r"Total momentum stays zero: $1\times8=2\times v\Rightarrow v=4$ m/s in the opposite direction. (The other piece has mass $3-1=2$ kg, not $3$ kg.)",
    R(1 * 8 / (3 - 1)))

# ------------------------------------------------------------ work & energy
B.q("p-ene-01", "work-energy", 2,
    r"A force of $10$ N pulls a box $5$ m along the floor. The force makes an angle of $60^\circ$ with the displacement. The work done by the force is",
    [r"$25$ J", r"$50$ J", r"$43.3$ J", r"$2$ J"],
    r"$W=Fs\cos\theta=10\times5\times\cos60^\circ=25$ J.",
    R(10 * 5 * sp.cos(sp.pi / 3)))

B.q("p-ene-02", "work-energy", 1,
    r"The kinetic energy of a $4$ kg object moving at $5$ m/s is",
    [r"$50$ J", r"$100$ J", r"$20$ J", r"$10$ J"],
    r"$E_k=\tfrac12mv^2=\tfrac12\times4\times25=50$ J.",
    R(sp.Rational(1, 2) * 4 * 25))

B.q("p-ene-03", "work-energy", 1,
    r"A $2$ kg object is lifted $3$ m vertically at constant speed " + G10 + r". The increase in its gravitational potential energy is",
    [r"$60$ J", r"$6$ J", r"$30$ J", r"$600$ J"],
    r"$\Delta E_p=mgh=2\times10\times3=60$ J.",
    R(2 * g * 3))

B.q("p-ene-04", "work-energy", 2,
    r"A ball is released from rest and slides down a smooth curved track, dropping a vertical height of $5$ m " + G10 + r". Its speed at the bottom is",
    [r"$10$ m/s", r"$5$ m/s", r"$50$ m/s", r"$100$ m/s"],
    r"No friction, so mechanical energy is conserved: $mgh=\tfrac12mv^2\Rightarrow v=\sqrt{2gh}=\sqrt{100}=10$ m/s. The shape of the track does not matter.",
    R(sp.sqrt(2 * g * 5)))

B.q("p-ene-05", "work-energy", 2,
    r"A motor lifts a $50$ kg load through $12$ m in $10$ s at constant speed " + G10 + r". The power output of the motor is",
    [r"$600$ W", r"$6000$ W", r"$60$ W", r"$500$ W"],
    r"Work $=mgh=50\times10\times12=6000$ J; power $P=\dfrac Wt=\dfrac{6000}{10}=600$ W.",
    R(50 * g * 12 / 10))

B.q("p-ene-06", "work-energy", 2,
    r"A car's engine delivers a constant power of $60$ kW. When the car moves at $20$ m/s, the driving force is",
    [r"$3000$ N", r"$1200$ N", r"$300$ N", r"$12000$ N"],
    r"$P=Fv\Rightarrow F=\dfrac{60000}{20}=3000$ N.",
    R(60000 / 20))

B.q("p-ene-07", "work-energy", 3,
    r"A $2$ kg block sliding at $6$ m/s on a rough horizontal floor stops after $9$ m. The friction force is",
    [r"$4$ N", r"$2$ N", r"$36$ N", r"$8$ N"],
    r"Work–energy theorem: $-f\cdot9=0-\tfrac12\times2\times36=-36$ J, so $f=4$ N.",
    R(sp.Rational(1, 2) * 2 * 36 / 9))

B.q("p-ene-08", "work-energy", 3,
    r"A $1$ kg ball is thrown upward from the ground at $20$ m/s and reaches a maximum height of $16$ m " + G10 + r". The work done against air resistance on the way up is",
    [r"$40$ J", r"$160$ J", r"$200$ J", r"$0$ J"],
    r"Initial kinetic energy $=\tfrac12\times1\times400=200$ J. At the top it has potential energy $mgh=160$ J. The missing $40$ J was done against air resistance.",
    R(sp.Rational(1, 2) * 1 * 400 - 1 * g * 16))

B.q("p-ene-09", "work-energy", 1,
    r"A satellite moves in a circular orbit around the Earth. The work done by gravity on it during one revolution is",
    [r"zero, because gravity is perpendicular to the velocity", r"positive", r"negative", r"equal to its kinetic energy"],
    r"In a circular orbit the gravitational force always points to the centre, perpendicular to the velocity, so $W=Fs\cos90^\circ=0$ at every instant. The speed stays constant.")

B.q("p-ene-10", "work-energy", 2,
    r"A spring with spring constant $200$ N/m is compressed by $0.1$ m. The elastic potential energy stored is",
    [r"$1$ J", r"$2$ J", r"$20$ J", r"$10$ J"],
    r"$E_p=\tfrac12kx^2=\tfrac12\times200\times0.01=1$ J.",
    R(sp.Rational(1, 2) * 200 * sp.Rational(1, 100)))

B.q("p-ene-11", "work-energy", 2,
    r"A pendulum bob is released from rest $0.45$ m above its lowest point " + G10 + r". Its speed at the lowest point is",
    [r"$3$ m/s", r"$4.5$ m/s", r"$9$ m/s", r"$0.3$ m/s"],
    r"$\tfrac12mv^2=mgh\Rightarrow v=\sqrt{2\times10\times0.45}=\sqrt9=3$ m/s. The string tension does no work (it is perpendicular to the motion).",
    R(sp.sqrt(2 * g * sp.Rational(45, 100))))

B.q("p-ene-12", "work-energy", 1,
    r"Which quantity is a scalar?",
    [r"Work", r"Momentum", r"Force", r"Displacement"],
    r"Work $W=\vec F\cdot\vec s$ is a dot product, so it has magnitude (and sign) but no direction. Momentum, force and displacement are vectors.")

B.q("p-ene-13", "work-energy", 3,
    r"A $1500$ kg car has maximum engine power $60$ kW and the total resistance is a constant $2000$ N. Its maximum speed on a level road is",
    [r"$30$ m/s", r"$40$ m/s", r"$20$ m/s", r"$60$ m/s"],
    r"At maximum speed the acceleration is zero, so the driving force equals the resistance: $F=2000$ N. $v_{\max}=\dfrac{P}{F}=\dfrac{60000}{2000}=30$ m/s.",
    R(60000 / 2000))

B.q("p-ene-14", "work-energy", 3,
    r"A $2$ kg block is released from rest at the top of a $5$ m high, $10$ m long incline and reaches the bottom at $8$ m/s " + G10 + r". The work done by friction is",
    [r"$-36$ J", r"$-64$ J", r"$-100$ J", r"$36$ J"],
    r"$W_g+W_f=\Delta E_k$: $2\times10\times5+W_f=\tfrac12\times2\times64$, so $W_f=64-100=-36$ J (negative because friction opposes motion).",
    R(sp.Rational(1, 2) * 2 * 64 - 2 * g * 5))

# --------------------------------------------- circular motion & gravitation
B.q("p-cir-01", "circular-gravitation", 2,
    r"An object moves in a circle of radius $2$ m at a constant speed of $4$ m/s. Its centripetal acceleration is",
    [r"$8\ \text{m/s}^2$", r"$2\ \text{m/s}^2$", r"$16\ \text{m/s}^2$", r"$0$"],
    r"$a=\dfrac{v^2}{r}=\dfrac{16}{2}=8\ \text{m/s}^2$, directed toward the centre. The speed is constant but the velocity's direction changes, so $a\ne0$.",
    R(sp.Rational(16, 2)))

B.q("p-cir-02", "circular-gravitation", 1,
    r"A wheel turns at $2$ revolutions per second. Its angular velocity is",
    [r"$4\pi$ rad/s", r"$2\pi$ rad/s", r"$2$ rad/s", r"$\pi$ rad/s"],
    r"$\omega=2\pi n=2\pi\times2=4\pi$ rad/s.",
    R(2 * sp.pi * 2))

B.q("p-cir-03", "circular-gravitation", 2,
    r"A $0.5$ kg ball on a string moves in a horizontal circle of radius $0.4$ m on a smooth table at $2$ m/s. The tension in the string is",
    [r"$5$ N", r"$2.5$ N", r"$10$ N", r"$1.25$ N"],
    r"The tension provides the centripetal force: $T=\dfrac{mv^2}{r}=\dfrac{0.5\times4}{0.4}=5$ N.",
    R(0.5 * 4 / 0.4))

B.q("p-cir-04", "circular-gravitation", 3,
    r"A car of mass $1000$ kg drives over the top of a hump of radius $40$ m at $10$ m/s " + G10 + r". The normal force from the road at the top is",
    [r"$7500$ N", r"$10000$ N", r"$12500$ N", r"$2500$ N"],
    r"At the top the net force points down to the centre: $mg-N=\dfrac{mv^2}{r}$, so $N=1000\left(10-\dfrac{100}{40}\right)=7500$ N. The car feels lighter.",
    R(1000 * (g - 100 / 40)))

B.q("p-cir-05", "circular-gravitation", 3,
    r"A small ball on a string of length $0.4$ m moves in a vertical circle " + G10 + r". The minimum speed at the top for the string to stay taut is",
    [r"$2$ m/s", r"$0$ m/s", r"$4$ m/s", r"$\sqrt2$ m/s"],
    r"At the minimum speed the tension is zero and gravity alone gives the centripetal force: $mg=\dfrac{mv^2}r\Rightarrow v=\sqrt{gr}=\sqrt{4}=2$ m/s.",
    R(sp.sqrt(g * sp.Rational(4, 10))))

B.q("p-cir-06", "circular-gravitation", 1,
    r"If the distance between two point masses is doubled, the gravitational force between them becomes",
    [r"one quarter of the original", r"half of the original", r"twice the original", r"four times the original"],
    r"$F=\dfrac{Gm_1m_2}{r^2}$: doubling $r$ divides $F$ by $2^2=4$.")

B.q("p-cir-07", "circular-gravitation", 2,
    r"For satellites in circular orbits around the Earth, a satellite in a **higher** orbit has",
    [r"a smaller speed and a longer period", r"a larger speed and a longer period", r"a smaller speed and a shorter period", r"the same speed"],
    r"$\dfrac{GMm}{r^2}=\dfrac{mv^2}{r}\Rightarrow v=\sqrt{\dfrac{GM}{r}}$, which decreases as $r$ increases, while $T=2\pi\sqrt{\dfrac{r^3}{GM}}$ increases.")

B.q("p-cir-08", "circular-gravitation", 2,
    r"Two satellites orbit the Earth in circles of radii $r$ and $4r$. The ratio of their speeds $v_1:v_2$ is",
    [r"$2:1$", r"$4:1$", r"$1:2$", r"$16:1$"],
    r"$v=\sqrt{GM/r}$, so $\dfrac{v_1}{v_2}=\sqrt{\dfrac{4r}{r}}=2$. Ratio $2:1$.",
    T(f"{sp.sqrt(sp.Rational(4, 1))}:1"))

B.q("p-cir-09", "circular-gravitation", 2,
    r"The acceleration due to gravity at the Earth's surface is $g$. At a height equal to the Earth's radius $R$ above the surface it is",
    [r"$\dfrac g4$", r"$\dfrac g2$", r"$g$", r"$2g$"],
    r"$g\propto\dfrac1{r^2}$ and the distance from the centre doubles ($R\to2R$), so $g'=\dfrac g4$.")

B.q("p-cir-10", "circular-gravitation", 1,
    r"The first cosmic velocity (minimum launch speed for a circular orbit just above the Earth's surface) is about",
    [r"$7.9$ km/s", r"$11.2$ km/s", r"$16.7$ km/s", r"$340$ m/s"],
    r"$v_1=\sqrt{gR}\approx\sqrt{9.8\times6.4\times10^6}\approx7.9$ km/s. $11.2$ km/s is the escape velocity and $16.7$ km/s the third cosmic velocity.",
    Num(sp.sqrt(9.8 * 6.4e6) / 1000, rel=0.01))

_M = 6.0e24
_R = 6.4e6
B.q("p-cir-11", "circular-gravitation", 3,
    r"Using $G=6.67\times10^{-11}\ \text{N}\cdot\text{m}^2/\text{kg}^2$, Earth mass $M=6.0\times10^{24}$ kg and radius $R=6.4\times10^6$ m, the gravitational acceleration at the Earth's surface is closest to",
    [r"$9.8\ \text{m/s}^2$", r"$6.3\ \text{m/s}^2$", r"$62\ \text{m/s}^2$", r"$1.0\ \text{m/s}^2$"],
    r"$g=\dfrac{GM}{R^2}=\dfrac{6.67\times10^{-11}\times6.0\times10^{24}}{(6.4\times10^6)^2}=\dfrac{4.0\times10^{14}}{4.1\times10^{13}}\approx9.8\ \text{m/s}^2$.",
    R(Gc * _M / _R ** 2, rel=0.01))

B.q("p-cir-12", "circular-gravitation", 2,
    r"A geostationary satellite has",
    [r"a period of 24 hours and an orbit above the equator", r"any orbit with a period of 24 hours", r"a period of 1 hour", r"an orbit over the poles"],
    r"To stay above the same point, the satellite must turn with the Earth (period $\approx24$ h) in the equatorial plane, which fixes its height too.")

B.q("p-cir-13", "circular-gravitation", 2,
    r"Two points $A$ and $B$ are on a rotating disc at distances $0.1$ m and $0.3$ m from the axis. The ratio of their linear speeds $v_A:v_B$ is",
    [r"$1:3$", r"$3:1$", r"$1:1$", r"$1:9$"],
    r"Points on the same rigid disc have the same angular velocity $\omega$, and $v=\omega r$, so $v_A:v_B=0.1:0.3=1:3$.",
    T(f"{(sp.Rational(1, 10) / sp.Rational(3, 10)).p}:{(sp.Rational(1, 10) / sp.Rational(3, 10)).q}"))

B.q("p-cir-14", "circular-gravitation", 3,
    r"A planet has twice the Earth's mass and twice its radius. If the gravitational acceleration on Earth is $10\ \text{m/s}^2$, on the planet it is",
    [r"$5\ \text{m/s}^2$", r"$10\ \text{m/s}^2$", r"$20\ \text{m/s}^2$", r"$2.5\ \text{m/s}^2$"],
    r"$g=\dfrac{GM}{R^2}$: $g'=\dfrac{G(2M)}{(2R)^2}=\dfrac{2}{4}g=5\ \text{m/s}^2$.",
    R(10 * 2 / 2 ** 2))

# ----------------------------------------------------- SHM & mechanical waves
B.q("p-wav-01", "shm-waves", 1,
    r"A wave has frequency $50$ Hz and wavelength $2$ m. Its speed is",
    [r"$100$ m/s", r"$25$ m/s", r"$52$ m/s", r"$0.04$ m/s"],
    r"$v=f\lambda=50\times2=100$ m/s.",
    R(50 * 2))

B.q("p-wav-02", "shm-waves", 1,
    r"A simple pendulum makes $20$ complete oscillations in $40$ s. Its period is",
    [r"$2$ s", r"$0.5$ s", r"$20$ s", r"$800$ s"],
    r"$T=\dfrac{\text{time}}{\text{number of oscillations}}=\dfrac{40}{20}=2$ s.",
    R(40 / 20))

B.q("p-wav-03", "shm-waves", 2,
    r"The period of a simple pendulum is $T$. If its length is made $4$ times as long, the period becomes",
    [r"$2T$", r"$4T$", r"$\dfrac T2$", r"$16T$"],
    r"$T=2\pi\sqrt{\dfrac Lg}\propto\sqrt L$, so $T'=\sqrt4\,T=2T$. The mass of the bob does not matter.")

B.q("p-wav-04", "shm-waves", 2,
    r"A mass of $0.4$ kg on a spring of constant $40$ N/m oscillates. Its period is",
    [r"$\dfrac{\pi}{5}$ s", r"$\dfrac{\pi}{10}$ s", r"$2\pi$ s", r"$0.1$ s"],
    r"$T=2\pi\sqrt{\dfrac mk}=2\pi\sqrt{\dfrac{0.4}{40}}=2\pi\times0.1=\dfrac\pi5\approx0.63$ s.",
    N(2 * sp.pi * sp.sqrt(sp.Rational(4, 10) / 40)))

B.q("p-wav-05", "shm-waves", 1,
    r"In simple harmonic motion, the speed of the oscillating object is greatest",
    [r"at the equilibrium position", r"at maximum displacement", r"halfway between equilibrium and maximum displacement", r"it is the same everywhere"],
    r"At the equilibrium position all the energy is kinetic, so the speed is maximum (and the restoring force and acceleration are zero). At maximum displacement the speed is zero.")

B.q("p-wav-06", "shm-waves", 1,
    r"In a transverse wave, the particles of the medium vibrate",
    [r"perpendicular to the direction the wave travels", r"parallel to the direction the wave travels", r"in circles", r"they move along with the wave"],
    r"Transverse: vibration ⟂ propagation (e.g. waves on a string). Longitudinal (e.g. sound): vibration ∥ propagation. In both cases the particles oscillate about fixed positions; only energy travels.")

B.q("p-wav-07", "shm-waves", 2,
    r"Sound travels at $340$ m/s in air. A tuning fork of frequency $680$ Hz produces sound of wavelength",
    [r"$0.5$ m", r"$2$ m", r"$1020$ m", r"$0.25$ m"],
    r"$\lambda=\dfrac vf=\dfrac{340}{680}=0.5$ m.",
    R(340 / 680))

B.q("p-wav-08", "shm-waves", 2,
    r"An object performs SHM described by $x=0.05\sin(4\pi t)$ (SI units). Its amplitude and frequency are",
    [r"$0.05$ m and $2$ Hz", r"$0.05$ m and $4$ Hz", r"$0.1$ m and $2$ Hz", r"$0.05$ m and $4\pi$ Hz"],
    r"Compare with $x=A\sin(\omega t)$: $A=0.05$ m and $\omega=4\pi$ rad/s, so $f=\dfrac{\omega}{2\pi}=2$ Hz.",
    Nums(0.05, 4 * sp.pi / (2 * sp.pi)))

B.q("p-wav-09", "shm-waves", 3,
    r"A wave travels along a string at $4$ m/s. Two adjacent crests are $0.8$ m apart. The time for a particle on the string to make one full oscillation is",
    [r"$0.2$ s", r"$5$ s", r"$3.2$ s", r"$0.4$ s"],
    r"Adjacent crests are one wavelength apart: $\lambda=0.8$ m. $f=\dfrac v\lambda=5$ Hz, so the period is $T=\dfrac1f=0.2$ s.",
    R(0.8 / 4))

B.q("p-wav-10", "shm-waves", 2,
    r"When a wave passes from one medium into another, the quantity that stays the same is the",
    [r"frequency", r"wavelength", r"speed", r"amplitude only"],
    r"The frequency is set by the source, so it does not change at a boundary. The speed changes with the medium, and so does $\lambda=v/f$.")

B.q("p-wav-11", "shm-waves", 1,
    r"Resonance occurs when",
    [r"the driving frequency equals the natural frequency of the system", r"the amplitude is zero", r"two waves cancel", r"the driving force is removed"],
    r"A system driven at its natural frequency absorbs energy most efficiently, so its amplitude becomes very large. This is resonance.")

B.q("p-wav-12", "shm-waves", 3,
    r"A spring oscillator has amplitude $0.1$ m and maximum speed $2$ m/s. Its angular frequency is",
    [r"$20$ rad/s", r"$0.2$ rad/s", r"$2$ rad/s", r"$10$ rad/s"],
    r"In SHM $v_{\max}=A\omega$, so $\omega=\dfrac{2}{0.1}=20$ rad/s.",
    R(2 / 0.1))
