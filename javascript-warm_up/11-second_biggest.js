#!/usr/bin/node
'use strict';

/**
 * main
 * Create a script to return the second max number
 */
function main () {
  const args = process.argv.slice(2);

  console.log(secondMax(args));
}

/**
 * maximum
 * @param {array} array - Array to search
 * factorial([5, 7, 3, 2]); => 5
 */
const secondMax = (array = []) => {
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

main();
