#!/usr/bin/env python3
"""One-off generator: IGCSE Mathematics-related topic lectures + voice-overs."""
from __future__ import annotations

import os
from pathlib import Path

BASE = Path(__file__).resolve().parent

# (folder_name, syllabus_code, display_title, cambridge_slug_for_url)
SYLLABI = [
    ("Mathematics - 0580", "0580", "Cambridge IGCSE Mathematics", "cambridge-igcse-mathematics-0580"),
    ("Mathematics (9-1) - 0980", "0980", "Cambridge IGCSE Mathematics (9–1)", "cambridge-igcse-mathematics-9-1-0980"),
    ("Mathematics us - 0444", "0444", "Cambridge IGCSE Mathematics (US)", "cambridge-igcse-mathematics-us-0444"),
]

MATH_TOPICS = [
    ("Number", "Algebra and Graphs"),
    ("Algebra and Graphs", "Coordinate Geometry"),
    ("Coordinate Geometry", "Geometry"),
    ("Geometry", "Mensuration"),
    ("Mensuration", "Trigonometry"),
    ("Trigonometry", "Vectors and Transformations"),
    ("Vectors and Transformations", "Probability"),
    ("Probability", "Statistics"),
    ("Statistics", "Past Papers"),
    ("Past Papers", None),
]

INTL_TOPICS = [
    ("Number", "Algebra"),
    ("Algebra", "Functions"),
    ("Functions", "Coordinate Geometry"),
    ("Coordinate Geometry", "Geometry"),
    ("Geometry", "Mensuration"),
    ("Mensuration", "Trigonometry"),
    ("Trigonometry", "Transformations and Vectors"),
    ("Transformations and Vectors", "Probability"),
    ("Probability", "Statistics"),
    ("Statistics", "Past Papers"),
    ("Past Papers", None),
]

ADD_TOPICS = [
    ("Functions and Quadratics", "Indices Surds and Logarithms"),
    ("Indices Surds and Logarithms", "Polynomials and Equations"),
    ("Polynomials and Equations", "Coordinate Geometry and Graphs"),
    ("Coordinate Geometry and Graphs", "Circular Measure and Trigonometry"),
    ("Circular Measure and Trigonometry", "Series Binomial and Counting"),
    ("Series Binomial and Counting", "Vectors and Matrices"),
    ("Vectors and Matrices", "Differentiation"),
    ("Differentiation", "Integration"),
    ("Integration", "Past Papers"),
    ("Past Papers", None),
]

STAT_TOPICS = [
    ("Planning and Data Collection", "Presentation of Data"),
    ("Presentation of Data", "Averages and Spread"),
    ("Averages and Spread", "Probability"),
    ("Probability", "Discrete and Continuous Models"),
    ("Discrete and Continuous Models", "Correlation and Regression"),
    ("Correlation and Regression", "Sampling and Uncertainty"),
    ("Sampling and Uncertainty", "Past Papers"),
    ("Past Papers", None),
]


def cambridge_url(slug: str) -> str:
    return (
        "https://www.cambridgeinternational.org/programmes-and-qualifications/"
        f"{slug}/"
    )


