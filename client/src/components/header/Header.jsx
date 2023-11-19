import './header.css';

function Header(props){
    const { gameState } = props;
    return (
        <header>
            <div className='header--container'>
                <p>High Score: { gameState.highScore }</p>
                <p>Score: { gameState.score } </p>
            </div>
        </header>
    )
};

export default Header;