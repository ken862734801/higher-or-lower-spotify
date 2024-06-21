import { Button } from "../Button";

export interface EndScreenProps {
  scores?: any;
  restartGame?: () => void;
}
export const EndScreen: React.FC<EndScreenProps> = ({
  scores,
  restartGame,
}) => {
  return (
    <div>
      <h1 className="text-citrus">Game Over</h1>
      <h2 className="text-white">Your final score was:</h2>
      <h1 className="text-fuchsia">{scores.score}</h1>
      <div className="my-4">
        <Button
          className="border border-solid border-white text-lg text-white w-44 py-2 hover:bg-white hover:text-black transition-colors duration-300 ease-in-out"
          onClick={restartGame}
        >
          Play Again
        </Button>
      </div>
    </div>
  );
};
