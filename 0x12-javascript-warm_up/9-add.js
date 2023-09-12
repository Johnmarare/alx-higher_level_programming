#!/usr/bin/node
// prints addition of 2 integers
function add (a, b) {
  console.log(a + b);
}
const arg1 = parseInt(process.argv[2]);
const arg2 = parseInt(process.argv[3]);

if (process.argv.length === 4) {
  if (!isNaN(arg1) && !isNaN(arg2)) {
    add(arg1, arg2);
  }
}
