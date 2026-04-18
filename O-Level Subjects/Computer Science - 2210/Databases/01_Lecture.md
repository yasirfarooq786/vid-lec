# Complete Lecture: Databases (Cambridge International O Level Computer Science 2210)

This lecture covers **relational databases**, **tables**, **keys**, **relationships**, **normalisation ideas**, and **SQL-style** queries at **O Level**. Programme: [Cambridge 2210](https://www.cambridgeinternational.org/programmes-and-qualifications/cambridge-o-level-computer-science-2210/).

---

## 1. Why databases?

Compared to flat files, DBMS provides:
- **Structured** storage with **integrity** rules.
- **Concurrent** access controls (conceptual).
- **Query** languages for flexible retrieval.

---

## 2. Tables, fields, records

- **Table** (relation) = entity type (e.g. Student, Book).
- **Field** (attribute/column) = property (e.g. StudentID, Surname).
- **Record** (row/tuple) = one instance.

---

## 3. Keys

- **Primary key:** uniquely identifies each record (must be unique, non-null—per syllabus rules).
- **Foreign key:** field referencing a primary key in another table—enforces **referential integrity** between related tables.

---

## 4. Relationships

- **One-to-many** (common): one parent, many children (e.g. one Customer, many Orders).
- **Many-to-many** often implemented via a **link** table (two foreign keys).

---

## 5. Data validation in databases

- **Data types**, **length**, **range checks**, **required fields**, **lookup** tables.
- **Validation** reduces garbage entering the system (link to Algorithm topic vocabulary).

---

## 6. SQL (typical O Level commands)

Be able to read/write simple statements (syntax per specimen papers):
- **SELECT** … **FROM** … **WHERE**
- **INSERT INTO** … **VALUES**
- **UPDATE** … **SET** … **WHERE**
- **DELETE FROM** … **WHERE**

Understand **WHERE** filters rows; avoid **DELETE/UPDATE** without conditions unless intended.

---

## 7. Normalisation (introductory)

Goals: reduce **redundancy** and **update anomalies** by splitting tables sensibly. At O Level, explain **why** duplication is risky even if full formal proofs are not required.

---

## Common misconceptions

- **Primary key** is not “any unique field”—it is the **chosen** identifier for the table.
- **Foreign key** values must exist in the referenced table (integrity).
- SQL **SELECT** does not change data; **INSERT/UPDATE/DELETE** do.

---

## Revision checklist

- [ ] Draw a two-table relationship with PK/FK labelled.
- [ ] Write SELECT queries with WHERE for scenarios.
- [ ] Explain one insert/update that could break referential integrity.
- [ ] Give one reason to split repeated data into separate tables.

**Next:** Security and Ethics.

---

### Reference

- [Cambridge 2210](https://www.cambridgeinternational.org/programmes-and-qualifications/cambridge-o-level-computer-science-2210/)
