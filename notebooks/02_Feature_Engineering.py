"""02_Feature_Engineering.py - Feature Engineering for Alpha Signals"""
import pandas as pd
import numpy as np
from typing import Dict, List

class FeatureEngineeringNotebook:
    def __init__(self, market_data: pd.DataFrame):
        self.market_data = market_data
        self.features = {}
    
    def create_momentum_features(self) -> pd.DataFrame:
        """Create momentum-based features."""
        closes = self.market_data['close']
        self.features['momentum_5'] = (closes - closes.shift(5)) / closes.shift(5)
        self.features['momentum_10'] = (closes - closes.shift(10)) / closes.shift(10)
        self.features['roc'] = closes.pct_change(12)
        return pd.DataFrame(self.features)
    
    def create_volatility_features(self) -> pd.DataFrame:
        """Create volatility features."""
        returns = self.market_data['close'].pct_change()
        self.features['volatility_20'] = returns.rolling(20).std()
        self.features['volatility_ratio'] = returns.rolling(20).std() / returns.rolling(60).std()
        return pd.DataFrame(self.features)
    
    def create_mean_reversion_features(self) -> pd.DataFrame:
        """Create mean reversion features."""
        closes = self.market_data['close']
        sma_20 = closes.rolling(20).mean()
        self.features['distance_to_sma'] = (closes - sma_20) / sma_20
        self.features['z_score'] = (closes - sma_20) / closes.rolling(20).std()
        return pd.DataFrame(self.features)
    
    def create_volume_features(self) -> pd.DataFrame:
        """Create volume-based features."""
        self.features['volume_sma_ratio'] = self.market_data['volume'] / self.market_data['volume'].rolling(20).mean()
        self.features['on_balance_volume'] = (np.sign(self.market_data['close'].diff()) * self.market_data['volume']).cumsum()
        return pd.DataFrame(self.features)
    
    def create_all_features(self) -> pd.DataFrame:
        """Create all engineered features."""
        self.create_momentum_features()
        self.create_volatility_features()
        self.create_mean_reversion_features()
        self.create_volume_features()
        print(f"Created {len(self.features)} features")
        return pd.DataFrame(self.features)

def main():
    print("Feature Engineering for Alpha Signals")
    np.random.seed(42)
    data = pd.DataFrame({'close': 100 + np.cumsum(np.random.randn(252) * 2), 'volume': np.random.randint(1000000, 10000000, 252)})
    eng = FeatureEngineeringNotebook(data)
    features = eng.create_all_features()
    print(f"Features shape: {features.shape}")

if __name__ == "__main__":
    main()
