#!/usr/bin/node
/*
function that executes x times a function.

The function must be visible from outside
Prototype: function (x, theFunction)
You are not allowed to use var
*/

exports.callMeMoby = function (x, theFunction) {
  for (let a = 0; a < x; a++) theFunction();
};
