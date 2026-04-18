# Complete Lecture: Boolean Logic (Cambridge International O Level Computer Science 2210)

**Boolean logic** uses **true/false** (1/0) values with operators such as **AND**, **OR**, **NOT**, and **XOR** (if on your syllabus). It models **conditions** in programming and **gates** in hardware. Programme: [Cambridge 2210](https://www.cambridgeinternational.org/programmes-and-qualifications/cambridge-o-level-computer-science-2210/).

---

## 1. Truth values and expressions

- **Boolean variable** takes two states.
- Combine with operators; use **brackets** to show order of evaluation.

---

## 2. Truth tables

For each expression, list all input combinations and resulting output.

Typical pattern for two variables: **four rows** (00, 01, 10, 11). Three variables → **eight rows**.

---

## 3. Logic gates (symbols and behaviour)

Know standard gates (names may vary slightly by diagram style):
- **NOT** (inverter)
- **AND**, **OR**
- **NAND**, **NOR** (universal building blocks—conceptual)
- **XOR** (exclusive OR—true when inputs differ)

Be able to **read** a simple **logic circuit** diagram and derive its truth table.

---

## 4. Boolean identities (useful simplification)

Examples (verify with truth tables):
- **A AND 1 = A**; **A OR 0 = A**
- **A AND NOT A = 0**; **A OR NOT A = 1**
- **De Morgan’s laws:** `NOT (A AND B) = (NOT A) OR (NOT B)` (and the dual)

---

## 5. Link to computing

- **Conditions** in pseudocode combine comparisons with **AND/OR/NOT**.
- CPUs implement logic at gate level; understanding gates supports **low-level** comprehension questions.

---

## Common misconceptions

- **OR** in everyday English often means **exclusive** choice; Boolean **OR** is **inclusive** unless **XOR** is specified.
- **NOT** applies to a single input; do not “distribute” it blindly—use **De Morgan** correctly.

---

## Revision checklist

- [ ] Build truth tables for expressions with up to three inputs.
- [ ] Translate between logic expressions and gate diagrams.
- [ ] Apply De Morgan to simplify or match equivalent circuits.
- [ ] Link Boolean conditions to program `IF` statements.

**Next:** Databases.

---

### Reference

- [Cambridge 2210](https://www.cambridgeinternational.org/programmes-and-qualifications/cambridge-o-level-computer-science-2210/)
