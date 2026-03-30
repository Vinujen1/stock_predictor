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

        if df.empty:
            raise ValueError("Dataset is empty after preprocessing")

        for col in self.feature_cols + ["target"]:
            if col not in df.columns:
                raise ValueError(f"Missing required column: {col}")

        X = df[self.feature_cols].values
        y = df["target"].values

        split_index = int(len(X) * 0.8)

        if split_index == 0 or split_index == len(X):
            raise ValueError("Not enough data to split into train and test sets")

        X_train = X[:split_index]
        X_test = X[split_index:]
        y_train = y[:split_index]
        y_test = y[split_index:]

        X_train_scaled = self.scaler.fit_transform(X_train)
        X_test_scaled = self.scaler.transform(X_test)

        self.model.fit(X_train_scaled, y_train)

        y_train_pred = self.model.predict(X_train_scaled)
        y_test_pred = self.model.predict(X_test_scaled)

        train_mse = mean_squared_error(y_train, y_train_pred)
        train_rmse = root_mean_squared_error(y_train, y_train_pred)
        train_mae = mean_absolute_error(y_train, y_train_pred)

        test_mse = mean_squared_error(y_test, y_test_pred)
        test_rmse = root_mean_squared_error(y_test, y_test_pred)
        test_mae = mean_absolute_error(y_test, y_test_pred)

        return {
            "ticker": ticker.upper(),
            "train_size": len(X_train),
            "test_size": len(X_test),
            "train_mse": float(train_mse),
            "train_rmse": float(train_rmse),
            "train_mae": float(train_mae),
            "test_mse": float(test_mse),
            "test_rmse": float(test_rmse),
            "test_mae": float(test_mae),
            "predictions_preview": y_test_pred[:5].tolist(),
            "actual_preview": y_test[:5].tolist(),
            "last_training_loss": float(self.model.loss_history[-1]),
        }