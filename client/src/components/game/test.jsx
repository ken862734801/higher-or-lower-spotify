import React, {useState, useEffect } from "react";

const getData = async (apiUrl) => {
  const response = await fetch(apiUrl);
  const data = await response.json();
  return data;
};

const getRandomIndex = (data) => {
  const firstIndex = Math.floor(Math.random() * data.length);
  let secondIndex = Math.floor(Math.random() * data.length);

  while (secondIndex === firstIndex) {
    secondIndex = Math.floor(Math.random() * data.length);
  }

  return { firstIndex, secondIndex };
};

const Test = () => {
const apiUrl = "http://localhost:3000/spotify-global-200";
  const [data, setData] = useState([]);
  const [currentSong, setCurrentSong] = useState({});
  const [nextSong, setNextSong] = useState({});
  const [gameOver, setGameOver] = useState(false);

  useEffect(() => {
    const fetchData = async () => {
      const songs = await getData(apiUrl);
      setData(songs);
    };

    fetchData();
  }, [apiUrl]);

  useEffect(() => {
    if (data.length > 0) {
      const index = getRandomIndex(data);
      setCurrentSong(data[index.firstIndex]);
      setNextSong(data[index.secondIndex]);
    }
  }, [data]);

  const handleHigher = () => {
    if (nextSong.value > currentSong.value) {
      setCurrentSong(nextSong);
      const index = getRandomIndex(data);
      setNextSong(data[index.secondIndex]);
    } else {
      setGameOver(true);
    }
  };

  const handleLower = () => {
    if (nextSong.value < currentSong.value) {
      setCurrentSong(nextSong);
      const index = getRandomIndex(data);
      setNextSong(data[index.secondIndex]);
    } else {
      setGameOver(true);
    }
  };

  return (
    <div>
      {gameOver ? (
        <p>Game Over</p>
      ) : (
        <>
          <img src={currentSong.displayImageUri} alt="cover art" />
          <p>
            Song: {currentSong.trackName}
            <br />
            Artist: {currentSong.name}
            <br />
            value: {currentSong.value}
          </p>
          <img src={nextSong.displayImageUri} alt="cover art" />
          <p>
            Song: {nextSong.trackName}
            <br />
            Artist: {nextSong.name}
            <br />
            value: {nextSong.value}
          </p>
          <button onClick={handleHigher}>Higher</button>
          <button onClick={handleLower}>Lower</button>
        </>
      )}
    </div>
  );
};

export default Test;
