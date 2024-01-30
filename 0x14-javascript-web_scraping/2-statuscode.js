#!/usr/bin/node
const request = require('request');

// url
const url = process.argv[2];

// get status code of fetch request
request(url, (err, response, body) => {
  // check if error is returned
  if (err) throw err;
  // console.log(err);

  // else print status code
  console.log(response.statusCode);
});
