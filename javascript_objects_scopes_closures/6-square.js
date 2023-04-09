#!/usr/bin/node
'use strict';

const oldSquare = require('./5-square.js');

/**
 * class Square
 */
class Square extends oldSquare {
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

  /**
     * charPrint()
     * @param {char} char
     * Displays the square with this character
     */
  charPrint (char = 'X') {
    // In case initialization failed
    const size = this.width || 0;

    // Creation of a line template
    const line = char.repeat(size);

    // Display of @h line
    for (let s = 0; s < size; s++) {
      console.log(line);
    }
  }
}

module.exports = Square;
