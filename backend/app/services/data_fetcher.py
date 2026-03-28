from pathlib import Path
from typing import List, Dict

import pandas as pd
import yfinance as yf


BASE_DIR = Path(__file__).resolve().parent.parent
DATASET_DIR = BASE_DIR / "storage" / "datasets"
DATASET_DIR.mkdir(parents=True, exist_ok=True)


class DataFetcher:
    def __init__(self, dataset_dir: Path = DATASET_DIR):
        self.dataset_dir = dataset_dir
        self.dataset_dir.mkdir(parents=True, exist_ok=True)

    def fetch_stock_history(
        self,
        ticker: str,
        period: str = "5y",
        interval: str = "1d"
    ) -> pd.DataFrame:
        ticker = ticker.upper().strip()

        df = yf.download(
            tickers=ticker,
            period=period,
            interval=interval,
            auto_adjust=False,
            progress=False
        )

        if df.empty:
            raise ValueError(f"No data for {ticker}")

        df = df.reset_index()

        # Flatten multi-index columns if needed
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = [
                "_".join([str(part) for part in col if part]).strip("_")
                for col in df.columns
            ]

        # Normalize all column names
        df.columns = [str(col).strip().lower().replace(" ", "_") for col in df.columns]

        # Find the date column safely
        date_col = None
        for col in df.columns:
            if "date" in col or "datetime" in col:
                date_col = col
                break

        if date_col is None:
            raise ValueError(f"Could not find a date column for {ticker}. Columns: {list(df.columns)}")

        df = df.rename(columns={date_col: "date"})

        # Standardize OHLCV columns
        rename_map = {}
        for col in df.columns:
            if col.startswith("open"):
                rename_map[col] = "open"
            elif col.startswith("high"):
                rename_map[col] = "high"
            elif col.startswith("low"):
                rename_map[col] = "low"
            elif col.startswith("close"):
                rename_map[col] = "close"
            elif "adj_close" in col or "adjclose" in col:
                rename_map[col] = "adj_close"
            elif col.startswith("volume"):
                rename_map[col] = "volume"

        df = df.rename(columns=rename_map)

        required_cols = ["date", "open", "high", "low", "close", "volume"]
        missing_cols = [col for col in required_cols if col not in df.columns]
        if missing_cols:
            raise ValueError(
                f"Missing required columns for {ticker}: {missing_cols}. Found columns: {list(df.columns)}"
            )

        keep_cols = ["date", "open", "high", "low", "close", "adj_close", "volume"]
        existing_cols = [col for col in keep_cols if col in df.columns]
        df = df[existing_cols].copy()

        df["ticker"] = ticker
        df["date"] = pd.to_datetime(df["date"])
        df = df.sort_values("date").reset_index(drop=True)

        return df

    def save_stock_data(self, df: pd.DataFrame, ticker: str):
        ticker = ticker.upper().strip()
        file_path = self.dataset_dir / f"{ticker}.csv"
        df.to_csv(file_path, index=False)

    def load_stock_data(self, ticker: str) -> pd.DataFrame:
        ticker = ticker.upper().strip()
        file_path = self.dataset_dir / f"{ticker}.csv"

        if not file_path.exists():
            raise FileNotFoundError(f"{ticker} not found")

        df = pd.read_csv(file_path)
        df["date"] = pd.to_datetime(df["date"])
        return df

    def fetch_and_save_stock(self, ticker: str):
        df = self.fetch_stock_history(ticker)
        self.save_stock_data(df, ticker)
        return df

    def fetch_multiple_stocks(self, tickers: List[str]) -> Dict[str, pd.DataFrame]:
        results = {}

        for ticker in tickers:
            try:
                df = self.fetch_stock_history(ticker)
                self.save_stock_data(df, ticker)
                results[ticker.upper()] = df
            except Exception as e:
                print(f"Error fetching {ticker}: {e}")

        return results

    def fetch_latest_stock_row(self, ticker: str):
        df = self.fetch_stock_history(ticker, period="1mo")
        return df.iloc[-1]

    def list_saved_datasets(self):
        return sorted([file.stem.upper() for file in self.dataset_dir.glob("*.csv")])