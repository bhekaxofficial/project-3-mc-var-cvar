import numpy as np

from model import load_returns, estimate_mean_cov
from simulate import simulate_portfolio_returns, equal_weight_portfolio
from risk import value_at_risk, conditional_value_at_risk

# Stress transformations

def stress_volatility(sigma, scale):

    """
    Apply a volatility stress by scaling the covariance matrix.
    """
    return sigma * scale**2

def stress_correlation(sigma, rho):
    """
    Increase correlations while keeping individual variances unchanged.
    """

    std = np.sqrt(np.diag(sigma))
    corr = sigma / np.outer(std, std)

    stressed_corr = rho * corr + (1-rho) * np.eye(len(std))
    stressed_sigma = np.outer(std, std) * stressed_corr

    return stressed_sigma

# Main

def main():

    # Load model
    returns = load_returns()
    mu, sigma = estimate_mean_cov(returns)

    weights = equal_weight_portfolio(len(mu))
    n_sim = 10000
    alpha = 0.99

    # Baseline risk

    base_returns = simulate_portfolio_returns(mu, sigma, weights, n_sim)
    base_var = value_at_risk(base_returns, alpha)
    base_cvar = conditional_value_at_risk(base_returns, alpha)

    # Volatility stress

    sigma_vol = stress_volatility(sigma, scale = 2.0)
    vol_returns = simulate_portfolio_returns(mu, sigma_vol, weights, n_sim)
    vol_var = value_at_risk(vol_returns, alpha)
    vol_cvar = conditional_value_at_risk(vol_returns, alpha)

    # Correlation stress

    sigma_corr = stress_correlation(sigma, rho=0.7)
    corr_returns = simulate_portfolio_returns(mu, sigma_corr, weights, n_sim)
    corr_var = value_at_risk(corr_returns, alpha)
    corr_cvar = conditional_value_at_risk(corr_returns, alpha)

    # Results

    print("99% Risk Comparison\n")

    print(f"Baseline VaR: {base_var:.4f} | CVaR: {base_cvar:.4f})")
    print(f"Volatility Stress: {vol_var:.4f} | CVaR: {vol_cvar:.4f}")
    print(f"Correlation Stress: {corr_var:.4f} | CVaR: {corr_cvar:.4f}")


if __name__ == "__main__":
    main()