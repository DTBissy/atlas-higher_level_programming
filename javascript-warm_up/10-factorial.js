#!/usr/bin/node

if (process.argv.length < 3) {
  console.log(1);
} else {
  const fact = parseInt(process.argv[2]);

  function factorial (n) {
    if (n === 0 || isNaN(n)) {
      return 1;
    } else {
      return n * factorial(n - 1);
    }
  }
  console.log(factorial(fact));
}
