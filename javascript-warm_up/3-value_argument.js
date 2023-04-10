#!/usr/bin/node
'use strict';

/**
 * main
 * Create a script to display first argument if available
 */
function main () {
  const args = process.argv.slice(2);

  if (args[0]) {
    console.log(args[0]);
  } else {
    console.log('No argument');
  }
}

main();
