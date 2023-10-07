import "./header.css";

export default function Header (props) {
    const { highScore, score } = props;
    return (
        <header>
            <div className="header--container">
                <p>High Score: {highScore}</p>
                <p>Score: {score}</p>
            </div>
        </header>
    )
};