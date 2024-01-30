#!/usr/bin/node
const fs = require('fs');

// file path
const filePath = process.argv[2];
const data = process.argv[3];

// function that writes text to a file
fs.writeFile(filePath, data, 'utf8', (err) => {
  if (err) throw err;
});
