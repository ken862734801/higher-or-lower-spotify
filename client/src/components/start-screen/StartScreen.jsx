import './start-screen.css';
import Button from '../button/Button';

function StartScreen(props){
    const { startGame } = props;
    return (
        <div className='start-screen'>
            <div className='heading--container'>
                <h1 className='citric'>Welcome To</h1>
                <h1 className='spearmint'>Higher Or Lower</h1>
                <h1 className='fuschia'>Spotify Edition</h1>
                <div className='sub-heading--container'>
                    <h2>Can you guess the more popular song?</h2>
                </div>
            </div>
            <div className='button--container'>
                <Button handleOnClick={ startGame } text={ 'play' }/>
            </div>
        </div>
    )
};

export default StartScreen;