require("dotenv").config();

const express = require("express");
const mongoose = require("mongoose");
const cors = require("cors");
const mongoString = process.env.DATABASE_URL;

const routes = require("./routes/routes");
const Song = require("./models/song.model");
const data = require("./seeds/chart_data.json");

mongoose.connect(mongoString);
const db = mongoose.connection;

db.on("error", (error) => {
    console.log(error)
});

db.once("connected", () => {
    console.log("Database is connected!")
});

const app = express();

app.use(express.json());
app.use(cors());

app.use("/spotify-global-200", routes);

app.listen(3000, () => {
    console.log(`Server started at ${3000}`)
});