#!/usr/bin/node
const fs = require('fs');


const filePath = process.argv[2];



// function that reads and prints a file
fs.readFile(filePath, 'utf8', (err, data) => {
    if (err) throw err;
    // console.log(data.toString());
    process.stdout.write(data);
});
