// npm install -g express-generator

const express = require('express');
const axios = require('axios');

const app = express();
const PORT = 3000;

app.get('/', async (req, res) => {
    try {
        const response = await axios.get('http://localhost:5000/'); // Flask server
        res.json(response.data);
    } catch (error) {
        console.error(error);
        res.status(500).send('Internal Server Error');
    }
});

app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});