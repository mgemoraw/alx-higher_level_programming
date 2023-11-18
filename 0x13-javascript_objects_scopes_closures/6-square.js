#!/usr/bin/node
const Rectangle = require('./4-rectangle');

// Defines square object from Rectangle object
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  charPrint (c) {
    if (!c) {
      this.print();
    } else {
      for (let i = 0; i < this.size; i++) {
        console.log('C'.repeat(this.size));
      }
    }
  }
}

// exporting to module
module.exports = Square;
