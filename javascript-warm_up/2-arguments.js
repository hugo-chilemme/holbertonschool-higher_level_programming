#!/usr/bin/node
const arguments = process.argv.slice(2);

if (arguments.length === 0)
    console.log('No argument')
else if (arguments.length === 1)
    console.log('Argument found')
else
    console.log('Arguments found')
