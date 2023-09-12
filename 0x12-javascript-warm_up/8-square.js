#!/usr/bin/node
// print square
const args = parseInt(process.argv[2]);

if (isNaN(args)) {
  console.log('Missing size');
} else {
  let i = 0;
  while (i < args) {
    let j = 0;
    let row = '';
    while (j < args) {
      row += 'X';
      j++;
    }
    console.log(row);
    i++;
  }
}
