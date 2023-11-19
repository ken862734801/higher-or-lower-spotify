import './game-screen.css';
import CountUp from 'react-countup';

function GameScreen(props){
    const { displayOptions, gameState, handleUserChoice } = props;
    return (
        <div className='game-screen'>
            <div className='game-card'>
                <div className='game-card-image--container'>
                    <img className='game-card-image' src={(gameState.currentSong).displayImageUri}></img>
                </div>
                <div className='game-card-text--container'>
                    <div className='p-elements--container'>
                        <p className='game-card-song' title={(gameState.currentSong).trackName}>{(gameState.currentSong).trackName}</p>
                        <p className='game-card-artist'>{(gameState.currentSong).name}</p>
                        <p>Has</p>
                    </div>
                    <h3 className='game-card-stream-count'>{(gameState.currentSong).value.toLocaleString()}</h3>
                </div>
                <span>
                    <p>streams</p>
                </span>
            </div>
            <div className='feedback-text--container'>
                <p className={`feedback-text ${ gameState.isCorrect? 'correct' : gameState.isCorrect === false? 'incorrect' : '' }`}> { gameState.feedbackText } </p>
            </div>
            <div className='game-card'>
                <div className='game-card-image--container'>
                    <img className='game-card-image' src={(gameState.nextSong).displayImageUri}></img>
                </div>
                <div className='game-card-text--container'>
                    <div className='p-elements--container'>
                        <p className='game-card-song' title={(gameState.nextSong).trackName}>{(gameState.nextSong).trackName}</p>
                        <p className='game-card-artist'>{(gameState.nextSong).name}</p>
                        <p>Has</p>
                    </div>
                    {displayOptions.showStreamCount && (
                        <CountUp start={(gameState.nextSong).value * 0.95} end={(gameState.nextSong).value} duration={2} separator=',' delay={0}>
                             {({ countUpRef }) => <h3 className='game-card-stream-count' ref={countUpRef} />}
                        </CountUp>
                    )}
                </div>
                {!displayOptions.showStreamCount && (
                    <div className='game-card-button--container'>
                        <button onClick={()=> handleUserChoice('Higher')}>Higher</button>
                        <button onClick={()=> handleUserChoice('Lower')}>Lower</button>
                    </div>
                )}
                <span>streams</span>
            </div>
        </div>
    )
};

export default GameScreen;