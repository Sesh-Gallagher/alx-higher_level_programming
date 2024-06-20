#!/usr/bin/node
/*
Write a class Square that defines a square and inherits from Square of 5-square.js:

You must use the class notation for defining your class and extends
Create an instance method called charPrint(c) that prints the rectangle using thecharacter c
If c is undefined, use the character X

*/

const PrevSquare =  require('./5-square');

class Square extends PrevSquare {
	charPrint (c) {
		const myChar =  c === undefined ? 'X' : c;
		for (let a = 0; a < this.height; a++) {
			let myVar = '';
			let b = 0;
			while (b < this.width) {
				myVar += myChar;
				b++;
			}

			console.log(myVar);
		}
	}
}

module.exports = Square;
