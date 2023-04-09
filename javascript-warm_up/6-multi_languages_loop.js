#!/usr/bin/node
'use strict';

/**
 * Show multiple rows in a console only with array
 */
const lines = [
  'C is fun',
  'Python is cool',
  'JavaScript is amazing'
];

// We return to the line at each element of the array
const result = lines.join('\n');
console.log(result);
