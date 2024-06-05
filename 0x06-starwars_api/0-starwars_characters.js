#!/usr/bin/node
const request = require('request');

function printCharacters(movieId) {
    const url = `https://swapi.dev/api/films/${movieId}/`;

    request(url, (error, response, body) => {
        if (error || response.statusCode!== 200) {
            console.error('Error fetching data:', error);
            return;
        }

        const filmData = JSON.parse(body);

        const characters = filmData.characters;

        characters.forEach(characterUrl => {
            request(characterUrl, (err, res, charBody) => {
                if (err || res.statusCode!== 200) {
                    console.error('Error fetching character:', err);
                    return;
                }
                const character = JSON.parse(charBody);
                console.log(character.name);
            });
        });
    });
}

if (process.argv[2]) {
    const movieId = process.argv[2];
    printCharacters(movieId);
} else {
    console.error('Please provide a movie ID.');
}
