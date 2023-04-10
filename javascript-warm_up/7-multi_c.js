#!/usr/bin/node
'use strict';

/**
 * main
 * Create script to display multiples lines by a array
 */
function main () {
  const args = process.argv.slice(2);

  if (!args[0]) {
    console.log('Missing number of occurrences');
    return;
  }

  for (let i = 0; i < parseInt(args[0]); i++) {
    console.log('C is fun');
  }
}

main();
