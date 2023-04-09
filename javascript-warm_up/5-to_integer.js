#!/usr/bin/node
const arguments = process.argv.slice(2);

if (isNaN(parseInt(arguments[0])))
    console.log('Not a number')
else
    console.log(parseInt(arguments[0]))