def lecture_math(topic: str, next_t: str | None, meta: dict) -> str:
    code = meta["code"]
    title = meta["title"]
    url = meta["url"]
    tier = meta.get("tier_note", "")
    next_line = f"**Next:** **{next_t}**." if next_t else "**Next:** past papers and mixed revision."

    if topic == "Past Papers":
        return f"""# Complete Lecture: Past Papers and Examination Technique ({title} {code})

This lecture is **exam technique** for **{code}**: timing, calculator discipline, and how to **read** questions—not a replacement for topic notes. Programme: [{title} ({code})]({url}).

---

## 1. What {code} papers reward

- **Accurate** routine skills (algebra, number, diagrams).
- **Communication**: show working; **label** diagrams and **state** assumptions.
- **Interpretation** of results in **context** questions.

{tier}

---

## 2. Before you start a question

1. Note **Core vs Extended** expectations if you are entered for a tier—answer at the depth you prepared for.
2. Underline **given** information and the **required form** (exact value, 3 s.f., inequality…).
3. Decide **calculator vs non-calculator** paper rules for this session.

---

## 3. Working habits

- **Mental check** of magnitude (indices, standard form, trig).
- **Re-read** inequalities and **domain** restrictions (e.g. valid triangle side lengths).
- For **probability**, check probabilities sum where appropriate and **0 ≤ p ≤ 1**.

---

## 4. Common mark drops

- Arithmetic slips in **fractions** and **indices**.
- Wrong **angle mode** (degrees vs radians) where relevant.
- **Vectors**: direction errors; **transformations**: wrong centre or scale factor sign.

---

## 5. Revision cycle

| When | Task |
|------|------|
| Weekly | Mixed topic sheet |
| Fortnightly | Timed past paper |
| After each paper | Error log + redo |

---

## Revision checklist

- [ ] Formula sheet (if provided) practised until fast.
- [ ] Non-calculator skills fluent for the relevant paper.
- [ ] Two full papers under time before the exam series.

{next_line}

---

### Reference

- [{title} ({code})]({url})
"""

    bodies = {
        "Number": f"""# Complete Lecture: Number ({title} {code})

**Number** underpins every other topic: **indices**, **fractions**, **percentages**, **standard form**, and **estimation**. Programme: [{title} ({code})]({url}).

---

## 1. Types of number and sets

- **Natural numbers**, **integers**, **rationals**, **irrationals**, **reals** (use definitions from your syllabus).
- **Factors**, **multiples**, **HCF/LCM** (Euclidean method for HCF where practised).

---

## 2. Fractions, ratio, and proportion

- Four operations with fractions; **order of operations** (BIDMAS/BODMAS).
- **Ratio** and **proportion** in context (recipes, maps, best-buy problems).

---

## 3. Percentages and growth

- **Percentage change**; **reverse percentages** (“after a 20% increase…”).
- **Simple** and **compound** interest models (definitions and rearrangement).

---

## 4. Indices and standard form

- Laws of indices for integer powers; **standard form** **a × 10ⁿ** with **1 ≤ |a| < 10** (unless syllabus states otherwise).
- **Estimation** by rounding to **1 s.f.** for a sense-check.

---

## 5. Bounds and accuracy (if examined)

- **Upper/lower bounds** from rounded measurements; **intervals** for discrete vs continuous contexts—follow **exam** definitions.

---

## Common misconceptions

- **Increasing** a price by **10%** then **decreasing** by **10%** does **not** return to the start.
- **(−2)⁴** is **positive**; **−2⁴** means **−(2⁴)** unless brackets say otherwise.

---

## Revision checklist

- [ ] Mixed drill: fractions + percentages + indices.
- [ ] Standard form add/multiply on paper and verify on calculator where allowed.
- [ ] One bounds question from a past paper.

{next_line}

---

### Reference

- [{title} ({code})]({url})
""",
        "Algebra and Graphs": f"""# Complete Lecture: Algebra and Graphs ({title} {code})

**Algebra** is the language of relationships: **expressions**, **equations**, **graphs**, and **sequences**. Programme: [{title} ({code})]({url}).

---

## 1. Expressions and formulae

- **Substitution**; **expanding** brackets; **factorising** (common factor, quadratic patterns you are taught).
- **Rearranging** formulae: treat target variable like “unknown” and **balance** operations.

---

## 2. Linear and quadratic equations

- **Linear**: ax + b = c; **fractional** coefficients carefully.
- **Quadratic**: factorisation where possible; **completing the square** if in your tier; **formula** with **discriminant** awareness (number of roots).

---

## 3. Simultaneous equations

- **Elimination** and **substitution** for two unknowns; interpret **no solution** / **infinitely many** in **linear** cases if examined.

---

## 4. Graphs and functions (IGCSE core skills)

- Plot and read **y = mx + c**; **gradient** and **intercept** meaning.
- **Curves**: recognise **parabola** shape from **y = ax² + bx + c**; **sketch** using roots and vertex where appropriate.

---

## 5. Sequences (if in your specification)

- **nth term** rules for arithmetic patterns; recognise **geometric** patterns if required.

---

## Common misconceptions

- **Squaring** a negative on a calculator: use **brackets**.
- **Gradient** is **rise/run**—consistent scales on axes when reading graphs.

---

## Revision checklist

- [ ] Factorise at least 12 quadratics mixed with negatives.
- [ ] Solve simultaneous equations from a word problem.
- [ ] Sketch a line and a quadratic on the same axes and read intersections.

{next_line}

---

### Reference

- [{title} ({code})]({url})
""",
        "Coordinate Geometry": f"""# Complete Lecture: Coordinate Geometry ({title} {code})

You use coordinates to turn geometry into **algebra**: **distance**, **midpoint**, **gradient**, and **equations of lines**. Programme: [{title} ({code})]({url}).

---

## 1. Points and length

- **Midpoint** of (x₁, y₁) and (x₂, y₂): **((x₁+x₂)/2, (y₁+y₂)/2)**.
- **Distance** from Pythagoras: **√((x₂−x₁)² + (y₂−y₁)²)**.

---

## 2. Gradient and parallel/perpendicular

- **m = (y₂−y₁)/(x₂−x₁)** (x₂ ≠ x₁).
- **Parallel** lines: **equal** gradients.
- **Perpendicular** lines (non-vertical/horizontal): **m₁m₂ = −1** (if examined).

---

## 3. Line equations

- **y = mx + c**; **y − y₁ = m(x − x₁)**.
- Find equation through two points: compute **m**, then substitute a point.

---

## 4. Intersections

- Solve **simultaneous** equations for intersection of **line** and **curve** (quadratic) where examined—interpret **discriminant** for number of intersections.

---

## Common misconceptions

- Vertical lines: **undefined** gradient; equation **x = k**, not **y = mx + c**.
- Distance is always **positive**—square root of a sum of squares.

---

## Revision checklist

- [ ] Compute distance + midpoint from coordinates without a diagram mistake.
- [ ] Find line equations in two different forms.
- [ ] One intersection problem with a quadratic curve.

{next_line}

---

### Reference

- [{title} ({code})]({url})
""",
        "Geometry": f"""# Complete Lecture: Geometry ({title} {code})

**Geometry** combines **angle facts**, **polygons**, **circles**, and **reasoning**—often with a diagram. Programme: [{title} ({code})]({url}).

---

## 1. Angle facts

- Angles on a **straight line**; at a **point**; **vertically opposite**.
- **Parallel lines** with a transversal: corresponding/alternate/interior relationships.

---

## 2. Polygons

- Sum of interior angles of an **n**-gon: **(n − 2) × 180°** (or equivalent formula you use).
- **Regular** polygons: equal sides/angles.

---

## 3. Circle theorems (tier-dependent)

Learn the theorems your syllabus lists (e.g. angle at centre vs circumference; angle in a semicircle; cyclic quadrilateral properties). Always **state the theorem** you used.

---

## 4. Similarity and congruence

- **Similar** shapes: angles equal; sides in proportion; **area scale k²**, **volume k³**.
- **Congruence** tests for triangles as taught (SSS/SAS/ASA/RHS).

---

## Common misconceptions

- Assuming a diagram is **drawn to scale** unless told.
- Mixing up **similar** vs **congruent**.

---

## Revision checklist

- [ ] Angle-chase on a parallel-line diagram.
- [ ] One circle theorem proof-style explanation.
- [ ] Similarity area/volume scale factor problem.

{next_line}

---

### Reference

- [{title} ({code})]({url})
""",
        "Mensuration": f"""# Complete Lecture: Mensuration ({title} {code})

**Mensuration** is **measurement**: **perimeter**, **area**, **surface area**, and **volume**—including **compound** shapes. Programme: [{title} ({code})]({url}).

---

## 1. Units and compound shapes

- Convert **mm/cm/m/km** consistently; watch **square** and **cubic** units.
- Split compound shapes into **rectangles/triangles/prisms** you know.

---

## 2. Standard results (learn precisely)

- **Rectangle** area **bh**; **triangle** **½bh**; **parallelogram** **bh**; **trapezium** **½(a+b)h**.
- **Circle**: circumference **2πr**, area **πr²**.
- **Prism** volume: **cross-sectional area × length** (concept that rescues many problems).

---

## 3. Surface area

- **Net** thinking: count faces carefully; **cylinder** **2πr² + 2πrh** if examined.

---

## 4. Arc length and sector area (if examined)

- Fraction **θ/360°** of full circle for arc/sector (degrees model); radians if your course uses them.

---

## Common misconceptions

- Doubling a length **does not** double area—area scales by **k²**.
- Confusing **diameter** and **radius** in formulas.

---

## Revision checklist

- [ ] Table of perimeter/area/volume formulas you must recall.
- [ ] One compound shape with subtraction of a hole.
- [ ] One surface area problem with a cylinder or prism.

{next_line}

---

### Reference

- [{title} ({code})]({url})
""",
        "Trigonometry": f"""# Complete Lecture: Trigonometry ({title} {code})

**Trigonometry** links **angles** and **side lengths** in right-angled and general triangles (as your tier requires). Programme: [{title} ({code})]({url}).

---

## 1. Right-angled triangle definitions

- **sin θ = opposite/hypotenuse**, **cos θ = adjacent/hypotenuse**, **tan θ = opposite/adjacent**.
- Use **SOHCAHTOA** consistently; label the **right angle** and **hypotenuse** first.

---

## 2. Exact values (if required)

- Learn **sin/cos/tan** for **30°, 45°, 60°** (and **0°/90°** cautiously where defined).

---

## 3. Sine and cosine rules (Extended/tier-dependent)

- **Sine rule** and **cosine rule** for general triangles; **area = ½ab sin C**.

---

## 4. Bearings and 3D sketches

- **Three-figure bearings** clockwise from **north**; clean diagrams for **3D** problems.

---

## Common misconceptions

- Using SOHCAHTOA in **non-right** triangles without dropping a perpendicular or switching rules.
- Calculator in **wrong angle mode** (degrees vs radians).

---

## Revision checklist

- [ ] Ten right-triangle trig questions mixed find-side/find-angle.
- [ ] One sine/cosine rule problem if in your specification.
- [ ] One bearing/3D interpretation question.

{next_line}

---

### Reference

- [{title} ({code})]({url})
""",
        "Vectors and Transformations": f"""# Complete Lecture: Vectors and Transformations ({title} {code})

**Vectors** describe **displacement**; **transformations** move or resize shapes in the plane. Programme: [{title} ({code})]({url}).

---

## 1. Vector notation and arithmetic

- Column vectors **(x, y)**; **addition** componentwise; **scalar multiple** **k** stretches/reverses direction if **k < 0**.
- **Magnitude** **√(x² + y²)** (2D).

---

## 2. Transformations

Know definitions and **invariant** points/lines where taught:
- **Translation** by vector
- **Reflection** (line)
- **Rotation** (centre, angle, direction)
- **Enlargement** (centre, scale factor; **negative** scale factor meaning)

---

## 3. Combining transformations (if examined)

- Track a single point through a sequence; watch **order** effects.

---

## Common misconceptions

- **Translation vector** is what you **add**, not a coordinate pair of the shape “corner” unless stated.
- Enlargement with **|k| < 1** reduces size.

---

## Revision checklist

- [ ] Vector addition and scalar multiplication drill.
- [ ] Identify transformation from a diagram + give full specification.
- [ ] One combined transformation question.

{next_line}

---

### Reference

- [{title} ({code})]({url})
""",
        "Probability": f"""# Complete Lecture: Probability ({title} {code})

**Probability** quantifies uncertainty using **0 to 1** (or 0% to 100%). Programme: [{title} ({code})]({url}).

---

## 1. Experimental vs theoretical

- **Relative frequency** from trials estimates probability; improves with more trials (intuition for **law of large numbers** at O Level depth).

---

## 2. Sample space and events

- List outcomes systematically for **two dice**, **cards**, **spinners**.
- **Mutually exclusive** events: **P(A or B) = P(A) + P(B)**.
- **Independent** events: **P(A and B) = P(A) × P(B)** (only when independence is justified).

---

## 3. Tree diagrams

- Multiply along branches; add **mutually exclusive** end outcomes.

---

## 4. Conditional probability (if examined)

- **P(A|B) = P(A and B) / P(B)** with **P(B) > 0**; read wording carefully (“given that…”).

---

## Common misconceptions

- Adding probabilities that are **not** mutually exclusive.
- Treating events as independent without checking (with replacement vs without).

---

## Revision checklist

- [ ] Build a tree for a two-stage experiment.
- [ ] Translate word problems into events and probabilities.
- [ ] One conditional probability question if in your tier.

{next_line}

---

### Reference

- [{title} ({code})]({url})
""",
        "Statistics": f"""# Complete Lecture: Statistics ({title} {code})

**Statistics** summarises data: **tables**, **charts**, **averages**, and **spread**. Programme: [{title} ({code})]({url}).

---

## 1. Collecting and organising data

- **Tally charts**, **frequency tables**, **grouped data** (continuous measurements).

---

## 2. Charts you must read and draw cleanly

- **Bar chart** (categories) vs **histogram** (continuous classes—equal class widths if required).
- **Pie chart** angles from frequencies; **line graph** for trends over time.

---

## 3. Averages and which to use

- **Mean**, **median**, **mode**; **range** and **interquartile range** if examined.
- **Outliers** affect mean more than median—interpret in context.

---

## 4. Cumulative frequency (if examined)

- Plot **upper class boundary** vs cumulative frequency; read **median** and **quartiles** graphically.

---

## Common misconceptions

- Histogram **area** meaning vs bar chart **height** meaning (depends on definition taught).
- Using **midpoint** of class for estimating mean from grouped data—method clarity.

---

## Revision checklist

- [ ] Draw one bar chart and one histogram from the same dataset idea (different variable types).
- [ ] Compute mean/median/mode for raw and grouped data.
- [ ] Interpret one chart in a sentence of context.

{next_line}

---

### Reference

- [{title} ({code})]({url})
""",
    }

    return bodies[topic]


