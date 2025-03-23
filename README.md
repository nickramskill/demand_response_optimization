# Data Center Demand Response Optimization

This project models and solves a **linear optimization problem** to minimize electricity costs for a data center located in the Houston zone of ERCOT (uses ERCOT Houston Hub prices from 3/1/2025)


## Problem Statement

The goal is to **optimize the hourly power consumption** of a data center over a 24-hour period by:

- Shifting load to lower-price hours  
- Shedding non-critical load (at a cost)  
- Responding to time-varying electricity prices  
- Enforcing operational constraints (min/max load)  
- Ensuring all shifted load is eventually recovered


## Model Formulation

**Objective:**
Minimize total cost:
\[
\sum_{t=1}^{T} \left( p_t \cdot l_t + c_s \cdot s_t + c_f \cdot f_t \right)
\]

Where:
- \( p_t \): electricity price at hour \( t \)  
- \( l_t \): load consumed at hour \( t \)  
- \( s_t \): load shed at hour \( t \)  
- \( f_t \): load shifted from hour \( t \)  
- \( c_s \): penalty for shedding  
- \( c_f \): cost for shifting  

**Subject to:**
- Load balance with shift-in and shift-out:
  \[
  l_t = d_t - s_t - f_t + f_{t-1}
  \]
- Min/max load bounds:
  \[
  L_{\min} \leq l_t \leq L_{\max}
  \]
- Shift recovery:
  \[
  \sum f_t = \sum f_{t-1}
  \]

-- 

