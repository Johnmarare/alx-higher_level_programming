#!/usr/bin/node
// C is fun
const args = process.argv[2];

if (isNaN(args)) {
  console.log('Missing number of occurrences');
} else {
  let i = 1;
  while (i <= args) {
    console.log('C is fun');
    i++;
  }
}
