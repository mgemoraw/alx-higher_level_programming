#!/usr/bin/node
const args = process.argv;
function getSecondMax (args) {
  let max = parseInt(args[2]);
  let smax = parseInt(args[2]);
  for (let i = 3; i < args.length; i++) {
    if (parseInt(args[i]) > max) {
      max = parseInt(args[i]);
    }
  }
  for (let j = 3; j < args.length; j++) {
    if ((parseInt(args[j]) < max) && (parseInt(args[j]) > smax)) {
      smax = parseInt(args[j]);
    }
  }
  return (smax);
}
// get number from argument
if ((!parseInt(args[2])) || (!parseInt(args[3]))) {
  console.log(0);
} else {
  console.log(getSecondMax(args));
}
