import "./game.css";
import React, {useRef, useEffect, useState} from 'react';


// function Game(){

//     const [image_1, setImage_1] = useState("");
//     const [image_2, setImage_2] = useState("");
//     const [title_1, setTitle_1] = useState("");
//     const [title_2, setTitle_2] = useState("");
//     const [artist_1, setArtist_1] = useState("");
//     const [artist_2, setArtist_2] = useState("");
//     const [value_1, setValue_1] = useState("");

//     let apiUrl = "http://localhost:3000/spotify-global-200";
//     let song_1;
//     let song_2;

//     async function getData(url){
//         let response = await fetch(url);
//         let data = await response.json()
//         return data
//     };
    
//     async function useData(){
//         let array = [];
//         let chartData = await getData(apiUrl);
//         if(array.length === 0){
//             song_1 = chartData[getRandomIndex().firstIndex];
//             song_2 = chartData[getRandomIndex().secondIndex];
//             console.log(song_1, song_2);  
//         }else if(array.length >= 1){
//             song_1 = array[0];
//             song_2 = chartData[getRandomIndex().secondIndex];
//             console.log(song_1, song_2);  
//         }
//         displayGameScreen();
//         displayInitialGameState(song_1, song_2);

//         return {song_1, song_2}
//     }



//     // function getData(){
//     //     displayGameScreen();
//     //     let song_1 = "test";
//     //     let song_2 = "test";
//     //     fetch("http://localhost:3000/spotify-global-200")
//     //         .then(function(response){
//     //             if(response.ok){
//     //                 response.json().then(function(data){
//     //                     console.log(data);
//     //                     console.log(song_1, song_2)
//     //                 buttons.forEach(button => {
//     //                     button.addEventListener("click", (e) => {
//     //                         song_1 = "new";
//     //                         song_2 = "new";
//     //                         console.log(song_1, song_2)
//     //                     })
//     //                 })  

//     //                 })
//     //             }else{
//     //                 console.log("Error: " + response.statusText)
//     //             }
//     //         })
//     // };

//       function displayInitialGameState(song1, song2){
//         setImage_1(song1.displayImageUri);
//         setTitle_1(song1.trackName);
//         setArtist_1(song1.name);
//         setValue_1(song1.value.toLocaleString());

//         setImage_2(song2.displayImageUri)
//         setTitle_2(song2.trackName)
//         setArtist_2(song2.name)

//       };
      
//       function getRandomIndex(){
//         let firstIndex = Math.floor(Math.random()*(200));
//         let secondIndex = Math.floor(Math.random()*(200));
//           while (firstIndex === secondIndex){
//               secondIndex = Math.floor(Math.random()*(200));
//             }
//             return {firstIndex, secondIndex}
//       };

//       function displayGameScreen(){
//         let startScreen = document.getElementById("start-container");
//         let gameScreen = document.getElementById("game-container");
//         startScreen.classList.add("hide");
//         gameScreen.classList.remove("hide");
//       };


//     return (
//         <main>
//             <section className="start-container" id="start-container">
//                 <div className="title-container">
//                     <h1 className="citric">Welcome to</h1>
//                     <h1 className="spearmint">Higher or Lower</h1>
//                     <h1 className="fuschia">Music Edition</h1>
//                     <div className="subtitle-container">
//                         <h2>Can you guess the more popular song?</h2>
//                         <p>A frustratingly addictive game of higher or lower using the top 200 songs from Spotify's global chart.</p>
//                         <p>The data was last updated on January 26th, 2023.</p>
//                     </div>
//                 </div>
//                 <div className="button-container">
//                     <button onClick={useData}>Play</button>
//                 </div>
//             </section>
//             <section className="hide game-container" id="game-container">
//                 <div className="game-card">
//                    <div className="card-image-container">
//                         <img className="card-image" src={image_1}></img>
//                    </div>
//                    <div className="card-info-container">
//                         <p className="card-title">{title_1}</p>
//                         <p className="card-artist">{artist_1}</p>
//                         <p>Has</p>
//                         <h3 className="card-streams">{value_1}</h3>
//                    </div>
//                    <p className="streams">Streams</p>
//                 </div>
//                 <div className="vs-container">
//                     <div className="circle">VS</div>
//                 </div>
//                 <div className="game-card">
//                     <div className="card-image-container">
//                         <img className="card-image" src={image_2}></img>
//                    </div>
//                    <div className="card-info-container">
//                         <p className="card-title">{title_2}</p>
//                         <p className="card-artist">{artist_2}</p>
//                         <p>Has</p>
//                    </div>
//                     <div className="card-button-container">
//                         <button className="answer-btn"  id="higher-btn">Higher</button>
//                         <button className="answer-btn"  id="lower-btn">Lower</button>
//                     </div>
//                     <p className="streams">Streams</p>
//                 </div>
//             </section>
//             <section className="hide end-container" id="end-container"></section>
//         </main>
//     )
// };

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

    const handleHigher = () => {
        if(nextSong.value > currentSong.value){
            setCurrentSong(nextSong);
            const index = getRandomIndex(data);
            setNextSong(data[index.secondIndex])
        }else{
            setGameOver(true)
        }
    };

    const handleLower = () => {
        if(nextSong.value < currentSong.value){
            setCurrentSong(nextSong);
            const index = getRandomIndex(data);
            setNextSong(data[index.secondIndex])
        } else {
            setGameOver(true)
        }
    }

    return (
        <main>
            {showStartScreen ? (
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
            ):(<section></section>)}
            {gameOver ? (<section><p>Game Over!</p></section>):
            (
            <section className="game-container" id="game-container">
                 <div className="game-card">
                    <div className="card-image-container">
                         <img className="card-image" src={currentSong.displayImageUri}></img>
                    </div>
                    <div className="card-info-container">
                         <p className="card-title">{currentSong.trackName}</p>
                         <p className="card-artist">{currentSong.name}</p>
                         <p>Has</p>
                         <h3 className="card-streams">{currentSong.value}</h3>
                    </div>
                    <p className="streams">Streams</p>
                 </div>
                 <div className="vs-container">
                     <div className="circle">VS</div>
                 </div>
                 <div className="game-card">
                     <div className="card-image-container">
                         <img className="card-image" src={nextSong.displayImageUri}></img>
                    </div>
                    <div className="card-info-container">
                         <p className="card-title">{nextSong.trackName}</p>
                         <p className="card-artist">{nextSong.name}</p>
                         <p>Has</p>
                    </div>
                     <div className="card-button-container">
                         <button onClick={handleHigher}>Higher</button>
                         <button onClick={handleLower}>Lower</button>
                     </div>
                     <p className="streams">Streams</p>
                 </div>
            </section>)}
        </main>
    )
};

export default Game;