def voice_math(topic: str, next_t: str | None, meta: dict) -> str:
    code = meta["code"]
    title = meta["title"]
    next_line = f"Next: **{next_t}**." if next_t else "Next: keep practising **timed papers**."

    if topic == "Past Papers":
        return f"""# Voice-Over Script: Past Papers and Examination Technique ({title} {code})

**[Visual: Past paper, formula sheet, calculator with “check mode” sticker]**

**Narrator:**  
Past papers train **exam habits** for **{code}**: reading constraints, showing working, and managing time across topics.

---

**[Visual: Highlight “3 s.f.” and “show that” prompts]**

**Narrator:**  
Circle command words and required forms before you write. “Show that” means every line must follow logically—no guessing the answer first without justification.

---

**[Visual: Error log notebook]**

**Narrator:**  
After each paper, log mistakes by type: arithmetic, algebra, diagram misread, probability model. Redo the same question next day—**fast improvement**.

---

**[Visual: Checklist — plan, work, interpret, review]**

**Narrator:**  
{next_line}

**[Visual: End card]**
"""

    intros = {
        "Number": ("Number line and indices on screen", "Number skills keep every later topic stable—fractions, indices, and standard form show up everywhere."),
        "Algebra and Graphs": ("Graph of line and parabola", "Algebra turns words into equations and pictures into graphs—factorise, solve, sketch."),
        "Coordinate Geometry": ("Coordinate grid with two points", "Coordinates let you compute distance, midpoint, and equations of straight lines."),
        "Geometry": ("Parallel lines and angles", "Geometry rewards neat diagrams and named angle facts—then apply circle theorems if your tier includes them."),
        "Mensuration": ("Compound shape split into rectangles", "Mensuration is about consistent units and choosing the right area or volume formula."),
        "Trigonometry": ("Right triangle labelled opposite/adjacent/hypotenuse", "Trigonometry links angles and sides—label the triangle before you press calculator buttons."),
        "Vectors and Transformations": ("Shape reflected and translated", "Vectors add like steps; transformations need a full description—centre, line, angle, scale factor."),
        "Probability": ("Tree diagram two stages", "Probability needs a clear model: sample space, tree, or table—then multiply along branches carefully."),
        "Statistics": ("Bar chart and frequency table", "Statistics is communication: choose the right chart and interpret the average in context."),
    }

    vis, line = intros[topic]
    return f"""# Voice-Over Script: {topic} ({title} {code})

**[Visual: {vis}]**

**Narrator:**  
{line}

---

**[Visual: Worked example skeleton — given, method, answer]**

**Narrator:**  
In exams, show **method** even when a calculator could jump ahead—method marks are often half the battle.

---

**[Visual: Common mistake flash — brackets, signs, units]**

**Narrator:**  
Slow down on signs, fractions, and units—those slips erase hard work on multi-mark questions.

---

**[Visual: Mini checklist for this topic]**

**Narrator:**  
{next_line}

**[Visual: End card]**
"""


