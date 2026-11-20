// Periodic table data (elements 1–57 and 72–88). Relative atomic masses are the rounded
// standard values used in high-school chemistry (Cl 35.5, Cu 64, ...). Values in
// parentheses are mass numbers of the most stable isotope.
export type ElementClass = 'metal' | 'nonmetal' | 'metalloid' | 'noble';

export interface Element {
  z: number;
  sym: string;
  name: string;
  mass: string;
  group: number; // 1–18
  period: number;
  cls: ElementClass;
}

const RAW = `1 H Hydrogen 1 1 1 n
2 He Helium 4 18 1 g
3 Li Lithium 7 1 2 m
4 Be Beryllium 9 2 2 m
5 B Boron 11 13 2 s
6 C Carbon 12 14 2 n
7 N Nitrogen 14 15 2 n
8 O Oxygen 16 16 2 n
9 F Fluorine 19 17 2 n
10 Ne Neon 20 18 2 g
11 Na Sodium 23 1 3 m
12 Mg Magnesium 24 2 3 m
13 Al Aluminium 27 13 3 m
14 Si Silicon 28 14 3 s
15 P Phosphorus 31 15 3 n
16 S Sulfur 32 16 3 n
17 Cl Chlorine 35.5 17 3 n
18 Ar Argon 40 18 3 g
19 K Potassium 39 1 4 m
20 Ca Calcium 40 2 4 m
21 Sc Scandium 45 3 4 m
22 Ti Titanium 48 4 4 m
23 V Vanadium 51 5 4 m
24 Cr Chromium 52 6 4 m
25 Mn Manganese 55 7 4 m
26 Fe Iron 56 8 4 m
27 Co Cobalt 59 9 4 m
28 Ni Nickel 59 10 4 m
29 Cu Copper 64 11 4 m
30 Zn Zinc 65 12 4 m
31 Ga Gallium 70 13 4 m
32 Ge Germanium 73 14 4 s
33 As Arsenic 75 15 4 s
34 Se Selenium 79 16 4 n
35 Br Bromine 80 17 4 n
36 Kr Krypton 84 18 4 g
37 Rb Rubidium 85.5 1 5 m
38 Sr Strontium 88 2 5 m
39 Y Yttrium 89 3 5 m
40 Zr Zirconium 91 4 5 m
41 Nb Niobium 93 5 5 m
42 Mo Molybdenum 96 6 5 m
43 Tc Technetium (98) 7 5 m
44 Ru Ruthenium 101 8 5 m
45 Rh Rhodium 103 9 5 m
46 Pd Palladium 106 10 5 m
47 Ag Silver 108 11 5 m
48 Cd Cadmium 112 12 5 m
49 In Indium 115 13 5 m
50 Sn Tin 119 14 5 m
51 Sb Antimony 122 15 5 s
52 Te Tellurium 128 16 5 s
53 I Iodine 127 17 5 n
54 Xe Xenon 131 18 5 g
55 Cs Caesium 133 1 6 m
56 Ba Barium 137 2 6 m
57 La Lanthanum* 139 3 6 m
72 Hf Hafnium 178.5 4 6 m
73 Ta Tantalum 181 5 6 m
74 W Tungsten 184 6 6 m
75 Re Rhenium 186 7 6 m
76 Os Osmium 190 8 6 m
77 Ir Iridium 192 9 6 m
78 Pt Platinum 195 10 6 m
79 Au Gold 197 11 6 m
80 Hg Mercury 201 12 6 m
81 Tl Thallium 204 13 6 m
82 Pb Lead 207 14 6 m
83 Bi Bismuth 209 15 6 m
84 Po Polonium (209) 16 6 s
85 At Astatine (210) 17 6 s
86 Rn Radon (222) 18 6 g
87 Fr Francium (223) 1 7 m
88 Ra Radium (226) 2 7 m`;

const CLS: Record<string, ElementClass> = { m: 'metal', n: 'nonmetal', s: 'metalloid', g: 'noble' };

export const ELEMENTS: Element[] = RAW.split('\n').map((line) => {
  const [z, sym, name, mass, group, period, c] = line.trim().split(/\s+/);
  return { z: Number(z), sym, name, mass, group: Number(group), period: Number(period), cls: CLS[c] };
});
