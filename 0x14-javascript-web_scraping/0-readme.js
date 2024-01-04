#!/usr/bin/nodejs
const fs = require('fs');

// Specifying the file path
const filePath = process.argv[2];

readFile(filePath);

function readFile (filePath) {
  // Read the content of the file asynchronously
  fs.readFile(filePath, 'utf8', (err, data) => {
    if (err) {
      // Handles errors, e.g., file not found
      console.log(err);
    } else {
      // Read and pring the contents of the file
      process.stdout.write(data)
    }
  });
}
