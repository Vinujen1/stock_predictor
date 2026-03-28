import numpy as np

from app.services.data_fetcher import DataFetcher
from app.services.feature_engineering import FeatureEngineer
from app.ml.scaler_scratch import StandardScalerScratch
from app.ml.linear_regression_scratch import LinearRegressionScratch


def main():
    fetcher = DataFetcher()
    engineer = FeatureEngineer()
    scaler = StandardScalerScratch()
    model = LinearRegressionScratch(learning_rate=0.01, n_iterations=2000)

    # Load and prepare stock data
    df = fetcher.load_stock_data("AAPL")
    df = engineer.prepare_dataset(df)

    # Feature columns
    feature_cols = [
        "open",
        "high",
        "low",
        "close",
        "volume",
        "return",
        "ma_5",
        "ma_10",
        "volatility_5",
        "momentum",
    ]

    # Build X and y
    X = df[feature_cols].values
    y = df["target"].values

    # Simple train/test split (80/20)
    split_index = int(len(X) * 0.8)

    X_train = X[:split_index]
    X_test = X[split_index:]
    y_train = y[:split_index]
    y_test = y[split_index:]

    # Scale features
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Train model
    model.fit(X_train_scaled, y_train)

    # Predictions
    y_pred = model.predict(X_test_scaled)

    # Evaluate
    mse = model.mse(y_test, y_pred)

    print("First 5 predictions:")
    print(y_pred[:5])

    print("\nFirst 5 actual values:")
    print(y_test[:5])

    print("\nMSE:")
    print(mse)

    print("\nLast training loss:")
    print(model.loss_history[-1])


if __name__ == "__main__":
    main()