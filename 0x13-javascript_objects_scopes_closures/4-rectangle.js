#!/usr/bin/node

/*
 Write a class Rectangle that defines a rectangle:

You must use the class notation for defining your class
The constructor must take 2 arguments: w and h
Initialize the instance attribute width with the value of w
Initialize the instance attribute height with the value of h
If w or h is equal to 0 or not a positive integer, create an empty object
Create an instance method called print() that prints the rectangle using the character X
Create an instance method called rotate() that exchanges the width and the heightof the rectangle
Create an instance method called double() that multiples the width and the heightof the rectangle by 2

*/
class Rectangle {
	constructor(w, h) {
	if (typeof w === 'number' && w > 0 && typeof h === 'number' && h > 0) {
		this.width = w;
		this.height = h;
	}
}

print () {
	for (let a = 0; a < this.height; a++) {
		let myVar = '';
		let b = 0;
		while (b < this.width) {
			myVar += 'X';
			b++;
		}

		console.log(myVar);
	}
}
rotate () {
	let temp = 0;
	temp = this.width;
	this.width = this.height;
	this.height = temp;
}

double () {
	this.width *= 2;
	this.height *= 2;
}
}

module.exports = Rectangle;