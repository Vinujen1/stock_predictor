from fastapi import APIRouter
from app.services.data_fetcher import DataFetcher

router = APIRouter()

fetcher = DataFetcher()


@router.get("/")
def get_available_stocks():
    return {
        "available_stocks": fetcher.list_saved_datasets()
    }