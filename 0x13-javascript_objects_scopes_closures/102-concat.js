#!/usr/bin/node
/*
Write a script that concats 2 files.

The first argument is the file path of the first source file
The second argument is the file path of the second source file
The third argument is the file path of the destination
*/

const fs = require('fs');
let content = '';

content = content.concat(fs.readFileSync(process.argv[2]));
content = content.concat(fs.readFileSync(process.argv[3]));
fs.writeFileSync(process.argv[4], content);
