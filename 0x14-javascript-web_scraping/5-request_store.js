#!/usr/bin/node
const fs = require('fs');
const request = require('request');

// Specifying the file path
const url = process.argv[2];
const filePath = process.argv[3];

// getting requests
request(url, (_err, data) => {
  // writing result to the filepath
  fs.writeFile(filePath, data, 'utf8', (err) => {
    if (err) {
      console.log(err);
    }
  });
});
