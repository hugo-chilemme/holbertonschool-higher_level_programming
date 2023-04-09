#!/usr/bin/node
const arguments = process.argv.slice(2);

if (arguments[0])
    console.log(arguments[0])
else
    console.log("No argument")
