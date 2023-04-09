#!/usr/bin/node
'use strict';
const args = process.argv.slice(2);

if (isNaN(parseInt(args[0]))) { console.log('Not a number'); } else { console.log(parseInt(args[0])); }
