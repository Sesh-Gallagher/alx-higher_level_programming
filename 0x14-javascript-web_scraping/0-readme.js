#!/usr/bin/node
// Script that reads and prints the content of/from a file
const fs = require('fs');
fs.readFile(process.argv[2], 'utf-8',
  function (err, data) {
    if (err) {
      console.log(err);
      return;
    }
    console.log(data);
  });
