#!/usr/bin/node

class Rectangle {
	constructor (w, h) {
		this.width = w;
		this.height = h;
	}
}
print () {
	for  (let a = 0; a < this.height; i++) {
		let pattern = '';
		for (let b = 0; b < this.width; b++) {
			pattern += 'x';
		}
		console.log(pattern);
	}
}
}

module.exports =  Rectangle;
