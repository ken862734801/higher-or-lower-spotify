import "./header.css";


function Header(props){
    return (
        <header>
            <div className="header-container">
                <p className="citric">High Score: {}</p>
                <p className="citric">Score: {props.score}</p>
            </div>
        </header>
    )
}

export default Header;