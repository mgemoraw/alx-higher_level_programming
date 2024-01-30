const fs = require('fs');


const filePath = process.argv[2];



// function that reads and prints a file
fs.readFile(filePath, (err, data) => {
    if (err) throw err;
    console.log(data.toString());
});
