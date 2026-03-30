# Stock Predictor

A full-stack machine learning application that predicts the **next-day stock closing price** using a custom-built regression model implemented **from scratch**.

This project demonstrates an end-to-end ML pipeline including **data collection, feature engineering, model training, evaluation, and deployment via API and frontend UI**.

---

## Features

* **Stock Data Pipeline**

  * Fetches historical stock data using `yfinance`
  * Stores datasets locally for reuse

* **Feature Engineering**

  * Daily returns
  * Moving averages (MA5, MA10)
  * Volatility (rolling std)
  * Momentum indicators

* **Custom Machine Learning Model**

  * Linear Regression implemented **from scratch**
  * Gradient Descent optimization
  * Custom StandardScaler

* **Model Evaluation**

  * Time-based train/test split (80/20)
  * Metrics:

    * Mean Squared Error (MSE)
    * Root Mean Squared Error (RMSE)
    * Mean Absolute Error (MAE)

* **Prediction System**

  * Predicts next-day closing price using latest data
  * Scales and processes inputs consistently

* **Full Stack Application**

  * FastAPI backend
  * React frontend
  * Interactive UI for training and prediction

---

## Architecture

```
Frontend (React)
   ↓
FastAPI Backend
   ↓
ML Pipeline
   ├── DataFetcher
   ├── FeatureEngineer
   ├── StandardScaler (custom)
   ├── LinearRegression (custom)
   └── Trainer / Predictor
```

---

## Machine Learning Pipeline

1. Load stock data
2. Feature engineering
3. Create target (next-day close)
4. Train/Test split (time-based)
5. Scale features
6. Train model (Gradient Descent)
7. Evaluate performance (MSE, RMSE, MAE)
8. Predict next-day price

---

## Example Output

```
Train RMSE: 3.52
Test RMSE: 4.99

Train MAE: 2.81
Test MAE: 4.02
```

Interpretation:

> The model predicts stock prices with an average error of ~$4–5 on unseen data.

---

## Tech Stack

### Backend

* Python
* FastAPI
* NumPy
* Pandas
* yfinance

### Frontend

* React
* Axios

---

## Project Structure

```
stock_predictor/
│
├── app/
│   ├── services/
│   │   ├── data_fetcher.py
│   │   ├── feature_engineering.py
│   │   ├── trainer.py
│   │   └── predictor.py
│   │
│   ├── ml/
│   │   ├── linear_regression_scratch.py
│   │   ├── scaler_scratch.py
│   │   └── metrics.py
│   │
│   ├── routes/
│   │   ├── stocks.py
│   │   ├── train.py
│   │   └── predict.py
│   │
│   └── main.py
│
├── frontend/
│   ├── components/
│   ├── hooks/
│   └── pages/
│
└── README.md
```

---

## ▶How to Run

### 1. Backend

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

API will run at:

```
http://127.0.0.1:8000
```

---

### 2. Frontend

```bash
cd frontend
npm install
npm start
```

---

## API Endpoints

| Endpoint            | Method | Description                    |
| ------------------- | ------ | ------------------------------ |
| `/stocks`           | GET    | List available stocks          |
| `/train/{ticker}`   | POST   | Train model and return metrics |
| `/predict/{ticker}` | GET    | Predict next-day closing price |

---

## Key Highlights

* Built **entire ML model from scratch** (no sklearn regression)
* Correct **time-series train/test split**
* Clean separation of:

  * Data layer
  * ML logic
  * API layer
  * UI layer
* Real-world ML workflow implementation

---

## Future Improvements

* Add more advanced models (Random Forest, XGBoost)
* Add cross-validation
* Visualize predictions vs actual values (charts)
* Deploy to cloud (AWS / Render / Railway)
* Add LSTM / deep learning models

---

## Final Note

This project demonstrates strong understanding of:

* Machine Learning fundamentals
* Model evaluation
* Backend API development
* Frontend integration
* Full-stack system design

---
