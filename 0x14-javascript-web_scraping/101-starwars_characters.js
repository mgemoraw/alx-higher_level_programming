#!/usr/bin/node
const request = require('request');

// Specifying the file path
const movieId = process.argv[2];
// const SWAPI = 'https://swapi-api.alx-tools.com/api/films/'.concat(movieId);

function getDataFrom (url) {
  return new Promise((resolve, reject) => {
    request(url, (err, _response, data) => {
      if (err) {
        reject(err);
      } else {
        resolve(data);
      }
    });
  });
}

const errHandler = (err) => {
  console.log(err);
};

function printMovieCharacters (movieId) {
  const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
  getDataFrom(url)
    .then(JSON.parse, errHandler)
    .then(function (res) {
      const chars = res.characters;
      const promises = [];

      for (let i = 0; i < chars.length; ++i) {
        promises.push(getDataFrom(chars[i]));
      }

      Promise.all(promises)
        .then((results) => {
          for (let i = 0; i < results.length; ++i) {
            console.log(JSON.parse(results[i]).name);
          }
        })
        .catch((err) => {
          console.log(err);
        });
    });
}

printMovieCharacters(movieId);
