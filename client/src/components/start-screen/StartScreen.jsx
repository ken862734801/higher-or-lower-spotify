import "./start-screen.css";
import Button from "../button/Button";
export default function StartScreen (props) {
    const {startGame} = props;
    return (
        <div className="start-screen--container">
            <div className="title--container">
                <h1 className="citric">Welcome To</h1>
                <h1 className="spearmint">Higher Or Lower</h1>
                <h1 className="fuschia">Spotify Edition</h1>
                <div className="subtitle--container">
                    <h2>Can you guess the more popular song?</h2>
                </div>
            </div>
            <div className="button--container">
                <Button handleClick={startGame} buttonText={'Play'}/>
            </div>
        </div>
    )
} 