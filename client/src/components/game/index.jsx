import "./game.css";
import React, { useEffect, useState} from 'react';
// handle animations
import CountUp from "react-countup";


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
    const apiUrl = "/api/";
    const [showStartScreen, setShowStartScreen] = useState(true);
    const [data, setData] = useState([]);
    const [currentSong, setCurrentSong] = useState({});
    const [nextSong, setNextSong] = useState({});
    const [displayNextSong, setDisplayNextSong] = useState(false);
    const [isCorrect, setIsCorrect] = useState(false);
    const [isWrong, setIsWrong] = useState(false);
    const [circleText, setCircleText] = useState("VS");
    const [gameOver, setGameOver] = useState(false);
    const [score, setScore] = useState(0);
    const [highScore, setHighScore] = useState(0);


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
    [data]);

    useEffect(()=> {
        let highScore = localStorage.getItem("highScore");
        if(!highScore){
            localStorage.setItem("highScore", 0);
            highScore = 0;
        };
        setHighScore(highScore);
    }, []);

    useEffect(() => {
        if (score > highScore){
            localStorage.setItem("highScore", score);
            setHighScore(score);
        }
    }, [score]);

    const startGame = () => {
        setShowStartScreen(false)
    };

    const resetGame = () => {
        const index = getRandomIndex(data);
        setCurrentSong(data[index.firstIndex]);
        setNextSong(data[index.secondIndex]);
        setShowStartScreen(true);
        setGameOver(false);
        setScore(0);
      };

    const displaySongValue = () => {
        setDisplayNextSong(true);
        setTimeout(() => {
            setDisplayNextSong(false)
        }, 3000)
    };

    const handleChangeColor = (answer) => {
        setIsCorrect(false);
        setIsWrong(false);
        if ((answer === "Higher" && nextSong.value > currentSong.value) || (answer === "Lower" && nextSong.value < currentSong.value)) {
            setIsCorrect(true);
                setCircleText("\u2713");
            setTimeout(() => {
                setIsCorrect(false);
            }, 1000);
            setTimeout(() => {
                setCircleText("VS");
            }, 1000);
        } else {
            setIsWrong(true);
                setCircleText("✗");
            setTimeout(() => {
                setIsWrong(false);
            }, 2000);
            setTimeout(() => {
                setCircleText("VS");
            }, 2000);
        }
    };
    

    const handleHigher = () => {
        if(nextSong.value > currentSong.value){
            displaySongValue();
            setTimeout(() => {
            handleChangeColor("Higher");
            }, 2000);
            setTimeout(() => {
                window.scrollTo(0,0);
                setCurrentSong(nextSong);
                const index = getRandomIndex(data);
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
                const index = getRandomIndex(data);
                setNextSong(data[index.secondIndex]);
                setScore(score + 1);
                }, 3000);
        }else {
            displaySongValue();
            setTimeout(() => {
                handleChangeColor("Higher");
            }, 2000);
            setTimeout(() => {
                setGameOver(true)
            }, 2750);
        }
    };

    const handleLower = () => {
        if(nextSong.value < currentSong.value){
            displaySongValue();
            setTimeout(() => {
                handleChangeColor("Lower");
                }, 2000);
            setTimeout(() => {
                window.scrollTo(0,0);
                setCurrentSong(nextSong);
                const index = getRandomIndex(data);
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
                const index = getRandomIndex(data);
                setNextSong(data[index.secondIndex]);
                setScore(score + 1);
                }, 3000);
        }else {
            displaySongValue();
            setTimeout(() => {
                handleChangeColor("Lower");
                }, 2000);
            setTimeout(() => {
                setGameOver(true)
            }, 2750);
        }
    }
    const circleClass = `circle ${isCorrect ? "green" : isWrong ? "red" : ""}`;
    return (
        <main>
            <header>
                <div className="header-container">
                    <p className="citric">High Score: {highScore}</p>
                    <p className="citric">Score: {score}</p>
                </div>
            </header>
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
                        <img className="card-image" id="card-image" src={currentSong.displayImageUri}></img>
                   </div>
                   <div className="card-info-container">
                        <div className="p-container">
                            <p className="card-title">{currentSong.trackName}</p>
                            <p className="card-artist">{currentSong.name}</p>
                            <p>Has</p>
                        </div>
                        <h3 className="card-streams">{currentSong.value.toLocaleString()}</h3>
                   </div>
                   <p className="p-streams">streams</p>
                </div>
                <div className="vs-container">
                    <div className={circleClass}>{circleText}</div>
                </div>
                <div className="game-card" id="game-card-one">
                    <div className="card-image-container">
                        <img className="card-image" src={nextSong.displayImageUri}></img>
                   </div>
                   <div className="card-info-container">
                        <div className="p-container">
                            <p className="card-title">{nextSong.trackName}</p>
                            <p className="card-artist">{nextSong.name}</p>
                            <p>Has</p>
                        </div>
                    {displayNextSong && (
                        <CountUp start={nextSong.value * 0.95} end={nextSong.value} duration={2} separator="," delay={0}>
                            {({ countUpRef}) => (
                                <h3 className="card-streams" ref={countUpRef}/>
                            )}
                        </CountUp>
                        )}
                   </div>
                    {!displayNextSong && (<div className="card-button-container">
                        <button onClick={handleHigher}>Higher</button>
                        <button onClick={handleLower}>Lower</button>
                    </div>)}
                    <p className="p-streams">streams</p>
                </div>
           </section>
            )}
            {!showStartScreen && gameOver && (
                <section className="end-container">
                    <h1 className="citric">Game Over</h1>
                    <h2>Your final score was:</h2>
                    <h2><span className="number">{score}</span></h2>
                    <div className="button-container">
                        <button onClick={resetGame}>Play Again</button>
                    </div>
                </section>
            )}
        </main>
    )
};

export default Game;