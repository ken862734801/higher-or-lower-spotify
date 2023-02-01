import logo from './logo.svg';
import './App.css';
import { useEffect, useState } from "react";
import { HashRouter, Route, Routes, Link } from "react-router-dom";
import Home from './components/home';
import Game from './components/game';
import Leaderboard from './components/leaderboard';


function getData(){
  fetch("http://localhost:3000/spotify-global-200")
    .then(response => response.json())
    .then(data => {
      console.log(data)
      console.log(data[getRandomIndex().firstIndex], data[getRandomIndex().secondIndex])
    })
    .catch(err => {
      console.log(err)
    })
};

function getRandomIndex(){
  let firstIndex = Math.floor(Math.random()*(200));
  let secondIndex = Math.floor(Math.random()*(200));
    while (firstIndex === secondIndex){
        secondIndex = Math.floor(Math.random()*(200));
      }
      return {firstIndex, secondIndex}
};

getData()

function App() {

  return (
    <div className="App">
      <HashRouter>
        <Routes>
          <Route path="/" element={<Home/>}></Route>
          <Route path="/game" element={<Game/>}></Route>
          <Route path="/leaderboard" element={<Leaderboard/>}></Route>
        </Routes>
      </HashRouter>
    </div>
  );
}

export default App;
