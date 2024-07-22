#!/usr/bin/node

if (process.argv.length < 2) {
  console.log("Please provide an argument.");
} else {
  const arg = Number(process.argv[2]);
  if (isNaN(arg)) {
    console.log("Not a number");
  } else {
    console.log(`My number: ${arg}`);
  }
}
