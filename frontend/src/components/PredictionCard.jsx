import Card from "./Card";

export default function PredictionCard({ prediction }) {
  if (!prediction) return null;

  return (
    <Card>
      <div className="section-header">
        <h2>Next-Day Prediction</h2>
        <span className="badge">{prediction.ticker}</span>
      </div>

      <div className="prediction-box">
        <p className="prediction-label">Predicted Next Close</p>
        <p className="prediction-value">
          ${Number(prediction.predicted_next_close).toFixed(2)}
        </p>
      </div>
    </Card>
  );
}