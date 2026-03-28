export default function StockSelector({
  stocks,
  selected,
  onChange,
  disabled = false,
}) {
  return (
    <div className="selector-group">
      <label className="label">Select Stock</label>
      <select
        className="select"
        value={selected}
        onChange={(e) => onChange(e.target.value)}
        disabled={disabled}
      >
        <option value="">Choose a stock</option>
        {stocks.map((stock) => (
          <option key={stock} value={stock}>
            {stock}
          </option>
        ))}
      </select>
    </div>
  );
}