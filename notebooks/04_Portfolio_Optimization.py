"""04_Portfolio_Optimization.py - Portfolio Optimization"""
import numpy as np
import pandas as pd
from scipy.optimize import minimize

class PortfolioOptimizationNotebook:
    def __init__(self, returns_df: pd.DataFrame):
        self.returns = returns_df
        self.cov_matrix = returns_df.cov()
        self.mean_returns = returns_df.mean()
    
    def calculate_portfolio_stats(self, weights: np.ndarray) -> tuple:
        """Calculate portfolio return and volatility."""
        port_return = np.dot(weights, self.mean_returns)
        port_vol = np.sqrt(np.dot(weights, np.dot(self.cov_matrix, weights)))
        sharpe_ratio = port_return / port_vol if port_vol > 0 else 0
        return port_return, port_vol, sharpe_ratio
    
    def optimize_portfolio(self, target_return: float = None) -> Dict:
        """Optimize portfolio using constraint methods."""
        n_assets = len(self.mean_returns)
        constraints = ({'type': 'eq', 'fun': lambda w: np.sum(w) - 1},)
        bounds = tuple((0, 1) for _ in range(n_assets))
        init_guess = np.array([1/n_assets] * n_assets)
        
        def neg_sharpe(w):
            _, _, sharpe = self.calculate_portfolio_stats(w)
            return -sharpe
        
        result = minimize(neg_sharpe, init_guess, method='SLSQP', bounds=bounds, constraints=constraints)
        ret, vol, sharpe = self.calculate_portfolio_stats(result.x)
        return {'weights': result.x, 'return': ret, 'volatility': vol, 'sharpe': sharpe}

def main():
    print("Portfolio Optimization")

if __name__ == "__main__":
    from typing import Dict
    main()
