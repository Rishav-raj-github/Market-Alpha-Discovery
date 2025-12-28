"""
01_Market_Analysis.py

Market Analysis & Time Series Analysis for Alpha Discovery

This notebook covers market data analysis, trend detection, volatility analysis,
and technical indicators essential for alpha discovery in trading systems.
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

class MarketAnalysisNotebook:
    """
    Market analysis and time series analysis for alpha discovery.
    """
    
    def __init__(self, market_data: pd.DataFrame):
        """
        Initialize market analysis.
        
        Parameters:
        -----------
        market_data : pd.DataFrame
            OHLCV market data with columns: open, high, low, close, volume
        """
        self.market_data = market_data
        self.indicators = {}
        
    def calculate_returns(self, window: int = 1) -> pd.Series:
        """
        Calculate returns from price series.
        
        Parameters:
        -----------
        window : int
            Returns calculation window in days
            
        Returns:
        --------
        pd.Series
            Returns series
        """
        returns = self.market_data['close'].pct_change(window)
        self.indicators['returns'] = returns
        print(f"Returns calculated (window={window})")
        return returns
    
    def calculate_volatility(self, window: int = 20) -> pd.Series:
        """
        Calculate rolling volatility.
        
        Parameters:
        -----------
        window : int
            Rolling window size
            
        Returns:
        --------
        pd.Series
            Volatility series
        """
        returns = self.calculate_returns()
        volatility = returns.rolling(window).std() * np.sqrt(252)
        self.indicators['volatility'] = volatility
        print(f"Volatility calculated: avg={volatility.mean():.4f}")
        return volatility
    
    def calculate_sma(self, window: int = 50) -> pd.Series:
        """
        Calculate Simple Moving Average.
        """
        sma = self.market_data['close'].rolling(window).mean()
        self.indicators[f'sma_{window}'] = sma
        return sma
    
    def calculate_rsi(self, window: int = 14) -> pd.Series:
        """
        Calculate Relative Strength Index.
        """
        delta = self.market_data['close'].diff()
        gains = (delta.where(delta > 0, 0)).rolling(window).mean()
        losses = (-delta.where(delta < 0, 0)).rolling(window).mean()
        rs = gains / losses
        rsi = 100 - (100 / (1 + rs))
        self.indicators['rsi'] = rsi
        return rsi
    
    def analyze_market_regime(self) -> Dict:
        """
        Analyze current market regime (trend, volatility regime).
        
        Returns:
        --------
        Dict
            Market regime analysis
        """
        sma_50 = self.calculate_sma(50)
        sma_200 = self.calculate_sma(200)
        volatility = self.calculate_volatility()
        
        current_price = self.market_data['close'].iloc[-1]
        in_uptrend = current_price > sma_50.iloc[-1] > sma_200.iloc[-1]
        current_vol = volatility.iloc[-1]
        avg_vol = volatility.mean()
        high_volatility = current_vol > avg_vol * 1.5
        
        regime = {
            'trend': 'uptrend' if in_uptrend else 'downtrend',
            'volatility_regime': 'high' if high_volatility else 'normal',
            'current_volatility': float(current_vol),
            'average_volatility': float(avg_vol),
        }
        return regime
    
    def detect_support_resistance(self, window: int = 50) -> Dict:
        """
        Detect support and resistance levels.
        """
        recent_data = self.market_data['close'].tail(window)
        support = recent_data.min()
        resistance = recent_data.max()
        
        return {
            'support': float(support),
            'resistance': float(resistance),
            'range': float(resistance - support),
        }
    
    def get_market_statistics(self) -> Dict:
        """
        Get comprehensive market statistics.
        """
        returns = self.calculate_returns()
        volatility = self.calculate_volatility()
        
        stats = {
            'daily_return_mean': float(returns.mean()),
            'daily_return_std': float(returns.std()),
            'annual_volatility': float(volatility.iloc[-1]) if not volatility.empty else 0,
            'sharpe_ratio': float((returns.mean() / returns.std()) * np.sqrt(252)) if returns.std() > 0 else 0,
            'max_drawdown': float((self.market_data['close'].cumsum().max() - self.market_data['close'].cumsum()) / self.market_data['close'].cumsum().max()) if self.market_data['close'].cumsum().max() > 0 else 0,
        }
        return stats

def main():
    """
    Example usage of Market Analysis.
    """
    print("="*60)
    print("Market Analysis for Alpha Discovery")
    print("="*60)
    
    # Generate synthetic market data
    np.random.seed(42)
    dates = pd.date_range('2023-01-01', periods=252)
    prices = 100 + np.cumsum(np.random.randn(252) * 2)
    
    market_data = pd.DataFrame({
        'date': dates,
        'open': prices,
        'high': prices + np.abs(np.random.randn(252)),
        'low': prices - np.abs(np.random.randn(252)),
        'close': prices,
        'volume': np.random.randint(1000000, 10000000, 252)
    })
    
    # Initialize analyzer
    analyzer = MarketAnalysisNotebook(market_data)
    
    print("\nMarket Statistics:")
    stats = analyzer.get_market_statistics()
    for key, value in stats.items():
        print(f"  {key}: {value:.6f}")
    
    print("\nMarket Regime:")
    regime = analyzer.analyze_market_regime()
    for key, value in regime.items():
        print(f"  {key}: {value}")
    
    print("\nSupport/Resistance:")
    sr = analyzer.detect_support_resistance()
    for key, value in sr.items():
        print(f"  {key}: {value:.2f}")
    
    print("\nMarket Analysis Complete!")

if __name__ == "__main__":
    from typing import Dict
    main()
