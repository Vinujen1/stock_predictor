from app.services.data_fetcher import DataFetcher
from app.services.feature_engineering import FeatureEngineer


def main():
    fetcher = DataFetcher()
    engineer = FeatureEngineer()

    df = fetcher.load_stock_data("AAPL")

    print("Before:")
    print(df.head())

    df = engineer.prepare_dataset(df)

    print("\nAfter:")
    print(df.head())

    print("\nColumns:")
    print(df.columns)


if __name__ == "__main__":
    main()