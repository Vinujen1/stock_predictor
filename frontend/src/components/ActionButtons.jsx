export default function ActionButtons({
  selected,
  onTrain,
  onPredict,
  trainLoading,
  predictLoading,
}) {
  return (
    <div className="button-row">
      <button
        className="btn btn-primary"
        onClick={() => {
          console.log("Train clicked:", selected);
          onTrain(selected);
        }}
        disabled={!selected || trainLoading}
      >
        {trainLoading ? "Training..." : "Train Model"}
      </button>

      <button
        className="btn btn-secondary"
        onClick={() => {
          console.log("Predict clicked:", selected);
          onPredict(selected);
        }}
        disabled={!selected || predictLoading}
      >
        {predictLoading ? "Predicting..." : "Predict"}
      </button>
    </div>
  );
}