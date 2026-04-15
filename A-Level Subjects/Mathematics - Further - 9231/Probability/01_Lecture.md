# Complete Lecture: Probability (Cambridge International AS & A Level Further Mathematics 9231)

**Further Probability** extends discrete models with **new distributions**, **algebra** of **expectations**, and **generating** **functions** (where examined). Programme: [Cambridge 9231](https://www.cambridgeinternational.org/programmes-and-qualifications/cambridge-international-as-and-a-level-mathematics-further-9231/).

---

## 1. Expectation algebra

**E(aX + b) = aE(X) + b**  
**Var(aX + b) = a² Var(X)**

**E(X + Y) = E(X) + E(Y)** (always, if **defined**)

**Var(X + Y) = Var(X) + Var(Y)** if **X, Y** **independent**

**E(XY) = E(X)E(Y)** if **independent**

---

## 2. Poisson distribution **Po(λ)**

**P(X = r) = e⁻λ λʳ / r!**, **r = 0,1,2,…**

**E(X) = Var(X) = λ**

**Modelling** **rare** **events** with **known** **mean** **rate**; **sum** of **independent** **Poissons** **Po(λ₁)** + **Po(λ₂)** = **Po(λ₁+λ₂)**.

---

## 3. Geometric distribution

**First** success on **k**th **trial** (versions differ on **starting** index):

**P(X = k) = (1−p)ᵏ⁻¹p** (**support** **k = 1,2,…**)

**E(X) = 1/p**, **Var(X) = (1−p)/p²** (**learn** **exact** **form** from **booklet**)

---

## 4. Continuous uniform **U(a, b)**

**f(x) = 1/(b−a)** on **[a,b]**, **0** otherwise.

**E(X) = (a+b)/2**, **Var(X) = (b−a)²/12**

---

## 5. Probability generating functions (discrete, non-negative integer)

**G_X(t) = E(t^X) = Σ p_r tʳ**

**G′(1) = E(X)**; **G″(1) + G′(1) − (G′(1))²** relates to **variance** (**check** **definition**).

**Sum** of **independent** **variables:** **G_{X+Y}(t) = G_X(t)G_Y(t)**

---

## 6. Normal approximation to Poisson / binomial

**Po(λ)** ≈ **N(λ, λ)** for **large λ** (**continuity** **correction** if **discrete** → **continuous**).

**Binomial** → **normal** with **continuity** **correction** (**conditions** on **np**, **n(1−p)**).

---

## Common mistakes

- **Independence** **assumed** **without** **justification**.  
- **Poisson** **parameter** **λ** must be **positive**; **mean** = **variance** **check**.

---

## Revision checklist

- [ ] **E** / **Var** **linear** **rules**; **independence** **conditions**.  
- [ ] **Poisson**, **geometric**, **uniform** **pmf/pdf** and **moments**.  
- [ ] **PGF** **properties** if **on** **syllabus**.  
- [ ] **Normal** **approximations** with **continuity** **correction**.

**Next:** **Statistics** (**inference**).

---

### Reference

- [Cambridge 9231](https://www.cambridgeinternational.org/programmes-and-qualifications/cambridge-international-as-and-a-level-mathematics-further-9231/)
