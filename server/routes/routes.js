const express = require("express");
const Song = require("../models/song.model");

const router = express.Router();

router.get("/", (req, res) => {
    Song.find()
        .sort({currentRank: 1})
        .then(songs => res.json(songs))
        .catch(err => res.status(400).json("Error: " + err));
});

router.get("/getOne/:id", (req, res) => {
    res.send(req.params.id)
});

module.exports = router;