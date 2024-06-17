#!/usr/bin/node
const counter = process.argv[2];
if (counter === undefined) {
  console.log('Missing number of occurrences');
}
for (let i = 0; i < counter; i++) {
  console.log('C is fun');
}
