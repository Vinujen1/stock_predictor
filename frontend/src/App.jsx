import { useState } from "react";
import useStocks from "./hooks/useStocks";
import useTrain from "./hooks/useTrain";
import usePredict from "./hooks/usePredict";

import Card from "./components/Card";
import Header from "./components/Header";
import StockSelector from "./components/StockSelector";
import ActionButtons from "./components/ActionButtons";
import MetricsCard from "./components/MetricsCard";
import PredictionCard from "./components/PredictionCard";
import StatusMessage from "./components/StatusMessage";

function App() {
  const [selected, setSelected] = useState("");

  const { stocks, loading: stocksLoading, error: stocksError } = useStocks();
  const {
    result,
    train,
    loading: trainLoading,
    error: trainError,
  } = useTrain();
  const {
    prediction,
    predict,
    loading: predictLoading,
    error: predictError,
  } = usePredict();

  return (
    <div className="app-shell">
      <div className="background-glow background-glow-1" />
      <div className="background-glow background-glow-2" />

      <main className="container">
        <Header />

        <Card>
          <StockSelector
            stocks={stocks}
            selected={selected}
            onChange={setSelected}
            disabled={stocksLoading}
          />

          <ActionButtons
            selected={selected}
            onTrain={train}
            onPredict={predict}
            trainLoading={trainLoading}
            predictLoading={predictLoading}
          />

          {stocksLoading && (
            <StatusMessage text="Loading available stocks..." type="info" />
          )}
          {stocksError && <StatusMessage text={stocksError} type="error" />}
          {trainError && <StatusMessage text={trainError} type="error" />}
          {predictError && <StatusMessage text={predictError} type="error" />}
        </Card>

        <MetricsCard result={result} />
        <PredictionCard prediction={prediction} />
      </main>
    </div>
  );
}

export default App;