def lecture_intl(topic: str, next_t: str | None, meta: dict) -> str:
    code = meta["code"]
    title = meta["title"]
    url = meta["url"]
    next_line = f"**Next:** **{next_t}**." if next_t else "**Next:** mixed revision."

    if topic == "Past Papers":
        return lecture_math("Past Papers", None, meta)

    if topic == "Algebra":
        return f"""# Complete Lecture: Algebra ({title} {code})

**Algebra** in **0607** supports functions, graphs, and modelling across the course. Programme: [{title} ({code})]({url}).

---

## 1. Expressions, equations, inequalities

- Expand/factorise; solve linear and quadratic equations as taught.
- Represent simple inequalities on a **number line**; solve linear inequalities.

---

## 2. Graphs and relationships

- Interpret **gradient** and **intercept** for **y = mx + c**.
- Sketch and read **non-linear** graphs required at your tier (including **functions** topic links).

---

## 3. Sequences and patterns

- Find **nth term** rules for arithmetic patterns; recognise other patterns if required.

---

## Common misconceptions

- Treating **≤** like **<** when endpoints matter.
- Sketching without marking **key points** (intercepts/turning points where relevant).

---

## Revision checklist

- [ ] Mixed algebra drill (expand/factor/solve).
- [ ] Interpret one graph question with context.
- [ ] Sequences: write nth term from first four terms.

{next_line}

---

### Reference

- [{title} ({code})]({url})
"""

    if topic == "Functions":
        return f"""# Complete Lecture: Functions ({title} {code})

**Functions** describe how one quantity depends on another—**inputs**, **outputs**, and **graphs**. Programme: [{title} ({code})]({url}).

---

## 1. Function notation

- **f(x)** meaning; substitute values; interpret **domain** and **range** at syllabus depth.

---

## 2. Graph features

- **Increasing/decreasing** intervals; **roots** where **f(x)=0**; **turning points** for quadratics/cubics as taught.

---

## 3. Transformations of graphs (if examined)

- Vertical/horizontal shifts and stretches—track **key points**.

---

## Revision checklist

- [ ] Evaluate **f(a)** including negative inputs carefully.
- [ ] Sketch a function using roots and axis intercepts.
- [ ] Link graph behaviour to an equation in one sentence.

{next_line}

---

### Reference

- [{title} ({code})]({url})
"""

    # Default: delegate to math lecture for overlapping topics by reading from math bodies
    # For Number, Coordinate Geometry, Geometry, Mensuration, Trigonometry, Transformations and Vectors, Probability, Statistics
    mapping = {
        "Number": "Number",
        "Coordinate Geometry": "Coordinate Geometry",
        "Geometry": "Geometry",
        "Mensuration": "Mensuration",
        "Trigonometry": "Trigonometry",
        "Transformations and Vectors": "Vectors and Transformations",
        "Probability": "Probability",
        "Statistics": "Statistics",
    }
    if topic in mapping:
        return lecture_math(mapping[topic], next_t, meta)

    return lecture_math("Algebra and Graphs", next_t, meta)  # fallback


