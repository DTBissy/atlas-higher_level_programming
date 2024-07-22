#!/usr/bin/node

const array = ['C is fun', 'Python is cool', 'JavaScript is amazing'];

let string = '';
for (let i = 0; i < array.length; i++) {
  string += array[i] + '\n';
}

console.log(string.trim());
