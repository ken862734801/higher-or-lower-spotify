import { Button } from "../Button";

export interface StartScreenProps {
  startGame?: () => void;
}

export const StartScreen: React.FC<StartScreenProps> = ({ startGame }) => {
  return (
    <div>
      <div>
        <h1 className="text-citrus">Welcome To</h1>
        <h1 className="text-spearmint">Higher Or Lower</h1>
        <h1 className="text-fuchsia">Spotify Edition</h1>
        <div>
          <h2 className="text-white md:text-xl text-base my-2">
            Can you guess this week&apos;s most played song?
          </h2>
        </div>
      </div>
      <div className="my-4">
        <Button
          className="border border-solid border-white md:text-lg text-base text-white w-44 md:py-2 py-1.5 hover:bg-white hover:text-black transition-colors duration-300 ease-in-out"
          onClick={startGame}
        >
          Play
        </Button>
      </div>
    </div>
  );
};
