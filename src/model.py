# Purpose of model.py
# 1: Load processed returns
# 2: Estimate mean vector mu and covariance matrix sigma
# 3: Validate the covariance matrix
# 4: Make parameters reusable by later modules

import numpy as np
import pandas as pd
import os


# -----------------------------
# Paths
# -----------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RETURNS_PATH = os.path.join(BASE_DIR, "data", "processed", "returns.csv")

print("DEBUG – loading:", RETURNS_PATH)


# -----------------------------
# Load data
# -----------------------------
def load_returns():
    """
    Load processed log returns.
    """
    returns = pd.read_csv(RETURNS_PATH, index_col=0, parse_dates=True)
    return returns


# -----------------------------
# Estimate parameters
# -----------------------------
def estimate_mean_cov(returns: pd.DataFrame):
    """
    Estimate mean vector and covariance matrix of returns.
    """
    mu = returns.mean().values      # Mean return vector
    sigma = returns.cov().values    # Covariance matrix
    return mu, sigma


# -----------------------------
# Diagnostics
# -----------------------------
def check_covariance(sigma: np.ndarray):
    """
    Basic covariance matrix diagnostics.
    """
    if not np.allclose(sigma, sigma.T):
        raise ValueError("Covariance matrix is not symmetric.")

    eigenvalues = np.linalg.eigvals(sigma)
    if np.any(eigenvalues < 0):
        raise ValueError("Covariance matrix is not positive semi-definite.")

    return True


# -----------------------------
# Main
# -----------------------------
def main():
    returns = load_returns()
    mu, sigma = estimate_mean_cov(returns)

    check_covariance(sigma)

    print("Model estimation complete.")
    print(f"Number of assets: {len(mu)}")
    print("Mean vector (mu):")
    print(mu)
    print("\nCovariance matrix (sigma):")
    print(sigma)


if __name__ == "__main__":
    main()
