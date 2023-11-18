#!/usr/bin/node
const Rectangle = require('./4-rectangle');

// Defines square object from Rectangle object
class Square extends Rectangle {
  constructor (w, h, size) {
    super(w, h);
    this.size = size;
  }
}

// exporting to module
module.exports = Square;
