#!/usr/bin/node

if (process.argv.length < 3) {
  console.log(0);
} else {
  const numbers = process.argv.slice(2).map(Number);
  function secondbiggest (arr) {
    return arr.sort((a, b) => b - a);
  }
  const sorted = secondbiggest(numbers);
  console.log(sorted[1]);
}
