#!/usr/bin/node
/*
Write a script that imports a dictionary of occurrences by user id and computes  dictionary
*/

const dict = require('./101-data').dict;

const newDict = {};

Object.keys(dict).map(function (key) {
  if (!Array.isArray(newDict[dict[key]])) {
    newDict[dict[key]] = [];
  }
  newDict[dict[key]].push(key);
});

console.log(newDict);
