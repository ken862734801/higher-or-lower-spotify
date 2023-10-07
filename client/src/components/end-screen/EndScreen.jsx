import "./end-screen.css";
import Button from "../button/Button";

export default function EndScreen (props) {
    const { handleGameReset, score } = props;
    return (
        <div className="end-screen--container">
            <h1 className="citric">Game Over</h1>
            <h2>Your final score was: </h2>
            <h2>
                <span className="number">{score}</span>
            </h2>
            <div className="button--container">
                <Button handleClick={handleGameReset} buttonText={"Play Again"}/>
            </div>
        </div>
    )
}