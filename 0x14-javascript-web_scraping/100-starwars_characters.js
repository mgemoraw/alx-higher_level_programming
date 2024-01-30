#!/usr/bin/node
const request = require('request');

// Specifying the file path
const movieId = process.argv[2];
const SWAPI = 'https://swapi-api.alx-tools.com/api/films/'.concat(movieId);

// getting requests
request(SWAPI, (_err, _data, movie) => {
  const strings = JSON.parse(movie).characters;

  for (let i = 0; i < strings.length; ++i) {
    request(strings[i], (_cErr, _cRes, body) => {
      console.log(JSON.parse(body).name);
    });
  }
});
