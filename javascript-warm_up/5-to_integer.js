#!/usr/bin/node
'use strict';

/**
 * Display 'My number: @arg' if it is a number
 */
const args = process.argv.slice(2);
const number = parseInt(args[0]);

// When number is a digit
if (isNaN(number)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${parseInt(args[0])}`);
}
