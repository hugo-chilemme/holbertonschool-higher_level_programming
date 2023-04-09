#!/usr/bin/node
'use strict';

/**
 * class Rectangle
 */
class Rectangle {
  /**
     * constructor
     * @param {number} w - Width
     * @param {number} h - Height
     * new Rectangle(2, 3);
     */
  constructor (w, h) {
    // When rectangle values are valid
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  /**
     * print()
     * Displays a rectangle with 'X'
     */
  print () {
    // In case initialization failed
    const width = this.width || 0;
    const height = this.height || 0;

    // Creation of a line template
    const line = 'X'.repeat(width);

    // Display of @h line
    for (let h = 0; h < height; h++) {
      console.log(line);
    }
  }

  /**
     * rotate()
     * Swap the width with the height
     */
  rotate () {
    const newWidth = this.height;
    const newHeight = this.width;

    this.width = newWidth;
    this.height = newHeight;
  }

  /**
     * double()
     * Double the width and height
     */
  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
