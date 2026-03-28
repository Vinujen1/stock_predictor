from app.services.data_fetcher import DataFetcher
from app.services.feature_engineering import FeatureEngineer
from app.ml.scaler_scratch import StandardScalerScratch
from app.ml.linear_regression_scratch import LinearRegressionScratch
from app.ml.metrics import (
    mean_squared_error,
    root_mean_squared_error,
    mean_absolute_error,
)


class Trainer:
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

    def train_for_ticker(self, ticker: str) -> dict:
        df = self.fetcher.load_stock_data(ticker)
        df = self.engineer.prepare_dataset(df)

        X = df[self.feature_cols].values
        y = df["target"].values

        split_index = int(len(X) * 0.8)

        X_train = X[:split_index]
        X_test = X[split_index:]
        y_train = y[:split_index]
        y_test = y[split_index:]

        X_train_scaled = self.scaler.fit_transform(X_train)
        X_test_scaled = self.scaler.transform(X_test)

        self.model.fit(X_train_scaled, y_train)

        y_pred = self.model.predict(X_test_scaled)

        mse = mean_squared_error(y_test, y_pred)
        rmse = root_mean_squared_error(y_test, y_pred)
        mae = mean_absolute_error(y_test, y_pred)

        return {
            "ticker": ticker.upper(),
            "train_size": len(X_train),
            "test_size": len(X_test),
            "mse": float(mse),
            "rmse": float(rmse),
            "mae": float(mae),
            "predictions_preview": y_pred[:5].tolist(),
            "actual_preview": y_test[:5].tolist(),
            "last_training_loss": float(self.model.loss_history[-1]),
        }