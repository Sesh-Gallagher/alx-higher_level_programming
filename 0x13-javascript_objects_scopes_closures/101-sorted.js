#!/usr/bin/node
/*
Write a script that imports a dictionary of occurrences by user id and computes  dictionary
*/

const dict = require('./101-data').dict;

const newDict = {};

Object.getOwnPropertyNames(dict).forEach(occurences => {
  if (newDict[dict[occurences]] === undefined) {
    newDict[dict[occurences]] = [occurences];
  } else {
    newDict[dict[occurences]].push(occurences);
  }
});
console.log(newDict);
