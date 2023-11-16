#!/usr/bin/node
const args = process.argv;

// collecting arguments
if (!parseInt(args[2])) {
  console.log('Missing size');
} else {
  const x = parseInt(args[2]);
  for (let row = 0; row < x; row++) {
    console.log('x'.repeat(x));
  }
}
