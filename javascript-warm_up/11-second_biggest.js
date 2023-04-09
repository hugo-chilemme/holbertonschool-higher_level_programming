#!/usr/bin/node
'use strict';

/**
 * Create function to return the max number
 */
const args = process.argv.slice(2);

const maximum = (array = []) => {
  const numbers = [];
  for (let i = 0; i < array.length; i++) {
    numbers.push(parseInt(array[i]));
  }
  numbers.sort((a, b) => a - b);
  if (numbers.length < 2) {
    return 0;
  }
  return numbers[numbers.length - 2];
};

console.log(maximum(args));
