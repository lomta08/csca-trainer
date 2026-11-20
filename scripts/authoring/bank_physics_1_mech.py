from qb import *  # noqa: F403

B = Bank("physics", "mechanics")
g = 10
G10 = r"(take $g=10\ \text{m/s}^2$)"

# ------------------------------------------------------------ kinematics
B.q("p-kin-01", "kinematics", 1,
    r"A car starts from rest and accelerates uniformly at $2\ \text{m/s}^2$. Its speed after $5$ s is",
    [r"$10$ m/s", r"$25$ m/s", r"$5$ m/s", r"$2.5$ m/s"],
    r"$v=v_0+at=0+2\times5=10$ m/s.",
    R(0 + 2 * 5))

B.q("p-kin-02", "kinematics", 2,
    r"A car starts from rest with constant acceleration $2\ \text{m/s}^2$. The distance it travels in the first $5$ s is",
    [r"$25$ m", r"$50$ m", r"$10$ m", r"$12.5$ m"],
    r"$x=v_0t+\tfrac12at^2=0+\tfrac12\times2\times5^2=25$ m.",
    R(sp.Rational(1, 2) * 2 * 5 ** 2))

B.q("p-kin-03", "kinematics", 1,
    r"A stone is dropped from rest and falls freely for $3$ s " + G10 + r". The distance fallen is",
    [r"$45$ m", r"$30$ m", r"$90$ m", r"$15$ m"],
    r"$h=\tfrac12gt^2=\tfrac12\times10\times9=45$ m.",
    R(sp.Rational(1, 2) * g * 3 ** 2))

B.q("p-kin-04", "kinematics", 1,
    r"A ball is thrown vertically upward at $20$ m/s " + G10 + r". The maximum height it reaches is",
    [r"$20$ m", r"$40$ m", r"$10$ m", r"$2$ m"],
    r"At the top $v=0$: $v_0^2=2gh\Rightarrow h=\dfrac{v_0^2}{2g}=\dfrac{400}{20}=20$ m.",
    R(20 ** 2 / (2 * g)))

B.q("p-kin-05", "kinematics", 2,
    r"A car moving at $20$ m/s brakes with a deceleration of $5\ \text{m/s}^2$. The distance it travels in the $6$ s after braking starts is",
    [r"$40$ m", r"$30$ m", r"$210$ m", r"$120$ m"],
    r"""The car stops after $t=\dfrac{20}{5}=4$ s, so it does **not** move during the last $2$ s.

Stopping distance: $\dfrac{v_0^2}{2a}=\dfrac{400}{10}=40$ m. (Using $t=6$ s in $x=v_0t-\tfrac12at^2$ gives $30$ m — the classic trap.)""",
    R(20 ** 2 / (2 * 5) if 20 / 5 < 6 else 20 * 6 - 2.5 * 36))

B.q("p-kin-06", "kinematics", 2,
    r"An object moves $30$ m east and then $40$ m north in $10$ s. The magnitude of its average velocity is",
    [r"$5$ m/s", r"$7$ m/s", r"$1$ m/s", r"$3.5$ m/s"],
    r"Average velocity $=\dfrac{\text{displacement}}{\text{time}}$. Displacement $=\sqrt{30^2+40^2}=50$ m, so $\bar v=5$ m/s. ($7$ m/s is the average **speed**, from the path length $70$ m.)",
    R(sp.sqrt(30 ** 2 + 40 ** 2) / 10))

B.q("p-kin-07", "kinematics", 2,
    r"An object accelerates uniformly from $2$ m/s to $10$ m/s over a distance of $24$ m. Its acceleration is",
    [r"$2\ \text{m/s}^2$", r"$4\ \text{m/s}^2$", r"$1\ \text{m/s}^2$", r"$3\ \text{m/s}^2$"],
    r"$v^2-v_0^2=2ax\Rightarrow a=\dfrac{100-4}{2\times24}=2\ \text{m/s}^2$.",
    R((10 ** 2 - 2 ** 2) / (2 * 24)))

