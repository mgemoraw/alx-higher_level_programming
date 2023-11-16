#!/usr/bin/node
let nb = 0;
function addMeMaybe (number, theFunction) {
  theFunction();
  nb = number + 1;
}

exports.nb = nb;
exports.addMeMaybe = addMeMaybe;
