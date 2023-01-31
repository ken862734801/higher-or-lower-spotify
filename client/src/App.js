import logo from './logo.svg';
import './App.css';
import React, { useEffect, useState } from "react";

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
    <div className="App"></div>
  );
}

export default App;
