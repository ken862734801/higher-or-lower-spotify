const mongoose = require("mongoose");

const songSchema = new mongoose.Schema({
    currentRank:{
        required: true,
        type:Number
    },
    trackName:{
        required: true,
        type: String
    },
    name: {
        required: true,
        type: String
    },
    displayImageUri: {
        required: true,
        type: String
    },
    value:{
        required: true,
        type: Number
    }
});

module.exports = mongoose.model("Song", songSchema)