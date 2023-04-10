#!/usr/bin/node
'use strict';

/**
 * main
 * Create script to display multiples lines by a array
 */
function main () {
  const lines = [
    'C is fun',
    'Python is cool',
    'JavaScript is amazing'
  ];

  console.log(lines.join('\n'));
}

main();
