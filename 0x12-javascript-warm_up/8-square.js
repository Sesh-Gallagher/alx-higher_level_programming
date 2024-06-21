#!/usr/bin/node
/*
script that prints a square

The first argument is the size of the square
If the first argument can’t be converted to an integer, print “Missing size”
You must use the character X to print the square
You must use console.log(...) to print all output
You are not allowed to use var
You must use a loop (while, for, etc.)
*/

const x = process.argv[2];

if (!parseInt(x)) {
  console.log('Missing size');
} else {
  for (let a = 0; a < x; a++) {
    let b = 0;
    let myVar = '';

    while (b < x) {
      myVar = myVar + 'X';
      b++;
    }
    console.log(myVar);
  }
}