def voice_intl(topic: str, next_t: str | None, meta: dict) -> str:
    if topic == "Past Papers":
        return voice_math("Past Papers", None, meta)
    if topic in ("Number", "Coordinate Geometry", "Geometry", "Mensuration", "Trigonometry", "Probability", "Statistics"):
        # reuse voice script with topic name swap
        v = voice_math(
            {"Transformations and Vectors": "Vectors and Transformations"}.get(topic, topic),
            next_t,
            meta,
        )
        return v.replace("Vectors and Transformations", topic) if topic == "Transformations and Vectors" else v
    if topic == "Algebra":
        return f"""# Voice-Over Script: Algebra ({meta['title']} {meta['code']})

**[Visual: Expand brackets animation]**

**Narrator:**  
Algebra is the toolkit for rearranging relationships—expand, factor, solve, then interpret.

---

**[Visual: Inequality on number line]**

**Narrator:**  
Watch endpoints for inequalities; shading open vs closed circles matches whether equality is allowed.

---

**[Visual: Checklist — solve, sketch, interpret]**

**Narrator:**  
{"Next: **Functions**." if next_t else "Next: past papers."}

**[Visual: End card]**
"""
    if topic == "Functions":
        return f"""# Voice-Over Script: Functions ({meta['title']} {meta['code']})

**[Visual: x-axis, y-axis, smooth curve with points marked]**

**Narrator:**  
Functions package repeated calculations: input in, output out—graphs show the whole behaviour at once.

---

**[Visual: Turning point and roots labelled]**

**Narrator:**  
Mark intercepts and turning points when sketching; examiners reward structured graphs, not doodles.

---

**[Visual: Checklist — roots, turning points, domain]**

**Narrator:**  
{"Next: **Coordinate Geometry**." if next_t else "Next: mixed revision."}

**[Visual: End card]**
"""
    return voice_math("Algebra and Graphs", next_t, meta)


