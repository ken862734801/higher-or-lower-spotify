import "./header.css";

function Header(){
    return (
        <header>
            <div className="header-container">
                <p className="citric">High Score: {0}</p>
                <p className="citric">Score: {0}</p>
            </div>
        </header>
    )
}

export default Header;