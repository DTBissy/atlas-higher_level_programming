#!/usr/bin/node

const a = Number(process.argv[2]);
const b = Number(process.argv[3]);

if (process.argv.length < 3) {
  console.log('need Numbers');
} else {
  function add (a, b) {
    return a + b;
  }
  console.log(add(a, b));
}
