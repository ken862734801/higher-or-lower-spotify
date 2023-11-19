import './end-screen.css';
import Button from "../button/Button";

function EndScreen (props){
    const { gameState, restartGame } = props;
    return (
        <div className="end-screen">
            <h1 className="citric">Game Over</h1>
            <h2>Your final score was:</h2>
            <h2 className='final-score'>{ gameState.score }</h2>
            <div className="end-screen-button--container">
                <Button handleOnClick={restartGame} text={'play again'}/>
            </div>
        </div>
    )
};

export default EndScreen;