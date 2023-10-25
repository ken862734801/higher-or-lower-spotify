import './App.css';

import React, { useEffect, useState } from "react";
import Header from './components/header/Header';
import StartScreen from './components/start-screen/StartScreen';
import GameScreen from './components/game-screen/GameScreen';
import EndScreen from './components/end-screen/EndScreen';

async function getData (url) {
  try {
    const headers = {
      "X-API-Key": process.env.REACT_APP_API_KEY,
    }
    const response = await fetch(url, {headers});
    const data = await response.json();
    return data
  } catch (err){
    console.error(err);
  }
};

function getRandomSong (data) {
  let firstIndex = Math.floor(Math.random() * data.length);
  let secondIndex = Math.floor(Math.random() * data.length);

  while (secondIndex === firstIndex){
    secondIndex = Math.floor(Math.random() * data.length)
  }
    return { firstIndex, secondIndex }
};

function App() {
  const [data, setData] = useState([]);
  const [showHeader, setShowHeader] = useState(false);
  const [showStartScreen, setShowStartScreen] = useState(true);
  const [gameOver, setGameOver] = useState(false);
  const [text, setText] = useState("VS");
  const [currentSong, setCurrentSong] = useState({});
  const [nextSong, setNextSong] = useState({});
  const [isCorrect, setIsCorrect] = useState(false);
  const [isWrong, setIsWrong] = useState(false);
  const [displayNextSong, setDisplayNextSong] = useState(false);
  const [score, setScore] = useState(0);
  const [highScore, setHighScore] = useState(0);

  const apiUrl = "/api/";
  const containerClassName = `circle ${isCorrect ? "green" : isWrong ? "red" : ""}`;

  function handleGameStart(){
    setShowStartScreen(false);
    setShowHeader(true);
  };

  function handleGameReset(){
    const index = getRandomSong(data);
    setCurrentSong(data[index.firstIndex]);
    setNextSong(data[index.secondIndex]);
    setShowStartScreen(true);
    setGameOver(false);
    setScore(0);
  };

  function displaySongValue (){
    setDisplayNextSong(true);
    setTimeout(() => {
      setDisplayNextSong(false)
    }, 3000);
  };

  const handleChangeColor = (answer) => {
    setIsCorrect(false);
    setIsWrong(false);
    if ((answer === "Higher" && nextSong.value > currentSong.value) || (answer === "Lower" && nextSong.value < currentSong.value)) {
        setIsCorrect(true);
            setText("\u2713");
        setTimeout(() => {
            setIsCorrect(false);
        }, 1000);
        setTimeout(() => {
            setText("VS");
        }, 1000);
    } else {
        setIsWrong(true);
            setText("✗");
        setTimeout(() => {
            setIsWrong(false);
        }, 2000);
        setTimeout(() => {
            setText("VS");
        }, 2000);
    }
};

  const handleSelectHigher = () => {
    if(nextSong.value > currentSong.value){
        displaySongValue();
        setTimeout(() => {
        handleChangeColor("Higher");
        }, 2000);
        setTimeout(() => {
            window.scrollTo(0,0);
            setCurrentSong(nextSong);
            const index = getRandomSong(data);
            setNextSong(data[index.secondIndex]);
            setScore(score + 1);
            }, 3000);
    } else if(nextSong.value === currentSong.value){
        displaySongValue();
        setTimeout(() => {
        handleChangeColor("Higher");
        }, 2000);
        setTimeout(() => {
            window.scrollTo(0,0);
            setCurrentSong(nextSong);
            const index = getRandomSong(data);
            setNextSong(data[index.secondIndex]);
            setScore(score + 1);
            }, 3000);
    }else {
        displaySongValue();
        setTimeout(() => {
            handleChangeColor("Higher");
        }, 2000);
        setTimeout(() => {
            setGameOver(true);
            setShowHeader(false);
        }, 2750);
    }
};

  function handleSelectLower(){
    if(nextSong.value < currentSong.value){
      displaySongValue();
      setTimeout(() => {
          handleChangeColor("Lower");
          }, 2000);
      setTimeout(() => {
          window.scrollTo(0,0);
          setCurrentSong(nextSong);
          const index = getRandomSong(data);
          setNextSong(data[index.secondIndex]);
          setScore(score + 1);
          }, 3000);
    } else if(nextSong.value === currentSong.value){
        displaySongValue();
        setTimeout(() => {
            handleChangeColor("Lower");
            }, 2000);
        setTimeout(() => {
            window.scrollTo(0,0);
            setCurrentSong(nextSong);
            const index = getRandomSong(data);
            setNextSong(data[index.secondIndex]);
            setScore(score + 1);
            }, 3000);
    }else {
        displaySongValue();
        setTimeout(() => {
            handleChangeColor("Lower");
            }, 2000);
        setTimeout(() => {
            setGameOver(true);
            setShowHeader(false);
        }, 2750);
    }
  };

  useEffect(() => {
    const handleDataFetch = async() => {
      const chartData = await getData(apiUrl);
        setData(chartData);
    };
    handleDataFetch();
  }, [apiUrl]);

  useEffect(() => {
    if(data.length > 0){
      const index = getRandomSong(data);
      setCurrentSong(data[index.firstIndex]);
      setNextSong(data[index.secondIndex])
    };
  }, [data]);

  useEffect(() => {
    if (score > highScore){
        localStorage.setItem("highScore", score);
        setHighScore(score);
    }
  }, [score]);

  useEffect(()=> {
    let highScore = localStorage.getItem("highScore");
    if(!highScore){
        localStorage.setItem("highScore", 0);
        highScore = 0;
    };
    setHighScore(highScore);
    }, []);



  return (
    <div className="App">
      {showHeader && (<Header score={score} highScore={highScore}/>)}
      {showStartScreen && <StartScreen handleGameStart={handleGameStart}/>}
      {!showStartScreen && !gameOver && (
        <GameScreen handleSelectHigher={handleSelectHigher}
                    handleSelectLower={handleSelectLower} 
                    currentSong={currentSong} 
                    nextSong={nextSong} 
                    containerClassName={containerClassName} 
                    displayNextSong={displayNextSong} 
                    currentSongImage={currentSong.displayImageUri}
                    nextSongImage={nextSong.displayImageUri}
                    text={text}/>
      )}
      {!showStartScreen && gameOver && (
        <EndScreen score={score} handleGameReset={handleGameReset}/>
      )}
    </div>
  );
}

export default App;
