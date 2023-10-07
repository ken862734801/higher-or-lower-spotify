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

app.use("/api", routes);

if(process.env.NODE_ENV === "production"){
    app.use(express.static("client/build"));

    app.get("*", (req, res) => res.sendFile(path.resolve(__dirname, "client", "build", "index.html")));
}

app.listen(port, () => {
    console.log(`server started at ${port}!`)
});