def lecture_add(topic: str, next_t: str | None, meta: dict) -> str:
    code = meta["code"]
    title = meta["title"]
    url = meta["url"]
    next_line = f"**Next:** **{next_t}**." if next_t else "**Next:** timed past papers."
    if topic == "Past Papers":
        return lecture_math("Past Papers", None, meta)

    templates = {
        "Functions and Quadratics": (
            "Functions, domain/range ideas, and quadratic graphs/equations at Additional Mathematics depth.",
            "## 1. Functions\n\n- **f(x)** notation; composite **f(g(x))** and inverses **f⁻¹(x)** as taught.\n- Sketch **parabolas**; complete the square for vertex form where required.\n\n## 2. Quadratics\n\n- Discriminant **b² − 4ac** and nature of roots.\n- Solve by factorising, formula, completing the square.\n",
        ),
        "Indices Surds and Logarithms": (
            "Indices, surds, and logarithmic/exponential relationships.",
            "## 1. Indices and surds\n\n- Laws of indices; rationalise denominators involving surds.\n\n## 2. Logarithms\n\n- **log(ab) = log a + log b**; **log(a/b) = log a − log b**; **log a^k = k log a** (bases as taught).\n- Solve **a^x = b** using logarithms.\n",
        ),
        "Polynomials and Equations": (
            "Polynomial algebra, equations, and inequalities beyond linear/quadratic basics.",
            "## 1. Polynomials\n\n- Remainder/factor ideas as taught; factor theorem patterns.\n\n## 2. Equations and inequalities\n\n- Simultaneous (linear/quadratic); modulus inequalities if examined—use cases/graphs carefully.\n",
        ),
        "Coordinate Geometry and Graphs": (
            "Straight lines, lengths, midpoints, and graph features for Additional Mathematics.",
            "## 1. Lines\n\n- Parallel/perpendicular gradients; distance and midpoint.\n\n## 2. Graphs\n\n- Linear and non-linear graphs required by the syllabus; intersections by solving simultaneously.\n",
        ),
        "Circular Measure and Trigonometry": (
            "Radians, arc/sector, and trigonometric skills for non-right triangles as required.",
            "## 1. Circular measure\n\n- **s = rθ**, **A = ½ r²θ** for radians model (if examined).\n\n## 2. Trigonometry\n\n- Sine/cosine rules; identities at syllabus depth; solve equations in an interval.\n",
        ),
        "Series Binomial and Counting": (
            "Arithmetic/geometric series, binomial expansions, and counting methods.",
            "## 1. Series\n\n- nth term and sum formulas as taught; convergence ideas for infinite geometric series if included.\n\n## 2. Binomial expansion\n\n- **(a+b)^n** for positive integer **n**; general term **C(n,r)a^(n-r)b^r**.\n\n## 3. Counting\n\n- **nPr**, **nCr**; factorial principles; careful with restrictions.\n",
        ),
        "Vectors and Matrices": (
            "2D vectors and matrix tools used in Additional Mathematics.",
            "## 1. Vectors\n\n- Addition, scalar multiples, magnitude; position vectors; lines in vector form if taught.\n\n## 2. Matrices\n\n- Addition/multiplication conditions; determinants/inverses for 2×2 as taught; transformations.\n",
        ),
        "Differentiation": (
            "Gradient functions, tangents, and basic stationary value problems.",
            "## 1. Techniques\n\n- Differentiate **x^n**, sums, constant multiples; chain/product/quotient rules at syllabus depth.\n\n## 2. Applications\n\n- Gradients and tangents; increasing/decreasing; **stationary points** classified by **second derivative** or sign test if taught.\n",
        ),
        "Integration": (
            "Antiderivatives and basic definite integrals linked to area.",
            "## 1. Techniques\n\n- Integrate **x^n** (n ≠ −1); recognise **∫ f'(x) f(x)^n dx** patterns if taught.\n\n## 2. Definite integrals\n\n- Area under a curve (respecting sign); interpret **negative** area carefully.\n",
        ),
    }
    intro, body = templates[topic]
    return f"""# Complete Lecture: {topic} ({title} {code})

This lecture covers **{intro}** Programme: [{title} ({code})]({url}).

---

{body}

---

## Common misconceptions

- Applying **log laws** outside the domain where logs are defined.
- Matrix multiplication **order** matters: **AB** vs **BA** is not generally interchangeable.

---

## Revision checklist

- [ ] One mixed skills sheet for this chapter.
- [ ] One past-paper question requiring **explanation** of method.
- [ ] Check non-calculator paper skills if your series includes a non-calculator component.

{next_line}

---

### Reference

- [{title} ({code})]({url})
"""


def voice_add(topic: str, next_t: str | None, meta: dict) -> str:
    if topic == "Past Papers":
        return voice_math("Past Papers", None, meta)
    nxt = f"Next: **{next_t}**." if next_t else "Next: timed papers."
    return f"""# Voice-Over Script: {topic} ({meta['title']} {meta['code']})

**[Visual: Title card — {topic}]**

**Narrator:**  
Additional Mathematics moves faster than IGCSE Mathematics—definitions are tighter and algebra is heavier. Build fluency with **exact** steps.

---

**[Visual: Worked example with highlighted rules]**

**Narrator:**  
Name the rule you used before you substitute numbers—examiners reward clear reasoning.

---

**[Visual: Non-calculator reminder icon]**

**Narrator:**  
If your syllabus includes a non-calculator paper, practise indices, surds, and exact trig values until they are automatic.

---

**[Visual: Checklist]**

**Narrator:**  
{nxt}

**[Visual: End card]**
"""


