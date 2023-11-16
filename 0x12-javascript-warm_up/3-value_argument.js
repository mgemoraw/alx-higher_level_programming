#!/usr/bin/node
const args = process.argv;
let x = 3;
// print proccess.argv
if (args[1] === 'undefined') {
  console.log('No argument');
} else {
  console.log(`${args[2]}`);
}
