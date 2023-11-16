#!/usr/bin/node
const args = process.argv;
function factorial (num) {
  if (num === 0) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}
// get number from argument
if (!parseInt(args[2])) {
  console.log(factorial(0));
} else {
  console.log(factorial(parseInt(args[2])));
}
