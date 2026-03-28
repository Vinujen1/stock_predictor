from fastapi import APIRouter
from app.services.trainer import Trainer

router = APIRouter()

trainer = Trainer()


@router.post("/{ticker}")
def train_model(ticker: str):
    results = trainer.train_for_ticker(ticker)
    return results