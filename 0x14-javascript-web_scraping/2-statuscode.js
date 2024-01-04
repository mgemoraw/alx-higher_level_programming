#!/usr/bin/node
const request = require('request');

// Specifying the file path
const movieId = process.argv[2];
const  SWAPI = 'https://swapi-api.alx-tools.com/api/films/'.concat(movieId);

// getting requests
request(SWAPI, (err, data, b) => {
  b = JSON.parse(b);
  // print respons status code to the console
  console.log(b.title);
});
