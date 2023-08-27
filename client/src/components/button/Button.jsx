import "./button.css";
export default function Button (props){
    const { handleClick, buttonText } = props;
    return (
        <button className="button--element" onClick={handleClick}>{buttonText}</button>
    )
}