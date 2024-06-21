#!/usr/bin/node
/*
script that prints two arguments passed to it, in the following format: “ is ”

You must use console.log(...) to print all output
You are not allowed to use var
*/

const argv0 = process.argv[2];
const argv1 = process.argv[3];

console.log(`${argv0} is ${argv1}`);
