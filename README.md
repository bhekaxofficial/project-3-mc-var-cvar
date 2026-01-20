# Monte Carlo Portfolio VaR & CVaR with Stress Testing

## Overview
This project implements a **Monte Carlo–based portfolio risk model** to estimate **Value at Risk (VaR)** and **Conditional Value at Risk (CVaR)** for a diversified equity portfolio.  
It combines statistical modelling, simulation, historical validation, and stress testing to analyse downside risk under normal and adverse market conditions.

The project is designed to demonstrate **practical quantitative risk modelling**, rather than purely theoretical results.

---

## Project Structure
project-3-mc-var-cvar/
├── README.md
├── data/
│ ├── raw/
│ │ └── prices.csv
│ └── processed/
│ └── returns.csv
├── src/
│ ├── data_pipeline.py
│ ├── model.py
│ ├── simulate.py
│ ├── risk.py
│ └── stress.py
├── figures/
│
│ 
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
\[
r_t = \log\left(\frac{P_t}{P_{t-1}}\right)
\]

Raw price data is stored unchanged, while all modelling uses processed returns to ensure reproducibility.

---

## Methodology

### 1. Data Pipeline (`data_pipeline.py`)
- Downloads adjusted close prices
- Computes daily log returns
- Separates raw and processed data

---

### 2. Return Model (`model.py`)
- Estimates the mean return vector \( \mu \)
- Estimates the covariance matrix \( \Sigma \)
- Validates covariance matrix properties
- Defines the multivariate return model:
\[
R \sim \mathcal{N}(\mu, \Sigma)
\]

---

### 3. Monte Carlo Simulation (`simulate.py`)
- Simulates 10,000 joint asset return scenarios
- Constructs portfolio returns using equal weights
- Produces a full empirical distribution of portfolio outcomes

---

### 4. Risk Measurement (`risk.py`)
- Computes:
  - 95% and 99% VaR
  - 95% and 99% CVaR
- Computes historical VaR for comparison
- Visualises tail risk using return distributions with VaR/CVaR thresholds

---

### 5. Stress Testing (`stress.py`)
- Applies adverse market scenarios:
  - **Volatility stress:** sharp increase in market uncertainty
  - **Correlation stress:** diversification breakdown
- Re-estimates VaR and CVaR under stress
- Compares baseline and stressed tail risk

---

## Key Results
- Monte Carlo VaR and CVaR estimates are economically realistic
- Volatility stress significantly increases tail losses
- Correlation stress highlights the fragility of diversification
- Visual diagnostics confirm correct tail-risk behaviour

---

## Key Takeaways
- VaR measures loss thresholds at a given confidence level
- CVaR captures the severity of extreme tail losses
- Monte Carlo simulation enables forward-looking risk analysis
- Stress testing is essential for understanding crisis behaviour

---

## Possible Extensions
- Heavy-tailed return distributions (Student-t)
- Time-varying volatility (GARCH)
- Multi-day horizon VaR
- Factor-based covariance models

---

## Author
Independent quantitative finance project demonstrating applied risk modelling, simulation, and stress testing.
