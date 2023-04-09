#!/usr/bin/node
'use strict';

/**
 * Create function to return the max number
 */
const args = process.argv.slice(2);

const maximum = (numbers = []) => {
  if (numbers.length === 0) {
    return 0;
  }
  return Math.max(...numbers);
};

console.log(maximum(args));
