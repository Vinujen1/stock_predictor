from app.services.data_fetcher import DataFetcher


def main():
    fetcher = DataFetcher()

    print("Fetching AAPL...")
    df = fetcher.fetch_and_save_stock("AAPL")

    print(df.head())
    print(df.tail())

    print("\nFetching multiple...")
    fetcher.fetch_multiple_stocks(["MSFT", "TSLA", "NVDA"])

    print("\nSaved datasets:")
    print(fetcher.list_saved_datasets())

    print("\nLatest row:")
    print(fetcher.fetch_latest_stock_row("AAPL"))


if __name__ == "__main__":
    main()