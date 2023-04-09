#!/usr/bin/node
const arguments = process.argv.slice(2);

if (!arguments[0])
    console.log('Missing number of occurrences');
else
    for (let i = 0; i < parseInt(arguments[0]); i++)
        console.log('C is fun')
