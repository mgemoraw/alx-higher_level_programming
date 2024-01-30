#!/usr/bin/node
const request = require('request');

// url
const url = process.argv[2];

// get status code of fetch request
request(url, (_err, response) => {
  // check if error is returned
  if (_err) throw _err;

  // else print status code
  console.log('code:', response.statusCode);
});
