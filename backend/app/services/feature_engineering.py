import pandas as pd


class FeatureEngineer:
    """
    Creates ML features from stock data.
    """

    def add_features(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df.copy()

        # --- Returns ---
        df["return"] = df["close"].pct_change()

        # --- Moving Averages ---
        df["ma_5"] = df["close"].rolling(window=5).mean()
        df["ma_10"] = df["close"].rolling(window=10).mean()

        # --- Volatility ---
        df["volatility_5"] = df["close"].rolling(window=5).std()

        # --- Momentum ---
        df["momentum"] = df["close"] - df["close"].shift(5)

        return df

    def add_target(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df.copy()

        # Predict next day close
        df["target"] = df["close"].shift(-1)

        return df

    def clean_data(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df.copy()

        # Remove NaNs caused by rolling + shift
        df = df.dropna().reset_index(drop=True)

        return df

    def prepare_dataset(self, df: pd.DataFrame) -> pd.DataFrame:
        df = self.add_features(df)
        df = self.add_target(df)
        df = self.clean_data(df)

        return df