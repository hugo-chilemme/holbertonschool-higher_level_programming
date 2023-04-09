#!/usr/bin/node
'use strict';

/**
 * Create function to addition @arg1 and @arg2
 */
const args = process.argv.slice(2);
const number1 = parseInt(args[0]);
const number2 = parseInt(args[1]);

console.log(number1 + number2);
