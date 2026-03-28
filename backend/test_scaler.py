import numpy as np
from app.services.data_fetcher import DataFetcher
from app.services.feature_engineering import FeatureEngineer
from app.ml.scaler_scratch import StandardScalerScratch


def main():
    fetcher = DataFetcher()
    engineer = FeatureEngineer()
    scaler = StandardScalerScratch()

    df = fetcher.load_stock_data("AAPL")
    df = engineer.prepare_dataset(df)

    # Select features (exclude non-numeric columns)
    feature_cols = [
        "open", "high", "low", "close",
        "volume", "return", "ma_5",
        "ma_10", "volatility_5", "momentum"
    ]

    X = df[feature_cols].values

    print("Before scaling:")
    print(X[:3])

    X_scaled = scaler.fit_transform(X)

    print("\nAfter scaling:")
    print(X_scaled[:3])

    print("\nMeans (should be ~0):")
    print(np.mean(X_scaled, axis=0))

    print("\nStds (should be ~1):")
    print(np.std(X_scaled, axis=0))


if __name__ == "__main__":
    main()