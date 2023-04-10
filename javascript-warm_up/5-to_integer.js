#!/usr/bin/node
'use strict';

/**
 * main
 * Create script to display My number: @number if it is a number
 */
function main () {
  const number = parseInt(process.argv[2]);

  // When number is a digit
  if (isNaN(number)) {
    console.log('Not a number');
    return;
  }

  console.log(`My number: ${number}`);
}

main();
