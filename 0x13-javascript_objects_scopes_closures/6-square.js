#!/usr/bin/node
const Square1 = require('./5-square');

// Defines square object from Rectangle object
class Square extends Square1 {
  constructor (size) {
    super(size);
  }

  charPrint (c) {
    if (!c) {
      this.print();
    } else {
      for (let i = 0; i < this.size; i++) {
        console.log(c.repeat(this.size));
      }
    }
  }
}

// exporting to module
module.exports = Square;
