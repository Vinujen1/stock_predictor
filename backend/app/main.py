from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.stocks import router as stocks_router
from app.routes.train import router as train_router
from app.routes.predict import router as predict_router

app = FastAPI(title="Stock Predictor API")

# Allow frontend to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(stocks_router, prefix="/stocks", tags=["Stocks"])
app.include_router(train_router, prefix="/train", tags=["Training"])
app.include_router(predict_router, prefix="/predict", tags=["Prediction"])


@app.get("/")
def root():
    return {"message": "Stock Predictor API is running"}