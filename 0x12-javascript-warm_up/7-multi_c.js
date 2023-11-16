#!/usr/bin/node
const args = process.argv;

// collecting arguments
if (!parseInt(args[2])) {
  console.log('Missing number of occurences');
} else {
  const x = parseInt(args[2]);
  for (let t = 0; t < x; t++) {
    console.log('C is fun');
  }
}
