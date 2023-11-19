import './App.css';

import React, { useEffect, useState } from 'react';
import { getRandomSong } from './utils/util';
import Header from './components/header/Header';
import StartScreen from './components/start-screen/StartScreen';
import GameScreen from './components/game-screen/GameScreen';
import EndScreen from './components/end-screen/EndScreen';

function App(){
  const [isLoading, setIsLoading] = useState(false);
  const [chartData, setChartData] = useState([]);
  const [displayOptions, setDisplayOptions] = useState({
    showHeader: false,
    showStartScreen: true,
    showStreamCount: false
  });
  const [gameState, setGameState] = useState({
    currentSong: {},
    nextSong: {},
    isCorrect: null,
    feedbackText: 'vs',
    score: 0,
    highScore: 0,
    isGameOver: false,
  });

  const urlPath = '/api/';
  const headers = {
    'x-api-key': process.env.REACT_APP_API_KEY
  };

  async function fetchData(url){
    setIsLoading(true);
    try {
      const response = await fetch(url, { headers });
      if(response.status === 200){
        const data = await response.json();
        setChartData(data);
      } else {
        console.error('Request failed with status:', response.status);
      }
    } catch (error){
      console.error('An error occured:', error)
    } finally {
      setIsLoading(false);
    }
  };

  function startGame(){
    setDisplayOptions((prev) => ({
      ...prev,
      showHeader: true,
      showStartScreen: false
    }));
  };

  function restartGame(){
    const randomSong = getRandomSong(chartData);
    setDisplayOptions((prev) => ({
      ...prev,
      showHeader: false,
      showStartScreen: true
    }));
    setGameState((prev) => ({
      ...prev,
      currentSong: chartData[randomSong.firstIndex],
      nextSong: chartData[randomSong.secondIndex],
      score: 0,
      isGameOver: false
    }))
  }

  function displayStreamCount(){
    setDisplayOptions((prev) => ({
      ...prev,
      showStreamCount: true
    }));
    setTimeout(() => {
      setDisplayOptions((prev) => ({
        ...prev,
        showStreamCount: false
      }));
    }, 3000);
  };

  function handleAnswerFeedback(answer){
    if(answer === 'correct'){
      setTimeout(() => {
        setGameState((prev) => ({
          ...prev,
          feedbackText: '\u2713',
          isCorrect: true
        }));

        setTimeout(() => {
          setGameState((prev) => ({
            ...prev,
            feedbackText: 'vs',
            isCorrect: null
          }));
        }, 1000);
      }, 2000);

    } else if (answer === 'incorrect'){
      setTimeout(() => {
        setGameState((prev) => ({
          ...prev,
          feedbackText: '✗',
          isCorrect: false
        }));

        setTimeout(() => {
          setGameState((prev) => ({
            ...prev,
            feedbackText: 'vs',
            isCorrect: null
          }));
        }, 1000);
      }, 2000);
    } else {
      setGameState((prev) => ({
        ...prev,
        feedbackText: 'vs'
      }));
    }
  };

  function getNextSong() {
    const randomSong = getRandomSong(chartData);
    setTimeout(() => {
      window.scrollTo(0, 0);
      setGameState((prev) => ({
        ...prev,
        currentSong: prev.nextSong,
        nextSong: chartData[randomSong.firstIndex],
      }));
    }, 3000)
  };

  function incrementScore(){
    setTimeout(() => {
      setGameState((prev) => ({
        ...prev,
        score: prev.score + 1
      }))
    }, 3000)
  };

  function handleGameOver(){
      setTimeout(() => {
        setDisplayOptions((prev) => ({
          ...prev,
          showHeader: false
        }));
        setGameState((prev) => ({
          ...prev,
          isGameOver: true
        }));
      }, 3000);
  };


  function handleUserChoice(choice){
    if((choice === 'Higher' && gameState.nextSong.value >= gameState.currentSong.value) || (choice === 'Lower' && gameState.nextSong.value <= gameState.currentSong.value)){
      displayStreamCount();
      handleAnswerFeedback('correct');
      getNextSong();
      incrementScore();
    } else {
      displayStreamCount();
      handleAnswerFeedback('incorrect');
      handleGameOver();
    }
  };

  useEffect(() => {
    fetchData(urlPath);
  }, [urlPath]);

  useEffect(() => {
    if(chartData.length > 0){
      const randomSong = getRandomSong(chartData);
      setGameState((prev) => ({
        ...prev,
        currentSong: chartData[randomSong.firstIndex],
        nextSong: chartData[randomSong.secondIndex]
      }));
    };
  }, [chartData]);

  useEffect(() => {
    if(gameState.score > gameState.highScore){
      localStorage.setItem('highScore', gameState.score);
      setGameState((prev) => ({
        ...prev,
        highScore: prev.score
      }))
    }
  }, [gameState.score]);

  useEffect(() => {
    let localHighScore = localStorage.getItem('highScore');
    if(!localHighScore){
      localStorage.setItem('highScore', 0);
    };
    setGameState((prev) => ({
      ...prev,
      highScore: localHighScore
    }))
  }, [])

  return (
    <div className='App'>
      {displayOptions.showHeader && (<Header gameState={ gameState }/>) }
      {displayOptions.showStartScreen && (<StartScreen startGame={ startGame }/>)}
      {!displayOptions.showStartScreen && !gameState.isGameOver && (
        <GameScreen displayOptions = {displayOptions} gameState={ gameState } handleUserChoice={ handleUserChoice }/>
      )}
      {gameState.isGameOver && (<EndScreen gameState={ gameState } restartGame= { restartGame }/>)}
    </div>
  )
};

export default App;