import './button.css';

function Button(props){
    const { handleOnClick, text } = props;
    return (
        <button onClick={handleOnClick} className='button--element'>{ text }</button>
    )
};

export default Button;