B.q("p-kin-08", "kinematics", 3,
    r"A ball is thrown horizontally at $10$ m/s from a height of $20$ m " + G10 + r". The horizontal distance it travels before hitting the ground is",
    [r"$20$ m", r"$10$ m", r"$40$ m", r"$200$ m"],
    r"Vertical motion is free fall: $20=\tfrac12\cdot10\,t^2\Rightarrow t=2$ s. Horizontal motion is uniform: $x=v_0t=10\times2=20$ m.",
    R(10 * sp.sqrt(2 * 20 / g)))

B.q("p-kin-09", "kinematics", 2,
    r"For the projectile in the previous situation (thrown horizontally at $10$ m/s from $20$ m, $g=10\ \text{m/s}^2$), the speed when it hits the ground is",
    [r"$10\sqrt5$ m/s", r"$30$ m/s", r"$20$ m/s", r"$10$ m/s"],
    r"After $t=2$ s: $v_y=gt=20$ m/s, $v_x=10$ m/s. $v=\sqrt{10^2+20^2}=10\sqrt5\approx22.4$ m/s. Speeds add as vectors, not as numbers.",
    R(sp.sqrt(10 ** 2 + (g * sp.sqrt(2 * 20 / g)) ** 2)))

B.q("p-kin-10", "kinematics", 1,
    r"On a velocity–time graph, the area between the graph and the time axis represents",
    [r"displacement", r"acceleration", r"velocity", r"force"],
    r"Displacement $=\int v\,dt$, which is the area under the $v$–$t$ graph. The **slope** of the $v$–$t$ graph is the acceleration.")

B.q("p-kin-11", "kinematics", 2,
    r"An object starting from rest moves with uniform acceleration. The ratio of the distances covered in the 1st, 2nd and 3rd seconds is",
    [r"$1:3:5$", r"$1:2:3$", r"$1:4:9$", r"$1:1:1$"],
    r"Total distances after $1,2,3$ s are proportional to $1,4,9$ (since $x\propto t^2$). Distances **in each** second: $1,\ 4-1=3,\ 9-4=5$, ratio $1:3:5$.",
    T(":".join(str(sp.Rational(1, 2) * (j ** 2 - (j - 1) ** 2) * 2) for j in (1, 2, 3))))

B.q("p-kin-12", "kinematics", 3,
    r"Two cars start together from the same place along a straight road. Car A moves at a constant $10$ m/s; car B starts from rest with acceleration $2\ \text{m/s}^2$. The maximum distance between them before B catches up is",
    [r"$25$ m", r"$50$ m", r"$100$ m", r"$12.5$ m"],
    r"""The gap grows while A is faster and shrinks once B is faster, so it is greatest when the speeds are equal: $2t=10$, $t=5$ s.

Gap $=10\times5-\tfrac12\times2\times5^2=50-25=25$ m.""",
    R(sp.maximum(10 * t - t ** 2, t, sp.Interval(0, 10))))

B.q("p-kin-13", "kinematics", 2,
    r"A stone is dropped from the top of a tower and takes $4$ s to reach the ground " + G10 + r". The distance it falls during the last second is",
    [r"$35$ m", r"$80$ m", r"$45$ m", r"$40$ m"],
    r"In $4$ s: $\tfrac12\cdot10\cdot16=80$ m. In $3$ s: $\tfrac12\cdot10\cdot9=45$ m. Last second: $80-45=35$ m.",
    R(sp.Rational(1, 2) * g * (16 - 9)))

B.q("p-kin-14", "kinematics", 3,
    r"A ball is thrown upward from the ground at $15$ m/s " + G10 + r". At what times is it $10$ m above the ground?",
    [r"$1$ s and $2$ s", r"$1$ s only", r"$2$ s only", r"$1.5$ s and $3$ s"],
    r"$10=15t-5t^2\Rightarrow t^2-3t+2=0\Rightarrow t=1$ s (on the way up) or $t=2$ s (on the way down). Both are valid because the ball rises to $\dfrac{15^2}{20}=11.25$ m $>10$ m.",
    Nums(*sorted(sp.solve(15 * t - 5 * t ** 2 - 10, t))))

