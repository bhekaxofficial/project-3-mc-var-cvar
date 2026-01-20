import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

from model import load_returns, estimate_mean_cov
from simulate import simulate_portfolio_returns, equal_weight_portfolio

# Risk measures

def value_at_risk(returns: np.ndarray, alpha: float):

    """
    Compute Value at Risk (Var) at confidence level alpha.
    """

    return np.quantile(returns, 1 - alpha)

def conditional_value_at_risk(returns: np.ndarray, alpha: float):
    """
    Compute Conditional Value at risk (CVaR).
    """

    var = value_at_risk(returns, alpha)

    return returns[returns <= var].mean()

# Main

def main():

    # Load data and model

    returns = load_returns()

    mu, sigma = estimate_mean_cov(returns)

    # Portfolio setup

    weights = equal_weight_portfolio(len(mu))

    #Monte Carlo simulation

    n_simulations = 10000
    portfolio_returns = simulate_portfolio_returns(
        mu, sigma, weights, n_simulations
    )
    #  Risk levels

    alpha_95 = 0.95

    alpha_99 = 0.99

    # Risk metrics

    var_95 = value_at_risk(portfolio_returns, alpha_95)
                           
    cvar_95 = conditional_value_at_risk(portfolio_returns, alpha_95)

    var_99 = value_at_risk(portfolio_returns, alpha_99)     

    cvar_99 = conditional_value_at_risk(portfolio_returns, alpha_99)

    # Output
    # 
    print("Risk estimation complete.\n")       

    print(f"95% VaR: {var_95:.4f}")
    print(f"95% CVaR: {cvar_95:.4f}\n")  

    print(f"99% VaR: {var_99:.4f}")   
    print(f"99% CVaR: {cvar_99:.4f}") 

    # Historical portfolio returns
    historical_portfolio_returns = returns.values @ weights

    hist_var_95 = historical_var(historical_portfolio_returns, alpha_95)
    hist_var_99 = historical_var(historical_portfolio_returns, alpha_99)

    print("\nHistorical VaR comparison:")
    print(f"Historical 95% VaR: {hist_var_95:.4f}")
    print(f"Historical 99% VaR: {hist_var_99:.4f}")



    # Plots
    plot_var_cvar(portfolio_returns, var_95, cvar_95, alpha_95)
    plot_var_cvar(portfolio_returns, var_99, cvar_99, alpha_99)



#We are now going to add helper function to plot VaR and CVaR


def plot_var_cvar(returns, var, cvar, alpha):
    """
    Plot portfolio return distribution with VaR and CVaR lines (no tail shading).
    """
    plt.figure(figsize=(8, 5))

    plt.hist(returns, bins=50, density=True, alpha=0.7)

    plt.axvline(var, linestyle="--", label=f"{int(alpha*100)}% VaR")
    plt.axvline(cvar, linestyle=":", label=f"{int(alpha*100)}% CVaR")

    plt.title(f"Portfolio Return Distribution with {int(alpha*100)}% VaR / CVaR")
    plt.xlabel("Portfolio Return")
    plt.ylabel("Density")
    plt.legend()

    plt.show()

def historical_var(returns: np.ndarray, alpha:float):
    return np.quantile(returns, 1-alpha)

if __name__ == "__main__":
    main()   