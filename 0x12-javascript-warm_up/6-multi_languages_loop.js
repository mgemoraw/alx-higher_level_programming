#!/usr/bin/node
const args = process.argv;

// prints My number: <first argument converted in integer>
if (!(parseInt(args[2]))) {
  console.log('Not a number');
} else {
  console.log(`My number: ${parseInt(args[2])}`);
}
