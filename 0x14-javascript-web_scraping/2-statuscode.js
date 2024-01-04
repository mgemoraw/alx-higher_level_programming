#!/usr/bin/node
const request = require('request');

// Specifying the file path
const url = process.argv[2];

// getting requests
request(url, (err, data) => {
  // print respons status code to the console
  console.log('code:', data.statusCode);
});
