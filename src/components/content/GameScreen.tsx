import { Choice, Data } from "@/app/page";
import { Header } from "../Header";
import { Check, X } from "@phosphor-icons/react";
import CountUp from "react-countup";
import { Button } from "../Button";

export interface GameScreenProps {
  data?: Data[];
  gameState?: any;
  showCount?: boolean;
  isCorrect?: boolean | null;
  scores?: any;
  handleUserChoice: (choice: Choice) => void;
}
export const GameScreen: React.FC<GameScreenProps> = ({
  data,
  gameState,
  showCount,
  isCorrect,
  scores,
  handleUserChoice,
}) => {
  return (
    <>
      <Header scores={scores} />
      <div className="flex flex-wrap items-center justify-center mt-5 p-10">
        {data && (
          <>
            <div className="mx-5 w-96">
              <div className="rounded">
                <img
                  className="rounded md:w-72 w-60 mx-auto"
                  src={gameState.currentSong.displayImageUri}
                />
              </div>
              <p
                className="text-white text-lg md:max-w-72 max-w-60 mx-auto truncate mt-2"
                title={gameState.currentSong.trackName}
              >
                {gameState.currentSong.trackName}
              </p>
              <p
                className="text-white text-lg md:max-w-72 max-w-60 mx-auto leading-none truncate"
                title={gameState.currentSong.name}
              >
                {gameState.currentSong.name}
              </p>
              <p className="text-white text-lg">has</p>
              <div className="h-10 my-1">
                <h3 className="md:text-6xl text-4xl font-bold text-citrus">
                  {gameState.currentSong.value.toLocaleString()}
                </h3>
              </div>
            </div>
            <div className="md:mx-5 my-2">
              <div
                className={`md:w-10 w-8 md:h-10 h-8 flex items-center justify-center rounded-full ${
                  isCorrect === true
                    ? "bg-citrus"
                    : isCorrect === false
                    ? "bg-fuchsia text-white"
                    : "text-citrus"
                }`}
              >
                {isCorrect === true ? (
                  <Check size={24} weight="bold"></Check>
                ) : isCorrect === false ? (
                  <X size={24} weight="bold"></X>
                ) : (
                  <span className="md:text-xl text-lg">VS</span>
                )}
              </div>
            </div>
            <div className="mx-5 w-96">
              <div className="rounded">
                <img
                  className="rounded md:w-72 w-60 mx-auto"
                  src={gameState.nextSong.displayImageUri}
                />
              </div>
              <p
                className="text-white text-lg md:max-w-72 max-w-60 mx-auto truncate mt-2"
                title={gameState.nextSong.trackName}
              >
                {gameState.nextSong.trackName}
              </p>
              <p
                className="text-white text-lg md:max-w-72 max-w-60 mx-auto leading-none truncate"
                title={gameState.nextSong.name}
              >
                {gameState.nextSong.name}
              </p>
              <p className="text-white text-lg">has</p>
              <div className="h-10 my-2">
                {showCount ? (
                  <CountUp
                    start={gameState.nextSong.value * 0.95}
                    end={gameState.nextSong.value}
                    duration={2}
                    separator=","
                    delay={0}
                  >
                    {({ countUpRef }) => (
                      <span
                        className="md:text-6xl text-4xl font-bold text-citrus"
                        ref={countUpRef}
                      />
                    )}
                  </CountUp>
                ) : (
                  <div className="flex flex-col items-center gap-2">
                    <Button
                      className="text-citrus border border-solid border-citrus rounded-full hover:bg-white hover:border-white hover:text-black transition-colors duration-300 ease-in-out md:p-1 p-0.5 mx-1.5 w-36"
                      onClick={() => handleUserChoice("higher")}
                    >
                      Higher
                    </Button>
                    <Button
                      className="text-citrus border border-solid border-citrus rounded-full hover:bg-white hover:border-white hover:text-black transition-colors duration-300 ease-in-out md:p-1 p-0.5 mx-1.5 w-36"
                      onClick={() => handleUserChoice("lower")}
                    >
                      Lower
                    </Button>
                  </div>
                )}
              </div>
            </div>
          </>
        )}
      </div>
    </>
  );
};
