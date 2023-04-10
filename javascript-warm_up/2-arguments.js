#!/usr/bin/node
'use strict';

/**
 * main
 * Create script to display if yes or not he have a argument or multiple
 */
function main () {
  const argsLen = process.argv.slice(2).length;

  if (argsLen === 0) {
    console.log('No argument');
  } else if (argsLen === 1) {
    console.log('Argument found');
  } else {
    console.log('Arguments found');
  }
}

main();
