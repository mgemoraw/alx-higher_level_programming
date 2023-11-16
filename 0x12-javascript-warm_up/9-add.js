#!/usr/bin/node
const args = process.argv;
function add (a, b) {
  return (a + b);
}

// adds two integers
const first = parseInt(args[2]);
const second = parseInt(args[3]);
console.log(add(first, second));
