#!/usr/bin/node
const args = process.argv;

// print proccess.argv
if (!args[2]) {
  console.log('No argument');
} else {
  console.log(`${args[2]}`);
}
