#!/usr/bin/nodejs
const fs = require('fs');

// Specifying the file path
const filePath = process.argv[2];
const data = process.argv[3];

writeFile(filePath);

function writeFile (filePath) {
  // Read the content of the file asynchronously
  fs.writeFile(filePath, data, 'utf8', (err) => {
    if (err) {
      // Handles errors, e.g., file not found
      console.log(err);
    }
  });
}
