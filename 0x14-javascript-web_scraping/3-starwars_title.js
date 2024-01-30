#!/usr/bin/node
const request = require('request');

// url
const movieId = process.argv[2];
const SWAPI = 'https://swapi-api.alx-tools.com/api/films/'.concat(movieId);

// get status code of fetch request
request(SWAPI, (_err, _data, movie) => {
  // parse movie using JSON
  movie = JSON.parse(movie);
  // print movie title with correspoinding id
  console.log(movie.title);
});
