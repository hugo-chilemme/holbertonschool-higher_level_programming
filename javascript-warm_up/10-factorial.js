#!/usr/bin/node
'use strict';

/**
 * Create function to factorial @arg1 and @arg2
 */
const args = process.argv.slice(2);
const number1 = parseInt(args[0]);

const factorial = number => {
  if (number === 0) {
    return 1;
  }
  return number * factorial(number - 1);
};

console.log(factorial(number1));