def lecture_stat(topic: str, next_t: str | None, meta: dict) -> str:
    code = meta["code"]
    title = meta["title"]
    url = meta["url"]
    next_line = f"**Next:** **{next_t}**." if next_t else "**Next:** timed papers."
    if topic == "Past Papers":
        return lecture_math("Past Papers", None, meta)

    blocks = {
        "Planning and Data Collection": """## 1. Types of data

- **Categorical** vs **numerical** (discrete/continuous).

## 2. Sampling

- **Population** vs **sample**; bias and convenience sampling pitfalls.
- Simple random ideas; systematic/stratified at outline level if taught.

## 3. Questionnaire design

- Clear questions, avoiding leading wording; ethical considerations.
""",
        "Presentation of Data": """## 1. Tables and charts

- Frequency tables; **bar charts**, **histograms**, **stem-and-leaf**, **cumulative frequency** as taught.

## 2. Choosing a display

- Match chart type to variable type; avoid misleading scales.
""",
        "Averages and Spread": """## 1. Averages

- Mean/median/mode; choose appropriate average for skewed data.

## 2. Spread

- Range, IQR, standard deviation ideas at syllabus depth.

## 3. Grouped data

- Use midpoints for estimating mean; interpret limitations.
""",
        "Probability": """## 1. Probability rules

- Complement rule; addition for mutually exclusive events; multiplication for independent events.

## 2. Tree and Venn diagrams

- Translate word problems into a diagram before calculating.
""",
        "Discrete and Continuous Models": """## 1. Discrete random variables

- Probability distribution tables; **E(X)** and **Var(X)** as taught.

## 2. Continuous models (if examined)

- Normal distribution ideas linked to mean and spread; use of tables/calculator functions per paper rules.
""",
        "Correlation and Regression": """## 1. Scatter diagrams

- Describe correlation strength and direction.

## 2. Regression line (if examined)

- Least squares interpretation; prediction cautions (**extrapolation**).
""",
        "Sampling and Uncertainty": """## 1. Variability

- Sampling variation; why two samples differ.

## 2. Estimation and confidence ideas (if examined)

- Interpret intervals at a basic level as taught—avoid overclaiming causation from correlation.
""",
    }
    return f"""# Complete Lecture: {topic} ({title} {code})

This lecture supports **IGCSE Statistics** skills for **{code}**. Programme: [{title} ({code})]({url}).

---

{blocks[topic]}

---

## Common misconceptions

- Correlation **does not** prove causation.
- **Mean** is sensitive to **outliers**; always interpret with context.

---

## Revision checklist

- [ ] One full question on presentation + interpretation.
- [ ] One probability model drawn as a tree or table.
- [ ] One “explain in context” sentence that uses data evidence.

{next_line}

---

### Reference

- [{title} ({code})]({url})
"""


def voice_stat(topic: str, next_t: str | None, meta: dict) -> str:
    if topic == "Past Papers":
        return voice_math("Past Papers", None, meta)
    nxt = f"Next: **{next_t}**." if next_t else "Next: timed papers."
    return f"""# Voice-Over Script: {topic} ({meta['title']} {meta['code']})

**[Visual: Data charts montage — {topic}]**

**Narrator:**  
Statistics is about honest summaries: collect carefully, display clearly, and interpret without overstating.

---

**[Visual: “Context” caption on graph]**

**Narrator:**  
Always connect numbers back to the scenario—**what does it mean for the claim in the question?**

---

**[Visual: Checklist]**

**Narrator:**  
{nxt}

**[Visual: End card]**
"""


def write_pair(folder: Path, topic: str, lecture: str, voice: str) -> None:
    tdir = folder / topic
    tdir.mkdir(parents=True, exist_ok=True)
    (tdir / "01_Lecture.md").write_text(lecture.rstrip() + "\n", encoding="utf-8")
    (tdir / "02_VoiceOver.md").write_text(voice.rstrip() + "\n", encoding="utf-8")


