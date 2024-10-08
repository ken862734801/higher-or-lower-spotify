"use client";
import { v4 as uuidv4 } from "uuid";
import { SiteContainer } from "@/components/SiteContainer";
import { StartScreen, GameScreen, EndScreen } from "@/components/content";
import {
  getFromLocalStorage,
  getRandomIndex,
  saveToLocalStorage,
} from "@/utils";
import { useEffect, useState } from "react";

export interface Data {
  currentRank: number;
  trackName: string;
  name: string;
  displayImageUri: string;
  value: number;
}

export type Choice = "higher" | "lower";
export type Answer = "correct" | "incorrect";

export interface GameState {
  currentSong: Data;
  nextSong: Data;
}

export interface Scores {
  score: number;
  highScore: number;
}

export default function Home() {
  const [userId, setUserId] = useState<string>("");
  const [data, setData] = useState<Data[]>();
  const [showStartScreen, setShowStartScreen] = useState(true);
  const [showCount, setShowCount] = useState<boolean>(false);
  const [gameState, setGameState] = useState<GameState>({
    currentSong: {
      currentRank: 0,
      trackName: "",
      name: "",
      displayImageUri: "",
      value: 0,
    },
    nextSong: {
      currentRank: 0,
      trackName: "",
      name: "",
      displayImageUri: "",
      value: 0,
    },
  });
  const [isCorrect, setIsCorrect] = useState<boolean | null>(null);
  const [gameOver, setGameOver] = useState(false);
  const [scores, setScores] = useState<Scores>({
    score: 0,
    highScore: 0,
  });

  const getData = async () => {
    try {
      const response = await fetch("/api/data");
      if (response.status === 200) {
        const responseJSON = await response.json();
        setData(responseJSON);
      } else {
        console.error("Request failed with status:", response.status);
      }
    } catch (error) {
      console.error("An error occured:", error);
    }
  };

  const addScore = async (userId: string, score: number) => {
    try {
      const response = await fetch("/api/score", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ userId, score }),
      });

      if (!response.ok) {
        throw new Error("Failed to update score.");
      }
      console.log("Success");
    } catch (error) {
      console.error("Error updating score:", error);
    }
  };

  const getSongs = () => {
    if (data) {
      const randomIndex = getRandomIndex(data);
      setGameState({
        currentSong: {
          ...data[randomIndex.firstIndex],
          value: Number(data[randomIndex.firstIndex].value),
        },
        nextSong: {
          ...data[randomIndex.secondIndex],
          value: Number(data[randomIndex.secondIndex].value),
        },
      });
    }
  };

  const getNextSong = () => {
    if (data) {
      const randomIndex = getRandomIndex(data);
      setTimeout(() => {
        window.scrollTo(0, 0);
        setGameState((prev) => ({
          ...prev,
          currentSong: {
            ...prev.nextSong,
            value: Number(prev.nextSong.value),
          },
          nextSong: {
            ...data[randomIndex.firstIndex],
            value: Number(data[randomIndex.firstIndex].value),
          },
        }));
      }, 3000);
    }
  };

  const startGame = () => {
    setShowStartScreen(false);
  };

  const endGame = () => {
    addScore(userId, scores.score);
    setTimeout(() => {
      setGameOver(true);
    }, 3000);
  };

  const restartGame = () => {
    setShowStartScreen(false);
    getSongs();
    resetScore();
    setGameOver(false);
  };

  const incrementScore = () => {
    setTimeout(() => {
      setScores((prev) => ({
        ...prev,
        score: prev.score + 1,
      }));
    }, 3000);
  };

  const resetScore = () => {
    setScores((prev) => ({
      ...prev,
      score: 0,
    }));
  };

  const handleShowCount = () => {
    setShowCount(true);
    setTimeout(() => {
      setShowCount(false);
    }, 3000);
  };

  const handleIsCorrect = (answer: Answer) => {
    if (answer === "correct") {
      setTimeout(() => {
        setIsCorrect(true);

        setTimeout(() => {
          setIsCorrect(null);
        }, 1000);
      }, 2000);
    } else if (answer === "incorrect") {
      setTimeout(() => {
        setIsCorrect(false);

        setTimeout(() => {
          setIsCorrect(null);
        }, 1000);
      }, 2000);
    } else {
      setIsCorrect(null);
    }
  };

  const handleUserChoice = (choice: Choice) => {
    if (
      (choice === "higher" &&
        gameState.nextSong.value >= gameState.currentSong.value) ||
      (choice === "lower" &&
        gameState.nextSong.value <= gameState.currentSong.value)
    ) {
      handleShowCount();
      handleIsCorrect("correct");
      getNextSong();
      incrementScore();
    } else {
      handleShowCount();
      handleIsCorrect("incorrect");
      endGame();
    }
  };

  useEffect(() => {
    getData();
  }, []);

  useEffect(() => {
    getSongs();
  }, [data]);

  useEffect(() => {
    let id = localStorage.getItem("userId");
    if (!id) {
      id = uuidv4();
      localStorage.setItem("userId", id);
    }
    setUserId(id);
  }, []);

  useEffect(() => {
    if (scores.score > scores.highScore) {
      saveToLocalStorage("highScore", scores.score);
      setScores((prev) => ({
        ...prev,
        highScore: prev.score,
      }));
    }
  }, [scores.score]);

  useEffect(() => {
    let localScore = getFromLocalStorage("highScore");
    if (localScore === null) {
      saveToLocalStorage("highScore", 0);
      localScore = 0;
    }
    setScores((prev) => ({
      ...prev,
      highScore: localScore,
    }));
  }, []);

  return (
    <SiteContainer>
      {showStartScreen && <StartScreen startGame={startGame} />}
      {!showStartScreen && !gameOver && (
        <GameScreen
          data={data}
          gameState={gameState}
          isCorrect={isCorrect}
          showCount={showCount}
          scores={scores}
          handleUserChoice={handleUserChoice}
        />
      )}
      {gameOver && <EndScreen scores={scores} restartGame={restartGame} />}
    </SiteContainer>
  );
}
