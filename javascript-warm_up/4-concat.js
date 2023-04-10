#!/usr/bin/node
'use strict';

/**
 * main
 * Create a script to display @firstArg is @secondArg
 */
function main () {
  const args = process.argv.slice(2);
  console.log(args[0] + ' is ' + args[1]);
}

main();
