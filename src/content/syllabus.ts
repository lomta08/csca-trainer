// Syllabus structure (CSCA 2025 syllabus). Edit names here; ids are used by
// question files, notes files and saved progress, so do not rename ids.

export type SubjectId = 'math' | 'physics' | 'chemistry';

export interface Subtopic {
  id: string;
  name: string;
  /** what the syllabus bullet covers (shown on Learn pages) */
  covers: string;
  /** rough study hours used by the plan generator */
  hours: number;
}

export interface Topic {
  id: string;
  name: string;
  /** number of questions in a 48-question mock exam */
  mockCount: number;
  subtopics: Subtopic[];
}

export interface Subject {
  id: SubjectId;
  name: string;
  short: string;
  color: string;
  topics: Topic[];
}

export const SUBJECTS: Subject[] = [
  {
    id: 'math',
    name: 'Mathematics',
    short: 'Math',
    color: '#2f5bd3',
    topics: [
      {
        id: 'sets-inequalities',
        name: 'Sets & Inequalities',
        mockCount: 7,
        subtopics: [
          { id: 'sets', name: 'Sets', covers: 'Definition, representation and operations of sets (union, intersection, complement, subsets)', hours: 2 },
          { id: 'inequality-properties', name: 'Properties of Inequalities', covers: 'Rules for manipulating inequalities, comparing sizes, basic AM–GM', hours: 1.5 },
          { id: 'quadratic-inequalities', name: 'Quadratic Inequalities', covers: 'Solving quadratic inequalities, the link with roots and the graph of a parabola', hours: 2 },
          { id: 'rational-inequalities', name: 'Rational (Fractional) Inequalities', covers: 'Solving inequalities with the unknown in a denominator; the sign-chart method', hours: 2 },
        ],
      },
      {
        id: 'functions',
        name: 'Functions',
        mockCount: 19,
        subtopics: [
          { id: 'function-properties', name: 'Domain, Range, Monotonicity & Parity', covers: 'Domain, range, increasing/decreasing functions, odd and even functions, periodicity', hours: 3 },
          { id: 'elementary-functions', name: 'Power, Exponential & Logarithmic Functions', covers: 'Laws of exponents and logarithms, graphs and properties, comparing values', hours: 3 },
          { id: 'trigonometry', name: 'Trigonometric Functions', covers: 'Radians, special values, identities, graphs, period, compound and double angle formulas', hours: 4 },
          { id: 'sequences', name: 'Sequences', covers: 'General term, arithmetic and geometric sequences and their sums', hours: 3 },
          { id: 'derivatives', name: 'Derivatives & Basic Calculus', covers: 'Definition, geometric meaning (tangent slope), rules, monotonicity, extrema, simple integrals', hours: 4 },
        ],
      },
      {
        id: 'geometry-algebra',
        name: 'Geometry & Algebra',
        mockCount: 15,
        subtopics: [
          { id: 'lines-circles', name: 'Lines & Circles', covers: 'Slope, equations of lines, parallel/perpendicular, distances, circle equations, line–circle position', hours: 3 },
          { id: 'conics', name: 'Ellipses, Hyperbolas & Parabolas', covers: 'Standard equations, a, b, c, eccentricity, foci, asymptotes, directrix', hours: 4 },
          { id: 'vectors', name: 'Vectors', covers: 'Vector operations, coordinates, dot product, angle, parallel and perpendicular vectors', hours: 2.5 },
          { id: 'complex-numbers', name: 'Complex Numbers', covers: 'Arithmetic, conjugate, modulus, the complex plane', hours: 2 },
          { id: 'solid-geometry', name: 'Solid Geometry', covers: 'Space rectangular coordinates, distances in 3D, surface area and volume of simple solids', hours: 3 },
        ],
      },
      {
        id: 'probability-statistics',
        name: 'Probability & Statistics',
        mockCount: 7,
        subtopics: [
          { id: 'classical-probability', name: 'Classical Probability', covers: 'Equally likely outcomes, counting, complementary and independent events', hours: 2.5 },
          { id: 'mean-variance', name: 'Mean & Variance', covers: 'Mean, variance, standard deviation, effect of linear transformations', hours: 1.5 },
          { id: 'normal-distribution', name: 'Normal Distribution', covers: 'Shape, symmetry, the 68–95–99.7 rule, standardising', hours: 1.5 },
        ],
      },
    ],
  },
  {
    id: 'physics',
    name: 'Physics',
    short: 'Physics',
    color: '#c2410c',
    topics: [
      {
        id: 'mechanics',
        name: 'Mechanics',
        mockCount: 24,
        subtopics: [
          { id: 'kinematics', name: 'Kinematics', covers: 'Displacement, velocity, acceleration, uniformly accelerated motion, free fall, projectiles', hours: 3 },
          { id: 'newtons-laws', name: "Newton's Laws", covers: 'Forces, friction, the three laws, connected bodies, inclines', hours: 3 },
          { id: 'momentum', name: 'Momentum & Impulse', covers: 'Momentum, impulse, conservation of momentum, collisions', hours: 2.5 },
          { id: 'work-energy', name: 'Work & Energy', covers: 'Work, power, kinetic and potential energy, work–energy theorem, conservation of mechanical energy', hours: 3 },
          { id: 'circular-gravitation', name: 'Circular Motion & Gravitation', covers: 'Angular velocity, centripetal acceleration and force, universal gravitation, satellites', hours: 3 },
          { id: 'shm-waves', name: 'Simple Harmonic Motion & Waves', covers: 'Springs and pendulums, period, wave speed, wavelength, frequency', hours: 2.5 },
        ],
      },
      {
        id: 'electromagnetism',
        name: 'Electromagnetism',
        mockCount: 12,
        subtopics: [
          { id: 'electrostatics', name: 'Electrostatics', covers: "Coulomb's law, electric field strength, potential, potential difference, capacitors", hours: 3 },
          { id: 'dc-circuits', name: 'DC Circuits', covers: "Ohm's law, resistance, series and parallel, power, EMF and internal resistance", hours: 3 },
          { id: 'magnetic-fields', name: 'Magnetic Fields', covers: 'Magnetic induction, Ampère force on a wire, Lorentz force on a charge, circular motion in B', hours: 2.5 },
          { id: 'em-induction', name: 'Electromagnetic Induction', covers: "Magnetic flux, Faraday's law, Lenz's law, motional EMF", hours: 2.5 },
        ],
      },
      {
        id: 'thermodynamics',
        name: 'Thermodynamics',
        mockCount: 4,
        subtopics: [
          { id: 'thermodynamics', name: 'Gases & the First Law', covers: 'Kinetic theory, ideal gas equation of state, gas laws, first law of thermodynamics', hours: 2.5 },
        ],
      },
      {
        id: 'optics',
        name: 'Optics',
        mockCount: 4,
        subtopics: [
          { id: 'reflection-refraction', name: 'Reflection & Refraction', covers: "Law of reflection, Snell's law, refractive index, total internal reflection", hours: 1.5 },
          { id: 'interference-diffraction', name: 'Interference & Diffraction', covers: "Young's double slit, fringe spacing, thin films, diffraction", hours: 1.5 },
        ],
      },
      {
        id: 'modern-physics',
        name: 'Modern Physics',
        mockCount: 4,
        subtopics: [
          { id: 'photoelectric', name: 'Photoelectric Effect', covers: "Photons, Einstein's photoelectric equation, work function, threshold frequency", hours: 1.5 },
          { id: 'atomic-structure', name: 'Atomic Structure', covers: 'Rutherford model, Bohr model, energy levels, emission and absorption spectra', hours: 1.5 },
          { id: 'nuclear', name: 'Nuclear Physics', covers: 'Nuclear composition, radioactive decay, half-life, nuclear equations, mass–energy', hours: 1.5 },
        ],
      },
    ],
  },
  {
    id: 'chemistry',
    name: 'Chemistry',
    short: 'Chem',
    color: '#0f766e',
    topics: [
      {
        id: 'basic-concepts',
        name: 'Basic Concepts & Calculations',
        mockCount: 13,
        subtopics: [
          { id: 'matter-classification', name: 'Classification & States of Matter', covers: 'Pure substances, mixtures, elements, compounds, physical vs chemical change, colloids', hours: 1.5 },
          { id: 'chemical-equations', name: 'Chemical Notation & Equations', covers: 'Formulas, valence, balancing equations, reaction types', hours: 1.5 },
          { id: 'concentration-ph', name: 'Solution Concentration & pH', covers: 'Mass fraction, molarity, dilution, pH of strong acids and bases', hours: 2 },
          { id: 'mole-calculations', name: 'Amount of Substance (mol)', covers: 'Molar mass, Avogadro constant, stoichiometry, limiting reagent', hours: 2.5 },
          { id: 'gas-law', name: 'Gas Laws in Chemistry', covers: 'Molar volume at STP, ideal gas law, Avogadro’s law, gas density', hours: 1.5 },
        ],
      },
      {
        id: 'properties-reactions',
        name: 'Properties & Reactions',
        mockCount: 14,
        subtopics: [
          { id: 'inorganic', name: 'Common Inorganic Substances', covers: 'Metals (Na, Al, Fe, Cu), non-metals (Cl, S, N, C, Si), oxides, acids, bases, salts', hours: 3 },
          { id: 'organic', name: 'Basic Organic Compounds', covers: 'Alkanes, alkenes, alkynes, benzene, alcohols, aldehydes, carboxylic acids, esters, isomers', hours: 3 },
          { id: 'redox', name: 'Redox Reactions', covers: 'Oxidation states, oxidising and reducing agents, electron transfer, balancing', hours: 2 },
          { id: 'ionic-reactions', name: 'Ionic Reactions & Ion Tests', covers: 'Ionic equations, coexistence of ions, tests for common ions', hours: 2 },
        ],
      },
      {
        id: 'theories-laws',
        name: 'Theories & Laws',
        mockCount: 12,
        subtopics: [
          { id: 'atomic-periodic', name: 'Atomic Structure & Periodic Law', covers: 'Protons, neutrons, electrons, isotopes, electron configuration, periodic trends', hours: 2.5 },
          { id: 'bonding', name: 'Chemical Bonds & Intermolecular Forces', covers: 'Ionic, covalent and metallic bonds, polarity, hydrogen bonds, van der Waals forces', hours: 2 },
          { id: 'rate-equilibrium', name: 'Reaction Rate & Equilibrium', covers: 'Factors affecting rate, equilibrium, Le Chatelier’s principle, equilibrium constant', hours: 3 },
          { id: 'electrolytes', name: 'Electrolyte Solutions', covers: 'Strong and weak electrolytes, ionisation, hydrolysis of salts, electrochemistry basics', hours: 2 },
        ],
      },
      {
        id: 'experiments',
        name: 'Experiments & Applications',
        mockCount: 9,
        subtopics: [
          { id: 'lab-safety', name: 'Lab Safety & Apparatus', covers: 'Safe practice, common apparatus and their uses, basic operations', hours: 1 },
          { id: 'gas-preparation', name: 'Preparation & Identification of Gases', covers: 'Preparing O₂, H₂, CO₂, Cl₂, NH₃; collection methods; tests', hours: 1.5 },
          { id: 'separation', name: 'Separation & Purification', covers: 'Filtration, evaporation, distillation, extraction, crystallisation, removing impurities', hours: 1.5 },
          { id: 'industrial', name: 'Industrial Processes', covers: 'Haber process, contact process, chlor-alkali, metal extraction, conditions and trade-offs', hours: 1.5 },
        ],
      },
    ],
  },
];

