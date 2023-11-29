#!/usr/bin/node
const Square1 = require('./5-square');

// Defines square object from Rectangle object
class Square extends Square1 {
  charPrint (c) {
    if (!c) {
      c = 'X';
    }
    for (let r = 0; r < this.height; r++) {
      let ss = '';
      for (let i = 0; i < this.width; i++) {
        ss += c;
      }
      console.log(ss);
    }
  }
}

// exporting to module
module.exports = Square;
