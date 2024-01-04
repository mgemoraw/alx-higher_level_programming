#!/usr/bin/node
const request = require('request');

// Specifying the file path
const swapi = process.argv[2];
// const SWAPI = 'https://swapi-api.alx-tools.com/api/films/'.concat(movieId);

let counter = 0;

// getting requests
request(swapi, (_err, _data, movie) => {
  movie = JSON.parse(movie).results;

  for (let i = 0; i < movie.length; ++i) {
    const chars = movie[i].characters;

    for (let j = 0; j < chars.length; ++j) {
      const char = chars[j];
      const charId = char.split('/')[5];

      if (charId === '18') {
        counter += 1;
      }
    }
  }
  // print respons status code to the console
  console.log(counter);
});
