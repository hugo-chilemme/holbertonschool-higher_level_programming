#!/usr/bin/node
'use strict';

/**
 * Create function to addition @arg1 and @arg2
 */
const args = process.argv.slice(2);
const number_1 = parseInt(args[0]);
const number_2 = parseInt(args[1]);

console.log(number_1 + number_2)
