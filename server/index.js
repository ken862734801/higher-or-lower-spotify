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

const port = process.env.PORT || 8080;

db.on("error", (error) => {
    console.log(error)
});

db.once("open", async () => {
    try{
        await Song.deleteMany({});
        await Song.create(data);
        console.log("all done!")
    } catch (err){
        throw err;
    }
});

db.once("connected", () => {
    console.log("database is connected!")
});

const app = express();

app.use(express.json());
app.use(cors());

app.use("/spotify-global-200", routes);

app.listen(port, () => {
    console.log(`server started at ${port}`)
});