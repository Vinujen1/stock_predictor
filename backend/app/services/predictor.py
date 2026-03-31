import pandas as pd

from app.services.data_fetcher import DataFetcher
from app.services.feature_engineering import FeatureEngineer
from app.ml.scaler_scratch import StandardScalerScratch
from app.ml.linear_regression_scratch import LinearRegressionScratch


class Predictor:
    def __init__(self):
        self.fetcher = DataFetcher()
        self.engineer = FeatureEngineer()
        self.scaler = StandardScalerScratch()
        self.model = LinearRegressionScratch(learning_rate=0.01, n_iterations=2000)

        self.feature_cols = [
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

    def train_model(self, ticker: str):
        df = self.fetcher.load_stock_data(ticker)
        df = self.engineer.prepare_dataset(df)

        df = df.dropna()

        if df.empty:
            raise ValueError("Dataset is empty after preprocessing")

        for col in self.feature_cols:
            if col not in df.columns:
                raise ValueError(f"Missing feature column: {col}")

        X = df[self.feature_cols].values
        y = df["target"].values

        X_scaled = self.scaler.fit_transform(X)
        self.model.fit(X_scaled, y)

    def predict_next(self, ticker: str) -> float:
        ticker = ticker.upper().strip()

        # Train first
        self.train_model(ticker)

        # Reload data
        df = self.fetcher.load_stock_data(ticker)
        df = self.engineer.prepare_dataset(df)

        # Remove NaNs
        df = df.dropna()

        if df.empty:
            raise ValueError("No valid data available for prediction")

        # Take latest row
        latest_row = df.iloc[-1]
        latest_df = pd.DataFrame([latest_row])

        # Ensure features exist
        for col in self.feature_cols:
            if col not in latest_df.columns:
                raise ValueError(f"Missing feature column: {col}")

        X_latest = latest_df[self.feature_cols].values

        # Ensure correct shape
        if X_latest.shape[1] != len(self.feature_cols):
            raise ValueError("Feature shape mismatch during prediction")

        # Scale
        X_latest_scaled = self.scaler.transform(X_latest)

        # Predict
        prediction = self.model.predict(X_latest_scaled)

        return float(prediction[0])