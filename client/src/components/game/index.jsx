import "./game.css";
import React, {useEffect, useState} from 'react';

function Game(){
    const [image_1, setImage_1] = useState([]);
    const [image_2, setImage_2] = useState([]);

    function getData(){
        fetch("http://localhost:3000/spotify-global-200")
          .then(response => response.json())
          .then(data => {
            console.log(data)
            let song_1 = data[getRandomIndex().firstIndex]
            let song_2 = data[getRandomIndex().secondIndex]
            setImage_1(song_1.displayImageUri);
            setImage_2(song_2.displayImageUri);
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
    function hideStartScreen(){

    }

    return (
        <main>
            <section className="start-container">
                <div className="title-container">
                    <h1 className="citric">Welcome to</h1>
                    <h1 className="spearmint">Higher or Lower</h1>
                    <h1 className="fuschia">Music Edition</h1>
                    <div className="subtitle-container">
                        <h2>Can you guess the more popular song?</h2>
                        <p>A frustratingly addictive game of higher or lower using the top 200 songs from Spotify's global chart.</p>
                        <p>The data was last updated in January 2023.</p>
                    </div>
                </div>
                <div className="button-container">
                    <button onClick={getData}>Play</button>
                </div>
            </section>
            <div className="game-container">
                <div className="game-card">
                    <img src={image_1}></img>
                </div>
                <div className="game-card">
                    <img src={image_2}></img>
                </div>
            </div>
            <div className="end-container"></div>
        </main>
    )
};

export default Game;