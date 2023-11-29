#!/usr/bin/node
//  Converts a number from bawse 10 to another base

exports.converter = function (base) {
  return function (num) {
    return num.toString(base);
  };
};
