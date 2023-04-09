#!/usr/bin/node
'use strict';

const Rectangle = require('./4-rectangle');

/**
 * class Square
 */
class Square extends Rectangle {
  /**
     * constructor
     * @param {number} size - Size
     * new Square(2);
     */
  constructor (size) {
    super();
    // When rectangle values are valid
    if (size > 0) {
      this.width = size;
      this.height = size;
    }
  }
}

module.exports = Square;