def main() -> None:
    # --- Standard IGCSE Mathematics (0580 / 0980 / US 0444) ---
    for folder_name, code, title, slug in SYLLABI:
        folder = BASE / folder_name
        if not folder.is_dir():
            continue
        tier_note = ""
        if code == "0980":
            tier_note = (
                "\n---\n\n## Note on 9–1 grading\n\n"
                "Your final grade scale differs from **0580**, but the mathematical skills overlap strongly—"
                "still confirm **tier** entry and **paper** rules on your statement of entry.\n"
            )
        if code == "0444":
            tier_note = (
                "\n---\n\n## Note on US specification\n\n"
                "The **US** route may emphasise slightly different contexts; always align revision to the **0444** "
                "syllabus and specimen materials.\n"
            )
        meta = {
            "code": code,
            "title": title,
            "url": cambridge_url(slug),
            "tier_note": tier_note,
        }
        for topic, next_t in MATH_TOPICS:
            lec = lecture_math(topic, next_t, meta)
            voc = voice_math(topic, next_t, meta)
            write_pair(folder, topic, lec, voc)
        # remove subject-level gitkeep if present
        gk = folder / ".gitkeep"
        if gk.exists():
            gk.unlink()

    # --- International Mathematics 0607 ---
    folder = BASE / "International Mathematics - 0607"
    if folder.is_dir():
        meta = {
            "code": "0607",
            "title": "Cambridge IGCSE International Mathematics",
            "url": cambridge_url("cambridge-igcse-international-mathematics-0607"),
            "tier_note": "",
        }
        for topic, next_t in INTL_TOPICS:
            # Use math lectures for overlapping topics for consistency
            if topic in (
                "Number",
                "Coordinate Geometry",
                "Geometry",
                "Mensuration",
                "Trigonometry",
                "Probability",
                "Statistics",
            ):
                lec = lecture_math(
                    {"Transformations and Vectors": "Vectors and Transformations"}.get(topic, topic),
                    next_t,
                    meta,
                )
                lec_lines = lec.splitlines()
                lec_lines[0] = f"# Complete Lecture: {topic} ({meta['title']} {meta['code']})"
                lec = "\n".join(lec_lines)
            elif topic == "Transformations and Vectors":
                lec = lecture_math("Vectors and Transformations", next_t, meta)
                lec = lec.splitlines()
                lec[0] = f"# Complete Lecture: Transformations and Vectors ({meta['title']} {meta['code']})"
                lec = "\n".join(lec)
            elif topic == "Algebra":
                lec = lecture_intl("Algebra", next_t, meta)
            elif topic == "Functions":
                lec = lecture_intl("Functions", next_t, meta)
            elif topic == "Past Papers":
                lec = lecture_math("Past Papers", None, meta)
            else:
                lec = lecture_intl(topic, next_t, meta)

            if topic in (
                "Number",
                "Coordinate Geometry",
                "Geometry",
                "Mensuration",
                "Trigonometry",
                "Probability",
                "Statistics",
            ):
                voc = voice_math(
                    {"Transformations and Vectors": "Vectors and Transformations"}.get(topic, topic),
                    next_t,
                    meta,
                )
                voc_lines = voc.splitlines()
                voc_lines[0] = f"# Voice-Over Script: {topic} ({meta['title']} {meta['code']})"
                voc = "\n".join(voc_lines)
            elif topic == "Transformations and Vectors":
                voc = voice_math("Vectors and Transformations", next_t, meta)
                voc = voc.splitlines()
                voc[0] = f"# Voice-Over Script: Transformations and Vectors ({meta['title']} {meta['code']})"
                voc = "\n".join(voc)
            elif topic in ("Algebra", "Functions"):
                voc = voice_intl(topic, next_t, meta)
            elif topic == "Past Papers":
                voc = voice_math("Past Papers", None, meta)
                voc = voc.splitlines()
                voc[0] = f"# Voice-Over Script: Past Papers and Examination Technique ({meta['title']} {meta['code']})"
                voc = "\n".join(voc)
            else:
                voc = voice_intl(topic, next_t, meta)

            write_pair(folder, topic, lec, voc)
        gk = folder / ".gitkeep"
        if gk.exists():
            gk.unlink()

    # --- Additional Mathematics 0606 ---
    folder = BASE / "Mathematics Additional - 0606"
    if folder.is_dir():
        meta = {
            "code": "0606",
            "title": "Cambridge IGCSE Mathematics - Additional",
            "url": cambridge_url("cambridge-igcse-mathematics-additional-0606"),
            "tier_note": "",
        }
        for topic, next_t in ADD_TOPICS:
            lec = lecture_add(topic, next_t, meta)
            if topic == "Past Papers":
                lec = lecture_math("Past Papers", None, meta)
            voc = voice_add(topic, next_t, meta)
            if topic == "Past Papers":
                voc = voice_math("Past Papers", None, meta)
                voc = voc.splitlines()
                voc[0] = f"# Voice-Over Script: Past Papers and Examination Technique ({meta['title']} {meta['code']})"
                voc = "\n".join(voc)
            write_pair(folder, topic, lec, voc)
        gk = folder / ".gitkeep"
        if gk.exists():
            gk.unlink()

    # --- Statistics 0479 ---
    folder = BASE / "Statistics - 0479"
    if folder.is_dir():
        meta = {
            "code": "0479",
            "title": "Cambridge IGCSE Statistics",
            "url": cambridge_url("cambridge-igcse-statistics-0479"),
            "tier_note": "",
        }
        for topic, next_t in STAT_TOPICS:
            lec = lecture_stat(topic, next_t, meta)
            if topic == "Past Papers":
                lec = lecture_math("Past Papers", None, meta)
            voc = voice_stat(topic, next_t, meta)
            if topic == "Past Papers":
                voc = voice_math("Past Papers", None, meta)
                voc = voc.splitlines()
                voc[0] = f"# Voice-Over Script: Past Papers and Examination Technique ({meta['title']} {meta['code']})"
                voc = "\n".join(voc)
            write_pair(folder, topic, lec, voc)
        gk = folder / ".gitkeep"
        if gk.exists():
            gk.unlink()


if __name__ == "__main__":
    main()
