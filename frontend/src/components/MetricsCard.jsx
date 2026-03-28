import Card from "./Card";

export default function MetricsCard({ result }) {
  if (!result) return null;

  return (
    <Card>
      <div className="section-header">
        <h2>Training Results</h2>
        <span className="badge">{result.ticker}</span>
      </div>

      <div className="stats-grid">
        <div className="stat-box">
          <p className="stat-label">MSE</p>
          <p className="stat-value">{result.mse.toFixed(2)}</p>
        </div>

        <div className="stat-box">
          <p className="stat-label">RMSE</p>
          <p className="stat-value">{result.rmse.toFixed(2)}</p>
        </div>

        <div className="stat-box">
          <p className="stat-label">MAE</p>
          <p className="stat-value">{result.mae.toFixed(2)}</p>
        </div>

        <div className="stat-box">
          <p className="stat-label">Train Size</p>
          <p className="stat-value">{result.train_size}</p>
        </div>
      </div>

      <div className="details-grid">
        <div>
          <h3>Prediction Preview</h3>
          <ul className="mini-list">
            {result.predictions_preview.map((value, index) => (
              <li key={index}>{Number(value).toFixed(2)}</li>
            ))}
          </ul>
        </div>

        <div>
          <h3>Actual Preview</h3>
          <ul className="mini-list">
            {result.actual_preview.map((value, index) => (
              <li key={index}>{Number(value).toFixed(2)}</li>
            ))}
          </ul>
        </div>
      </div>
    </Card>
  );
}