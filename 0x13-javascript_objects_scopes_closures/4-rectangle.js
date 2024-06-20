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

module.exports = class Rectangle {
  constructor (width, height) {
    if (typeof width === 'number' && typeof height === 'number' && width > 0 && height > 0) {
      this.width = width;
      this.height = height;
    }
  }

  print (char = 'X') {
    for (let a = 0; a < this.height; ++a) {
      let b = 0;

      for (; b < this.width; ++b) {
        process.stdout.write(char);
      }

      if (b === this.width) {
        console.log('');
      }
    }
  }

  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
