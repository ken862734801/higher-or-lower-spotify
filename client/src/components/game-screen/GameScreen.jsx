import "./game-screen.css";
import GameCard from "../game-card/GameCard";
export default function GameScreen (props) {
    const { 
            handleSelectHigher,
            handleSelectLower,
            nextSong,
            currentSong,
            displayNextSong, 
            containerClassName, 
            text} = props;
    return (
        <div className="game-screen--container">
            <GameCard song={currentSong} status={"primary"} displayNextSong={false}/>
            <div className="vs--container">
                <div className={containerClassName}>{text}</div>
            </div>
            <GameCard handleSelectHigher={handleSelectHigher}
                      handleSelectLower={handleSelectLower} 
                      song={nextSong} status={"secondary"} 
                      displayNextSong={displayNextSong}/>
        </div>
    )
}