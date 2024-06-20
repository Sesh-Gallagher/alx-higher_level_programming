#!/usr/bin/node
/*
Write a function that returns the reversed version of a list:
Prototype: exports.esrever = function (list)
You are not allow to use the built-

*/

  const reversedList = [];

  for (let a = list.length - 1; a >= 0; --a) {
    reversedList.push(list[a]);
  }

  return reversedList;
};
