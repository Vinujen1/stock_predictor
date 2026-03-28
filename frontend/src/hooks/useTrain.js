import { useState } from "react";
import API from "../api/client";

export default function useTrain() {
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const train = async (ticker) => {
    try {
      setLoading(true);
      setError("");
      const res = await API.post(`/train/${ticker}`);
      setResult(res.data);
    } catch (err) {
      setError("Training failed. Please try again.");
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return { result, train, loading, error };
}