# ------------------------------------------------------------ Newton's laws
B.q("p-new-01", "newtons-laws", 1,
    r"A net force of $12$ N acts on a $3$ kg block. Its acceleration is",
    [r"$4\ \text{m/s}^2$", r"$36\ \text{m/s}^2$", r"$0.25\ \text{m/s}^2$", r"$9\ \text{m/s}^2$"],
    r"Newton's second law: $a=\dfrac{F}{m}=\dfrac{12}{3}=4\ \text{m/s}^2$.",
    R(sp.Rational(12, 3)))

B.q("p-new-02", "newtons-laws", 1,
    r"A book rests on a table. The reaction force (Newton's third law partner) to the gravitational force of the Earth on the book is",
    [r"the gravitational force of the book on the Earth", r"the normal force of the table on the book", r"the force of the book on the table", r"the friction force on the book"],
    r"Third-law pairs act on **different** bodies and are of the same type. The Earth pulls the book down by gravity, so the book pulls the Earth up by gravity. The normal force balances the weight, but it is a different interaction (first-law balance, not a third-law pair).")

B.q("p-new-03", "newtons-laws", 2,
    r"A $2$ kg block is pulled along a horizontal floor by a horizontal force of $10$ N. The coefficient of kinetic friction is $0.3$ " + G10 + r". The acceleration of the block is",
    [r"$2\ \text{m/s}^2$", r"$5\ \text{m/s}^2$", r"$3\ \text{m/s}^2$", r"$8\ \text{m/s}^2$"],
    r"Friction $f=\mu mg=0.3\times2\times10=6$ N. Net force $=10-6=4$ N, so $a=\dfrac42=2\ \text{m/s}^2$.",
    R((10 - 0.3 * 2 * g) / 2))

B.q("p-new-04", "newtons-laws", 2,
    r"A block slides down a smooth (frictionless) incline of angle $30^\circ$ " + G10 + r". Its acceleration is",
    [r"$5\ \text{m/s}^2$", r"$10\ \text{m/s}^2$", r"$5\sqrt3\ \text{m/s}^2$", r"$2.5\ \text{m/s}^2$"],
    r"Only the component of gravity along the slope accelerates the block: $a=g\sin30^\circ=10\times\tfrac12=5\ \text{m/s}^2$. The mass cancels.",
    R(g * sp.sin(sp.pi / 6)))

B.q("p-new-05", "newtons-laws", 3,
    r"A person of mass $50$ kg stands on a scale in a lift that accelerates **upward** at $2\ \text{m/s}^2$ " + G10 + r". The scale reads",
    [r"$600$ N", r"$500$ N", r"$400$ N", r"$100$ N"],
    r"$N-mg=ma\Rightarrow N=m(g+a)=50\times12=600$ N. The person feels heavier (overweight).",
    R(50 * (g + 2)))

B.q("p-new-06", "newtons-laws", 3,
    r"Blocks of mass $2$ kg and $3$ kg are in contact on a smooth horizontal surface. A horizontal force of $10$ N pushes the $2$ kg block, which pushes the $3$ kg block. The force between the blocks is",
    [r"$6$ N", r"$4$ N", r"$10$ N", r"$5$ N"],
    r"Whole system: $a=\dfrac{10}{2+3}=2\ \text{m/s}^2$. The $3$ kg block is accelerated only by the contact force: $F_{12}=3\times2=6$ N.",
    R(3 * sp.Rational(10, 5)))

B.q("p-new-07", "newtons-laws", 1,
    r"A passenger in a bus that suddenly brakes lurches forward. This is best explained by",
    [r"inertia (Newton's first law)", r"a forward force acting on the passenger", r"Newton's third law", r"the passenger's weight increasing"],
    r"The passenger's body tends to keep moving at the original speed (inertia) while the bus slows down. No forward force pushes the passenger.")

