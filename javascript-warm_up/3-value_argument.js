#!/usr/bin/node
'use strict';

/**
 * Show first argument if available
 */
const args = process.argv.slice(2);

if (args[0]) {
  console.log(args[0]);
} else {
  console.log('No argument');
}
