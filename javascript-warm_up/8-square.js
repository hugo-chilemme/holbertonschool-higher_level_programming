#!/usr/bin/node
'use strict';

/**
 * Create script to display a square with a 'X'
 */
const args = process.argv.slice(2);
const SIZE = args[0];

if ( SIZE ) {
    
    // Creating a line with @SIZE 'X'
    const line = 'X'.repeat(SIZE);

    // Creating a line with so many Xs
    for ( let nline = 0 ; nline < SIZE ; nline++ )
        console.log(line);

}
else
{
    console.log('Missing size');
}
