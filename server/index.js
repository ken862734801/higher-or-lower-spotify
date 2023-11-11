require("dotenv").config();
const path = require('path');

const express = require("express");
const mongoose = require("mongoose");
const cors = require("cors");
const mongoString = process.env.DATABASE_URL;

const routes = require("./routes/routes");
const Song = require("./models/song.model");
const data = require("./seeds/chart_data.json");

mongoose.connect(mongoString);
const db = mongoose.connection;

const port = process.env.PORT || 8080;

db.on("error", (error) => {
    console.log(error)
});

db.once("open", async () => {
    try{
        await Song.deleteMany({});
        await Song.create(data);
        console.log("The database has been seeded!")
    } catch (err){
        throw err;
    }
});

db.once("connected", () => {
    console.log("The database is connected!")
});

const app = express();

app.use(express.json());
app.use(cors());

app.use((req, res, next) => {
    const apiKey = req.header("X-API-Key");

    if (apiKey === process.env.API_KEY) {
        next();
    } else {
        res.status(401).json("Invalid X-API Key");
    }
});

app.use("/api", routes);

app.listen(port, () => {
    console.log(`server started at ${port}!`)
});