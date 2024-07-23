#!/usr/bin/node

if (process.argv.length < 3) {
  console.log(0);
} else {
  const numbers = process.argv.slice(2).map(Number);
  if (numbers.length < 2) {
    console.log(0);
  } else {
  function secondbiggest (arr) {
    return arr.sort((a, b) => b - a);
  }
  const sorted = secondbiggest(numbers);
  if (sorted[1] < 0) {
    console.log(0);
  } else {
  console.log(sorted[1]);
  }
}
}
