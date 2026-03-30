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
          <p className="stat-label">Train MSE</p>
          <p className="stat-value">
            {result.train_mse != null ? Number(result.train_mse).toFixed(2) : "—"}
          </p>
        </div>

        <div className="stat-box">
          <p className="stat-label">Train RMSE</p>
          <p className="stat-value">
            {result.train_rmse != null ? Number(result.train_rmse).toFixed(2) : "—"}
          </p>
        </div>

        <div className="stat-box">
          <p className="stat-label">Train MAE</p>
          <p className="stat-value">
            {result.train_mae != null ? Number(result.train_mae).toFixed(2) : "—"}
          </p>
        </div>

        <div className="stat-box">
          <p className="stat-label">Test MSE</p>
          <p className="stat-value">
            {result.test_mse != null ? Number(result.test_mse).toFixed(2) : "—"}
          </p>
        </div>

        <div className="stat-box">
          <p className="stat-label">Test RMSE</p>
          <p className="stat-value">
            {result.test_rmse != null ? Number(result.test_rmse).toFixed(2) : "—"}
          </p>
        </div>

        <div className="stat-box">
          <p className="stat-label">Test MAE</p>
          <p className="stat-value">
            {result.test_mae != null ? Number(result.test_mae).toFixed(2) : "—"}
          </p>
        </div>

        <div className="stat-box">
          <p className="stat-label">Train Size</p>
          <p className="stat-value">{result.train_size ?? "—"}</p>
        </div>

        <div className="stat-box">
          <p className="stat-label">Test Size</p>
          <p className="stat-value">{result.test_size ?? "—"}</p>
        </div>
      </div>

      <div className="details-grid">
        <div>
          <h3>Prediction Preview</h3>
          <ul className="mini-list">
            {result.predictions_preview?.map((value, index) => (
              <li key={index}>{Number(value).toFixed(2)}</li>
            ))}
          </ul>
        </div>

        <div>
          <h3>Actual Preview</h3>
          <ul className="mini-list">
            {result.actual_preview?.map((value, index) => (
              <li key={index}>{Number(value).toFixed(2)}</li>
            ))}
          </ul>
        </div>
      </div>
    </Card>
  );
}