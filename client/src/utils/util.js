
function getRandomSong(data){
    let firstIndex = Math.floor(Math.random() * data.length);
    let secondIndex = Math.floor(Math.random() * data.length);
    while (secondIndex === firstIndex){
        secondIndex = Math.floor(Math.random() * data.length);
    }
    return { firstIndex, secondIndex }
};

export { getRandomSong };