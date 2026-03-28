import { useState } from "react";
import API from "../api/client";

export default function usePredict() {
  const [prediction, setPrediction] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const predict = async (ticker) => {
    try {
      setLoading(true);
      setError("");
      setPrediction(null);

      const cleanTicker = ticker.trim().replace(".csv", "").toUpperCase();
      console.log("Predicting:", cleanTicker);

      const res = await API.get(`/predict/${cleanTicker}`);
      console.log("Prediction response:", res.data);

      setPrediction(res.data);
    } catch (err) {
      console.error(err);
      setError("Prediction failed. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  return { prediction, predict, loading, error };
}