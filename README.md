
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

- `T`: number of time periods (hours)
- `p_t`: price at time `t`
- `l_t`: load served at time `t`
- `s_t`: load shed at time `t`
- `f_t`: load shifted out at time `t`
- `f_{t-1}`: load shifted in from previous time
- `d_t`: baseline demand at time `t`
- `c_s`: cost per unit of shed load
- `c_f`: cost per unit of shifted load

### 🎯 Objective Function

Minimize the total cost:

```
Minimize:  ∑ [ p_t * l_t + c_s * s_t + c_f * f_t ]
```

### 📏 Constraints

**1. Load Balance (with shift-in and shift-out):**

```
l_t = d_t - s_t - f_t + f_{t-1}   for all t
```

**2. Load Limits:**

```
L_min ≤ l_t ≤ L_max
```

**3. Shift Recovery:**

```
∑ f_t = ∑ f_{t-1}
```

---

## 🧰 Dependencies

- Python 3.8+
- [Pyomo](http://www.pyomo.org/)
- matplotlib
- numpy

Install them with:

```bash
pip install pyomo matplotlib numpy
```

Install a solver (e.g., **GLPK**):

```bash
brew install glpk   # on macOS
```

---

## 🚀 How to Run

```bash
python optimize_dr.py
```

The script will:
- Solve the model using Pyomo
- Plot demand vs. price with a second Y-axis
- Save the figure as `demand_response_optimization.png`

---

## 📊 Outputs

- Optimized demand profile
- Bar chart of shed and deferred load
- Second y-axis showing price
- PNG figure saved to the project directory

---

## ✨ Future Enhancements

- Add battery storage optimization
- Integrate real-time electricity prices from ERCOT/NYISO APIs
- Support multi-day or rolling horizon scheduling
- Include emissions minimization or carbon pricing

---

## 📜 License

MIT License

---

## 👤 Author

**Your Name**  
Email: yourname@example.com  
GitHub: [@yourusername](https://github.com/yourusername)
