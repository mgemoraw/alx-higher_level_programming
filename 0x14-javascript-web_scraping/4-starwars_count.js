#!/usr/bin/node
const request = require('request');

// url
const SWAPI = process.argv[2];
// const SWAPI = 'https://swapi-api.alx-tools.com/api/films/'.concat(movieId);

let counter = 0;
// get status code of fetch request
request(SWAPI, (_err, _data, movie) => {
  // parse movie using JSON
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
  // print movie title with correspoinding id
  console.log(counter);
});
