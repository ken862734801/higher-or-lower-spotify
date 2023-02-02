import "./game.css";
import React, {useRef, useEffect, useState} from 'react';


function Game(){

    const higher = useRef(false)
    const answer = useRef(false)

    const [image_1, setImage_1] = useState("");
    const [image_2, setImage_2] = useState("");
    const [title_1, setTitle_1] = useState("");
    const [title_2, setTitle_2] = useState("");
    const [artist_1, setArtist_1] = useState("");
    const [artist_2, setArtist_2] = useState("");
    const [value_1, setValue_1] = useState("")

    function getData(){
        fetch("http://localhost:3000/spotify-global-200")
          .then(response => response.json())
          .then(data => {
            console.log(data)
            displayGameScreen()
            let song_1 = data[getRandomIndex().firstIndex]
            let song_2 = data[getRandomIndex().secondIndex]
            displayInitialGameState(song_1, song_2)
            compareStreams(song_1, song_2);
            console.log(song_1.value);
            console.log(song_2.value);
          })
          .catch(err => {
            console.log(err)
          })
      };

      function displayInitialGameState(song1, song2){
        setImage_1(song1.displayImageUri);
        setTitle_1(song1.trackName);
        setArtist_1(song1.name);
        setValue_1(song1.value.toLocaleString());

        setImage_2(song2.displayImageUri)
        setTitle_2(song2.trackName)
        setArtist_2(song2.name)

      };
      
      function getRandomIndex(){
        let firstIndex = Math.floor(Math.random()*(200));
        let secondIndex = Math.floor(Math.random()*(200));
          while (firstIndex === secondIndex){
              secondIndex = Math.floor(Math.random()*(200));
            }
            return {firstIndex, secondIndex}
      };

      function displayGameScreen(){
        let startScreen = document.getElementById("start-container");
        let gameScreen = document.getElementById("game-container");
        startScreen.classList.add("hide");
        gameScreen.classList.remove("hide");
      };

    //   function displayEndScreen(){
    //     let gameScreen = document.getElementById("game-container");
    //     let endScreen = document.getElementById("end-container");
    //     gameScreen.classList.add("hide");
    //     endScreen.classList.remove("hide");
    //   };

      function getUserAnswer(e){
        if(e.target.id === "higher-btn"){
            answer.current = true;
            console.log("User thinks it is higher!");
            checkIfCorrect()
        }else if(e.target.id === "lower-btn"){
            answer.current = false;
            console.log("User thinks it is lower!");
            checkIfCorrect()
        }
      };

      function compareStreams(song1, song2){
        if(song1.value > song2.value){
            higher.current = false;
            console.log("It is not higher!")
        }else if(song1.value < song2.value){
            higher.current = true;
            console.log("It is higher!");
        }
      };

      function checkIfCorrect(){
        if(higher.current === answer.current){
            console.log("Correct!");
        }else if(higher.current !== answer.current){
            console.log("Incorrect!");
        }
      };

    return (
        <main>
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
                    <button onClick={getData}>Play</button>
                </div>
            </section>
            <section className="hide game-container" id="game-container">
                <div className="game-card">
                   <div className="card-image-container">
                        <img className="card-image" src={image_1}></img>
                   </div>
                   <div className="card-info-container">
                        <p className="card-title">{title_1}</p>
                        <p className="card-artist">{artist_1}</p>
                        <p>Has</p>
                        <h3 className="card-streams">{value_1}</h3>
                   </div>
                   <p className="streams">Streams</p>
                </div>
                <div className="vs-container">
                    <div className="circle">VS</div>
                </div>
                <div className="game-card">
                    <div className="card-image-container">
                        <img className="card-image" src={image_2}></img>
                   </div>
                   <div className="card-info-container">
                        <p className="card-title">{title_2}</p>
                        <p className="card-artist">{artist_2}</p>
                        <p>Has</p>
                   </div>
                    <div className="card-button-container">
                        <button onClick={getUserAnswer} id="higher-btn">Higher</button>
                        <button onClick={getUserAnswer} id="lower-btn">Lower</button>
                    </div>
                    <p className="streams">Streams</p>
                </div>
            </section>
            <section className="hide end-container" id="end-container"></section>
        </main>
    )
};

export default Game;