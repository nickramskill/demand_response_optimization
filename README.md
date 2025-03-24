
# Data Center Demand Response Optimization

Optimize the hourly power consumption of a data center in the ERCOT Houston Hub load zone over a 24-hour period by:

- Shifting load to lower-price hours  
- Shedding non-critical load (at a cost)  
- Responding to time-varying electricity prices  
- Enforcing operational constraints (min/max load)  
- Ensuring all shifted load is eventually recovered

---

## Optimization Model

- `time_axis`: time intervals (hours)
- `price_data`: ERCOT Houston Hub price 
- `load_optimized`: optimized load
- `load_shed`: load shed 
- `load_defer`: load deferred 
- `base_load`: baseline load
- `shed_cost`: cost per unit of shed load
- `defer_cost`: cost per unit of shifted load
- `min_load`: minimum operational load of the data center
- `max_load`: maximum operational load of the data center

### Objective Function

Minimize the total cost:

```
Minimize:  ∑ [ price_data[t] * load_optimized[t] + shed_cost * load_shed[t] + load_cost * load_defer[t] ]
```

### Constraints

**1. Load Balance:**

```
load_optimized[t] = base_load[t] - load_shed[t] - load_defer[t] + load_defer[t-1] for all t
```

**2. Load Limits:**

```
min_load ≤ load_optimized ≤ max_load
```

**3. Deferred Load Recovery:**

```
∑ load_defer[t] = ∑ load_defer[t-1]
```

---

## Notes
- Python 3.12.8
- Pyomo to formulate the optimization model and cbc as the solver
- Create venv and install requirements.txt
- Run as: python demand_response_optimization.py