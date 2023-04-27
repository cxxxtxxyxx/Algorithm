const fs = require('fs');

const input = Number(fs.readFileSync('dev/stdin').toString());

let count = 0;


let firstRange = 1;
let lastRange = 1;
let increase = 6;
let i = 1;


calc(input);

function calc(input) {
  while(1) {
    if(firstRange <= input && input <= lastRange) {
      count++;
      console.log(count);
      return;
    } else {
      count++;
    }
    firstRange = lastRange + 1;
    lastRange += increase * i;
    i++;
  }
}