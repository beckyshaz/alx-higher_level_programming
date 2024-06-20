#!/usr/bin/node
/* class rectangle that defines a rectangle */
class Rectangle {
  constructor (w, h) {
    this.width = w;
    this.height = h;
    if (this.width <= 0 || this.height <= 0) {
      this.width = {};
      this.height = {};
    }
  }
}

module.exports = Rectangle;
