import CountUp from "react-countup";
import "./game-card.css";

export default function GameCard (props) {
    const {handleSelectHigher, handleSelectLower, status, song, displayNextSong} = props;
    const isPrimary = status === 'primary';

   return (
    <div className="game-card">
        <div className="game-card-image--container">
            <img className="game-card-image" src={song.displayImageUri}></img>
        </div>
        <div className="game-card-text--container">
            <div className="p-element--container">
                <p className="card--title">{song.trackName}</p>
                <p className="card--artist">{song.name}</p>
                <p>Has</p>
            </div>
            {isPrimary && <h3 className="card-streams">{song.value.toLocaleString()}</h3>}
            {displayNextSong && !isPrimary && (
                <CountUp start={song.value * 0.95} end={song.value} duration={2} separator="," delay={0}>
                    {({ countUpRef }) => <h3 className="card-streams" ref={countUpRef} />}
                </CountUp>
            )}
        </div>
        {!isPrimary && !displayNextSong && (
            <div className="card-button--container">
                <button onClick={handleSelectHigher}>Higher</button>
                <button onClick={handleSelectLower}>Lower</button>
            </div>
        )}
        <p className="p-streams">streams</p>
    </div>
   )
}