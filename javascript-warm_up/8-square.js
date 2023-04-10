#!/usr/bin/node
'use strict';

/**
 * main
 * Create a script to display square with @SIZE
 */
function main () {
  const SIZE = parseInt(process.argv[2]);

  if (SIZE && !isNaN(SIZE)) {
    const line = 'X'.repeat(SIZE);

    for (let nline = 0; nline < SIZE; nline++) {
      console.log(line);
    }
    return;
  }

  console.log('Missing size');
}

main();
