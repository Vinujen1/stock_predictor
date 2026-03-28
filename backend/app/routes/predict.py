from fastapi import APIRouter
from app.services.predictor import Predictor

router = APIRouter()

predictor = Predictor()


@router.get("/{ticker}")
def predict(ticker: str):
    prediction = predictor.predict_next(ticker)

    return {
        "ticker": ticker.upper(),
        "predicted_next_close": prediction
    }