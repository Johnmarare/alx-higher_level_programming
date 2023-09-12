#!/usr/bin/node
// print square
const args = parseInt(process.argv[2]);

if (typeof args !== 'number') {
  console.log('Missing size');
} else {
  let i = 0;
  while (i < args) {
    let j = 0;
    let row = '';
    while (j < args) {
      row += 'x';
      j++;
    }
    console.log(row);
    i++;
  }
}
