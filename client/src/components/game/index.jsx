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

    return (
        <main>
            <div className="game-container">
                <div className="game-card">
                    <img src={image_1}></img>
                </div>
                <div className="game-card">
                    <img src={image_2}></img>
                </div>
            </div>
            <button onClick={getData}></button>
        </main>
    )
};

export default Game;