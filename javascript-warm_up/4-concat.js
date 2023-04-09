#!/usr/bin/node
'use strict';

/**
 * Display @firstArg is @secondArg in a console
 */
const args = process.argv.slice(2);
console.log(args[0] + ' is ' + args[1]);
