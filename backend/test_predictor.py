from app.services.predictor import Predictor


def main():
    predictor = Predictor()

    prediction = predictor.predict_next("AAPL")

    print("Predicted next-day close for AAPL:")
    print(prediction)


if __name__ == "__main__":
    main()  