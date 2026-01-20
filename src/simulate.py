import numpy as np
import pandas as pd
import os
from model import load_returns, estimate_mean_cov
# From our modle python file, we need to import our load_returns and estimate_mean_cov functions

# Configuration

N_SIMULATIONS = 10000

# Portfolio weights

def equal_weight_portfolio(n_assets: int):

    """

    Create equal weight portfolio.
    """

    return np.ones(n_assets) / n_assets

#Monte Carlo Simulation

def simulate_portfolio_returns(mu, sigma, weights, n_simulations):

    """
    Simulate portfolio returns using a multivariate normal model.
    """

    simulated_asset_returns = np.random.multivariate_normal(
        mean = mu,
        cov = sigma,
        size = n_simulations
    )

    #Portfolio returns: R_p = w'R

    portoflio_returns = simulated_asset_returns @ weights

    return portoflio_returns

# Main

def main():

    returns = load_returns()
    mu, sigma = estimate_mean_cov(returns)

    n_assets = len(mu)
    weights = equal_weight_portfolio(n_assets)

    portfolio_returns = simulate_portfolio_returns(
        mu, sigma, weights, N_SIMULATIONS
    )

    print("Monte Carlo simulation complete.")
    print(f"Simulations run: {N_SIMULATIONS}")
    print(f"Mean portfolio return: {portfolio_returns.mean():.6f}")
    print(f"Portfolio volatility: {portfolio_returns.std():.6f}")

if __name__ == "__main__":
    main()
    