B.q("p-new-08", "newtons-laws", 2,
    r"Two forces of $3$ N and $4$ N act on an object at right angles. The magnitude of the resultant force is",
    [r"$5$ N", r"$7$ N", r"$1$ N", r"$12$ N"],
    r"Perpendicular forces add like the sides of a right triangle: $F=\sqrt{3^2+4^2}=5$ N.",
    R(sp.sqrt(3 ** 2 + 4 ** 2)))

B.q("p-new-09", "newtons-laws", 2,
    r"A $10$ kg box rests on a horizontal floor with static friction coefficient $0.5$ " + G10 + r". A horizontal push of $30$ N is applied. The friction force on the box is",
    [r"$30$ N", r"$50$ N", r"$20$ N", r"$0$ N"],
    r"Maximum static friction $=\mu_sN=0.5\times100=50$ N. The push $30$ N is smaller, so the box does not move and static friction just balances the push: $f=30$ N.",
    R(min(30, 0.5 * 10 * g)))

B.q("p-new-10", "newtons-laws", 2,
    r"An object of weight $20$ N hangs from two strings, each making an angle of $60^\circ$ with the vertical. The tension in each string is",
    [r"$20$ N", r"$10$ N", r"$10\sqrt3$ N", r"$40$ N"],
    r"Vertical equilibrium: $2T\cos60^\circ=20\Rightarrow T=\dfrac{20}{2\times\frac12}=20$ N.",
    R(20 / (2 * sp.cos(sp.pi / 3))))

B.q("p-new-11", "newtons-laws", 1,
    r"The SI unit of force, the newton, is equivalent to",
    [r"$\text{kg}\cdot\text{m/s}^2$", r"$\text{kg}\cdot\text{m/s}$", r"$\text{kg}\cdot\text{m}^2/\text{s}^2$", r"$\text{kg/s}^2$"],
    r"From $F=ma$: $1\ \text{N}=1\ \text{kg}\times1\ \text{m/s}^2$. ($\text{kg}\cdot\text{m/s}$ is momentum and $\text{kg}\cdot\text{m}^2/\text{s}^2$ is energy.)")

B.q("p-new-12", "newtons-laws", 3,
    r"Masses of $3$ kg and $2$ kg hang from the two ends of a light string over a light, frictionless pulley " + G10 + r". The acceleration of the masses is",
    [r"$2\ \text{m/s}^2$", r"$10\ \text{m/s}^2$", r"$5\ \text{m/s}^2$", r"$4\ \text{m/s}^2$"],
    r"Net driving force $=(3-2)g=10$ N; total mass $=5$ kg. $a=\dfrac{10}{5}=2\ \text{m/s}^2$.",
    R((3 - 2) * g / sp.Integer(3 + 2)))

B.q("p-new-13", "newtons-laws", 3,
    r"A block slides down an incline of angle $37^\circ$ with kinetic friction coefficient $0.5$ " + G10 + r" and $\sin37^\circ=0.6$, $\cos37^\circ=0.8$. Its acceleration is",
    [r"$2\ \text{m/s}^2$", r"$6\ \text{m/s}^2$", r"$10\ \text{m/s}^2$", r"$4\ \text{m/s}^2$"],
    r"$a=g\sin\theta-\mu g\cos\theta=10\times0.6-0.5\times10\times0.8=6-4=2\ \text{m/s}^2$.",
    R(g * 0.6 - 0.5 * g * 0.8))

B.q("p-new-14", "newtons-laws", 1,
    r"An object moves at constant velocity. Which statement must be true?",
    [r"The net force on it is zero", r"No forces act on it", r"A constant force acts in the direction of motion", r"Its mass is zero"],
    r"Constant velocity means zero acceleration, so by Newton's first/second law the **net** force is zero. Several forces may act, but they balance.")
