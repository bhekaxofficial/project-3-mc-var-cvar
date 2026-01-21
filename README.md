# Monte Carlo Portfolio VaR & CVaR with Stress Testing

## Overview
This project implements a **Monte Carlo–based portfolio risk framework** to estimate **Value at Risk (VaR)** and **Conditional Value at Risk (CVaR)** for a multi-asset equity portfolio.

The objective is not theoretical elegance, but **decision-relevant risk measurement**.  
The model is built to answer a practical question faced by portfolio managers and risk desks:

> *How bad can losses get, how severe are they beyond the threshold, and how does that change when markets break?*

The framework integrates statistical estimation, joint-distribution simulation, tail-risk diagnostics, and explicit stress testing to evaluate downside exposure under both normal and adverse market regimes.

---

## Project Structure
```text
project-3-mc-var-cvar/
├── README.md
├── data/
│   ├── raw/
│   │   └── prices.csv
│   └── processed/
│       └── returns.csv
├── src/
│   ├── data_pipeline.py
│   ├── model.py
│   ├── simulate.py
│   ├── risk.py
│   └── stress.py
├── figures/
└── report/
    ├── main.tex
    └── notes.md


---

## Data
- **Assets:** AAPL, MSFT, GOOGL, AMZN, JPM, JNJ, XOM, SPY  
- **Frequency:** Daily  
- **Period:** 2015–2024  
- **Returns:** Log returns  

Log returns are computed as:

$$
r_t = \log\left(\frac{P_t}{P_{t-1}}\right)
$$

Raw prices are preserved unchanged.  
All modelling and simulation operate exclusively on processed return data to ensure **reproducibility, auditability, and clean separation between data ingestion and modelling logic**.

---

## Methodology

### 1. Data Pipeline (`data_pipeline.py`)
- Downloads adjusted close prices
- Computes daily log returns
- Enforces a strict raw vs processed data separation
- Outputs clean return matrices for downstream modelling

---

### 2. Return Model (`model.py`)
- Estimates the mean return vector \( \mu \)
- Estimates the covariance matrix \( \Sigma \)
- Validates positive semi-definiteness and numerical stability
- Defines the joint return process as:
  
$$
R \sim \mathcal{N}(\mu, \Sigma)
$$

This specification provides a transparent baseline for understanding **pure correlation-driven diversification effects** before introducing heavier-tailed extensions.

---

### 3. Monte Carlo Simulation (`simulate.py`)
- Simulates 10,000 joint return scenarios
- Constructs portfolio returns using equal weights
- Produces a full empirical distribution of portfolio P&L
- Enables forward-looking risk estimation beyond historical samples

---

### 4. Risk Measurement (`risk.py`)
- Computes:
  - 95% and 99% VaR
  - 95% and 99% CVaR
- Computes historical VaR for benchmarking
- Visualises tail losses with explicit VaR and CVaR cutoffs

The distinction between **threshold risk (VaR)** and **severity risk (CVaR)** is made explicit and quantified.

---

### 5. Stress Testing (`stress.py`)
- Applies explicit adverse scenarios:
  - **Volatility stress:** sharp regime-shift increase in uncertainty
  - **Correlation stress:** breakdown of diversification assumptions
- Re-estimates VaR and CVaR under stressed dynamics
- Compares baseline vs stressed tail exposure

This isolates **what actually drives tail risk when markets dislocate**.

---

## Key Results
- Baseline Monte Carlo VaR and CVaR are economically plausible
- Volatility shocks dominate tail-risk expansion
- Correlation stress reveals how quickly diversification benefits decay
- CVaR responds more aggressively than VaR under stress, highlighting tail severity risk
- Visual diagnostics confirm correct extreme-loss behaviour

---

## Key Takeaways
- VaR answers *“how bad, at a threshold”*
- CVaR answers *“how bad, on average, once things go wrong”*
- Monte Carlo simulation enables forward-looking risk analysis
- Stress testing is non-negotiable for real-world risk management
- Diversification is conditional — not guaranteed

---

## Possible Extensions
- Heavy-tailed return models (Student-t)
- Time-varying volatility (GARCH / stochastic volatility)
- Multi-day horizon VaR and CVaR
- Factor-based covariance estimation
- Regime-switching stress scenarios

---

## Author
**Bheka Mabika**

This project represents my approach to quantitative risk analysis: **practical, model-driven, and market-aware**.  
It is built with the mindset of a risk or trading desk — focusing on tail behaviour, model assumptions, and stress outcomes rather than headline statistics.

The goal is to develop tools that quantify downside exposure under both normal conditions and structural breaks, forming a foundation for more advanced portfolio construction, risk control, and systematic trading research.

