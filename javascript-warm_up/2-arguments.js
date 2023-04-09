#!/usr/bin/node
'use strict';

/**
 * Show if there are one or more or no arguments
 */
const args = process.argv.slice(2);
const argsLen = args.length;

if (argsLen === 0) {
  console.log('No argument');
} else if (argsLen === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
