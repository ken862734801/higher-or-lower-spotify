import "./game.css";
import React, { useEffect, useState} from 'react';

const getData = async (api) =>{
    const response = await fetch(api);
    const data = await response.json();
    return data
};

const getRandomIndex = (data) =>{
    const firstIndex = Math.floor(Math.random() * data.length);
    let secondIndex = Math.floor(Math.random() * data.length);

    while (secondIndex === firstIndex){
        secondIndex = Math.floor(Math.random() * data.length)
    }
    return {firstIndex, secondIndex}
}

function Game (){
    const apiUrl = "http://localhost:3000/spotify-global-200";
    const [showStartScreen, setShowStartScreen] = useState(true);
    const [data, setData] = useState([]);
    const [currentSong, setCurrentSong] = useState({});
    const [nextSong, setNextSong] = useState({});
    const [gameOver, setGameOver] = useState(false);
    const [score, setScore] = useState(0)

    useEffect(() => {
        const fetchData = async() => {
            const chartData = await getData(apiUrl);
            setData(chartData)
        };
        fetchData();
    }, [apiUrl]);

    useEffect(() => {
        if(data.length > 0){
            const index = getRandomIndex(data);
            setCurrentSong(data[index.firstIndex]);
            setNextSong(data[index.secondIndex]);
        }
    },
    [data])

    const startGame = () => {
        setShowStartScreen(false)
    };

    const resetGame = () => {
        setShowStartScreen(true);
        setGameOver(false);
        setScore(0);
      };

    const handleHigher = () => {
        if(nextSong.value > currentSong.value){
            setCurrentSong(nextSong);
            const index = getRandomIndex(data);
            setNextSong(data[index.secondIndex]);
            setScore(score + 1)
        }else{
            setGameOver(true)
        }
    };

    const handleLower = () => {
        if(nextSong.value < currentSong.value){
            setCurrentSong(nextSong);
            const index = getRandomIndex(data);
            setNextSong(data[index.secondIndex]);
            setScore(score + 1)
        } else {
            setGameOver(true)
        }
    }

    return (
        <main>
            {showStartScreen && ! gameOver && (
            <section className="start-container" id="start-container">
                <div className="title-container">
                    <h1 className="citric">Welcome to</h1>
                    <h1 className="spearmint">Higher or Lower</h1>
                    <h1 className="fuschia">Music Edition</h1>
                    <div className="subtitle-container">
                        <h2>Can you guess the more popular song?</h2>
                        <p>A frustratingly addictive game of higher or lower using the top 200 songs from Spotify's global chart.</p>
                        <p>The data was last updated on January 26th, 2023.</p>
                    </div>
                </div>
                <div className="button-container">
                    <button onClick={startGame}>Play</button>
                </div>
            </section>
            )}
            {!showStartScreen && ! gameOver && (
                <section className="game-container" id="game-container">
                <div className="game-card">
                   <div className="card-image-container">
                        <img className="card-image" src={currentSong.displayImageUri}></img>
                   </div>
                   <div className="card-info-container">
                        <div className="p-container">
                            <p className="card-title">{currentSong.trackName}</p>
                            <p className="card-artist">{currentSong.name}</p>
                            <p>Has</p>
                        </div>
                        <h3 className="card-streams">{currentSong.value.toLocaleString()}</h3>
                   </div>
                   <p>streams</p>
                </div>
                <div className="vs-container">
                    <div className="circle">VS</div>
                </div>
                <div className="game-card">
                    <div className="card-image-container">
                        <img className="card-image" src={nextSong.displayImageUri}></img>
                   </div>
                   <div className="card-info-container">
                        <div className="p-container">
                            <p className="card-title">{nextSong.trackName}</p>
                            <p className="card-artist">{nextSong.name}</p>
                            <p>Has</p>
                        </div>
                   </div>
                    <div className="card-button-container">
                        <button onClick={handleHigher}>Higher</button>
                        <button onClick={handleLower}>Lower</button>
                    </div>
                    <p>streams</p>
                </div>
           </section>
            )}
            {!showStartScreen && gameOver && (
                <section>
                    <h1 className="citric">Game Over</h1>
                    <h2>Your final score was: <span>{score}</span></h2>
                    <div className="button-container">
                        <button onClick={resetGame}>Play Again</button>
                    </div>
                </section>
            )}
        </main>
    )
};

export default Game;