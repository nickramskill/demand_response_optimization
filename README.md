# 💡 Data Center Demand Response Optimization

This project models and solves a **linear optimization problem** to minimize electricity costs for a data center while participating in **demand response (DR)** programs. It uses **Pyomo**, a Python-based optimization modeling language.

---

## 📈 Problem Statement

The goal is to **optimize the hourly power consumption** of a data center over a 24-hour period by:

- Shifting load to lower-price hours  
- Shedding non-critical load (at a cost)  
- Responding to time-varying electricity prices  
- Enforcing operational constraints (min/max load)  
- Ensuring all shifted load is eventually recovered

---

## 🧠 Mathematical Formulation

Let:
- \( T \): number of time periods (hours)
- \( p_t \): price at time \( t \)
- \( l_t \): load served at time \( t \)
- \( s_t \): load shed at time \( t \)
- \( f_t \): load shifted out at time \( t \)
- \( f_{t-1} \): load shifted in from previous time
- \( d_t \): baseline demand at time \( t \)
- \( c_s \): cost per unit of shed load
- \( c_f \): cost per unit of shifted load

---

### 🎯 Objective Function

Minimize the total cost:

\[
\text{Minimize:} \quad \sum_{t=1}^{T} \left( p_t \cdot l_t + c_s \cdot s_t + c_f \cdot f_t \right)
\]

---

### 📏 Constraints

**1. Load Balance (with shift-in and shift-out):**

\[
l_t = d_t - s_t - f_t + f_{t-1} \quad \forall t \in \{1, \ldots, T\}
\]

**2. Load Limits:**

\[
L_{\min} \leq l_t \leq L_{\max} \quad \forall t
\]

**3. Shift Recovery (no lost deferred load):**

\[
\sum_{t=1}^{T} f_t = \sum_{t=1}^{T} f_{t-1}
\]

---

## 🧰 Dependencies

- Python 3.8+
- [Pyomo](http://www.pyomo.org/)
- matplotlib
- numpy

Install them with:

```bash
pip install pyomo matplotlib numpy