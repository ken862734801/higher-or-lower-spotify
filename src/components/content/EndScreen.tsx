// components/EndScreen.tsx
import React, { useEffect, useState } from "react";
import { Button } from "../Button";

export interface EndScreenProps {
  scores?: { score: number };
  restartGame?: () => void;
}

export const EndScreen: React.FC<EndScreenProps> = ({
  scores,
  restartGame,
}) => {
  const [percentile, setPercentile] = useState<number | null>(null);

  useEffect(() => {
    const fetchPercentile = async () => {
      if (scores?.score == null) return;
      try {
        const res = await fetch(
          `/api/score?score=${encodeURIComponent(scores.score)}`, 
          { method: "GET" }
        );
        if (!res.ok) {
          throw new Error(`HTTP ${res.status}`);
        }
        const data: { percentile: number } = await res.json();
        setPercentile(data.percentile);
      } catch (err) {
        console.error("Error fetching percentile:", err);
      }
    };

    fetchPercentile();
  }, [scores?.score]);

  return (
    <div className="text-center">
      <h1 className="text-citrus">Game Over</h1>
      <h2 className="md:text-2xl text-base text-white mt-2">
        Your final score was:
      </h2>
      <h1 className="text-fuchsia">{scores?.score}</h1>

      {percentile !== null && (
        <p className="mt-4 text-white md:text-lg text-base">
          You scored better than{" "}
          <span className="font-bold">{percentile}%</span> of players!
        </p>
      )}

      <div className="my-4">
        <Button
          className="border border-solid border-white md:text-lg text-base text-white w-44 md:py-2 py-1.5 hover:bg-white hover:text-black transition-colors duration-300 ease-in-out"
          onClick={restartGame}
        >
          Play Again
        </Button>
      </div>
    </div>
  );
};
