# Complete Lecture: Programming Concepts (Cambridge International O Level Computer Science 2210)

This lecture covers **variables**, **data types**, **control structures**, **procedures**, **functions**, **arrays**, and **good programming practice** for **2210** (aligned with your **language** track—often **high-level pseudocode** or a specified language in exams). Programme: [Cambridge 2210](https://www.cambridgeinternational.org/programmes-and-qualifications/cambridge-o-level-computer-science-2210/).

---

## 1. Variables, constants, and data types

- **Variable:** named location holding a value that can change.
- **Constant:** value fixed after declaration (readability and fewer mistakes).

Common types at O Level:
- **Integer**, **real** (floating-point), **string**, **Boolean**, **character**.

Choose types so operations are **valid** (e.g. do not rely on exact equality for **reals** without care).

---

## 2. Operators and expressions

- **Arithmetic:** `+`, `-`, `*`, `/`, `MOD`, `DIV` (understand **integer division** vs real division per syllabus).
- **Relational:** `=`, `<>`, `<`, `>`, `<=`, `>=`.
- **Logical:** `AND`, `OR`, `NOT` (often tested with conditions and Boolean algebra links).

**Precedence:** brackets clarify intent and prevent errors.

---

## 3. Selection and iteration

- **IF / ELSE** and nested selection for multi-way logic (some syllabi use **CASE** / **SWITCH**—use your notation).
- **FOR** loops for definite counts; **WHILE** / **REPEAT…UNTIL** for indefinite loops—ensure **termination** (update loop variable or condition).

---

## 4. Arrays (1D and 2D if required)

- **Index** from 0 or 1 per specification—**critical** in exam code.
- **Traversals:** counting, searching, finding min/max, **accumulator** for totals.
- **2D arrays:** rows/columns, nested loops.

---

## 5. Procedures and functions

- **Procedure:** named block performing a task; may **return** nothing explicit.
- **Function:** returns a **value** to the caller.
- **Parameters** (by value vs by reference if examined): understand **scope**—local vs global variables.

---

## 6. Structured programming and readability

- **Indentation**, meaningful names, **comments** for *why* not obvious *what*.
- Avoid **spaghetti** logic—keep modules short and testable.

---

## 7. Testing mindset

- **Normal**, **boundary**, and **invalid** test data.
- Desk-check with **trace tables** before claiming correctness.

---

## Common misconceptions

- `=` can mean **assignment** in code but **comparison** in different contexts—follow your notation.
- Loops and arrays: **index out of range** is a classic error.
- **Efficiency** at O Level usually means **clear logic**, not micro-optimisation.

---

## Revision checklist

- [ ] Declare types and sizes consistently with the syllabus.
- [ ] Write nested conditions without redundant checks.
- [ ] Use arrays with correct bounds in loops.
- [ ] Separate procedures for distinct sub-tasks in longer questions.

**Next:** Data Representation.

---

### Reference

- [Cambridge 2210](https://www.cambridgeinternational.org/programmes-and-qualifications/cambridge-o-level-computer-science-2210/)
