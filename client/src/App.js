import logo from './logo.svg';
import './App.css';
import { useEffect, useState } from "react";
import { HashRouter, Route, Routes, Link } from "react-router-dom";
import Game from './components/game';
import Test from './components/game/test';
import Leaderboard from './components/leaderboard';


function App() {

  return (
    <div className="App">
      <HashRouter>
        <Routes>
          <Route path="/" element={<Game/>}></Route>
          <Route path="/leaderboard" element={<Leaderboard/>}></Route>
        </Routes>
      </HashRouter>
    </div>
  );
}

export default App;
