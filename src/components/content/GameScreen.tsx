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
      <div className="flex flex-wrap items-center justify-center">
        {data && (
          <>
            <div>
              <div className="rounded">
                <img
                  className="rounded"
                  src={gameState.currentSong.displayImageUri}
                />
              </div>
              <p className="text-white">{gameState.currentSong.trackName}</p>
              <p className="text-white">{gameState.currentSong.name}</p>
              <div>
                <h3 className="text-5xl text-citrus">
                  {gameState.currentSong.value.toLocaleString()}
                </h3>
              </div>
            </div>
            <div className="mx-5">
              <div
                className={`w-10 h-10 flex items-center justify-center rounded-full ${
                  isCorrect === true
                    ? "bg-citrus"
                    : isCorrect === false
                    ? "bg-fuchsia"
                    : ""
                }`}
              >
                {isCorrect === true ? (
                  <Check size={20}></Check>
                ) : isCorrect === false ? (
                  <X size={20}></X>
                ) : (
                  <span>VS</span>
                )}
              </div>
            </div>
            <div>
              <div className="rounded">
                <img
                  className="rounded"
                  src={gameState.nextSong.displayImageUri}
                />
              </div>
              <p className="text-white">{gameState.nextSong.trackName}</p>
              <p className="text-white">{gameState.nextSong.name}</p>
              {/* <h3 className="text-5xl text-citrus">{gameState.nextSong.value}</h3> */}
              <div>
                {showCount ? (
                  <CountUp
                    start={gameState.nextSong.value * 0.95}
                    end={gameState.nextSong.value}
                    duration={2}
                    separator=","
                    delay={0}
                  >
                    {({countUpRef}) => <span className="text-5xl text-citrus" ref={countUpRef}/>}
                  </CountUp>
                ) : (
                  <>
                    <Button
                      className="text-white"
                      onClick={() => handleUserChoice("higher")}
                    >
                      Higher
                    </Button>
                    <Button
                      className="text-white"
                      onClick={() => handleUserChoice("lower")}
                    >
                      Lower
                    </Button>
                  </>
                )}
              </div>
            </div>
          </>
        )}
      </div>
    </>
  );
};
