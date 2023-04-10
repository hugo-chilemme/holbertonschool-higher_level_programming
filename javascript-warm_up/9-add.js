#!/usr/bin/node
'use strict';

/**
 * main
 * Create a script to addition @firstArg and @secondArg
 */
function main () {
  const args = process.argv.slice(2);
  const number1 = parseInt(args[0]);
  const number2 = parseInt(args[1]);

  console.log(number1 + number2);
}

main();
