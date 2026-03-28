import { useEffect, useState } from "react";
import API from "../api/client";

export default function useStocks() {
  const [stocks, setStocks] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    const fetchStocks = async () => {
      try {
        setLoading(true);
        setError("");

        const res = await API.get("/stocks");
        setStocks(res.data.available_stocks || []);
      } catch (err) {
        setError("Failed to load available stocks.");
        console.error(err);
      } finally {
        setLoading(false);
      }
    };

    fetchStocks();
  }, []);

  return { stocks, loading, error };
}