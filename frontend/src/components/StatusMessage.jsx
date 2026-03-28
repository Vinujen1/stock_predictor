export default function StatusMessage({ text, type = "info" }) {
  if (!text) return null;

  return <div className={`status-message ${type}`}>{text}</div>;
}