#!/usr/bin/node
'use strict';

/**
 * main
 * Create a script to addition @firstArg and @secondArg
 */
function main () {
  const number = parseInt(process.argv[2]);

  const factorialNumber = factorial(number);

  console.log(factorialNumber);
}

/**
 * factorial
 * @param {number} number - Number to factorise
 * factorial(3);
 */
const factorial = number => {
  if (number === 0 || !number) {
    return 1;
  }
  return number * factorial(number - 1);
};

main();
