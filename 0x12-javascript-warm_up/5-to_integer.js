#!/usr/bin/node
// number or not a number
const first = process.argv[2];
if (!isNaN(first)) {
  console.log('My number: ' + first);
} else {
  console.log('Not a number');
}