export const SUBJECT_IDS: SubjectId[] = ['math', 'physics', 'chemistry'];

export function getSubject(id: string): Subject | undefined {
  return SUBJECTS.find((s) => s.id === id);
}

export interface SubtopicRef {
  subject: Subject;
  topic: Topic;
  subtopic: Subtopic;
}

export function allSubtopics(subject?: SubjectId): SubtopicRef[] {
  const out: SubtopicRef[] = [];
  for (const s of SUBJECTS) {
    if (subject && s.id !== subject) continue;
    for (const t of s.topics) for (const st of t.subtopics) out.push({ subject: s, topic: t, subtopic: st });
  }
  return out;
}

export function findSubtopic(subjectId: string, subtopicId: string): SubtopicRef | undefined {
  return allSubtopics(subjectId as SubjectId).find((r) => r.subtopic.id === subtopicId);
}

export function subtopicName(subjectId: string, subtopicId: string): string {
  return findSubtopic(subjectId, subtopicId)?.subtopic.name ?? subtopicId;
}

export function topicName(subjectId: string, topicId: string): string {
  return getSubject(subjectId)?.topics.find((t) => t.id === topicId)?.name ?? topicId;
}

export const EXAM = {
  questions: 48,
  minutes: 60,
  secondsPerQuestion: 75,
};
