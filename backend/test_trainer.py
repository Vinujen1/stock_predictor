from app.services.trainer import Trainer


def main():
    trainer = Trainer()
    results = trainer.train_for_ticker("AAPL")

    print("Training Results:")
    for key, value in results.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()