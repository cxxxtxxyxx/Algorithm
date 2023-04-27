const fs = require('fs');

const input = fs.readFileSync('dev/stdin').toString().trim();
let result = 0;
for(let i = 0; i < input.length; i++) {
  if('A' <= input[i] && input[i] <= 'C') {
    result += 3;
  } else if('D' <= input[i] && input[i] <= 'F') {
    result += 4;
  } else if('G' <= input[i] && input[i] <= 'I') {
    result += 5;
  } else if('J' <= input[i] && input[i] <= 'L') {
    result += 6;
  } else if('M' <= input[i] && input[i] <= 'O') {
    result += 7;
  } else if('P' <= input[i] && input[i] <= 'S') {
    result += 8;
  } else if('T' <= input[i] && input[i] <= 'V') {
    result += 9;
  }  else {
    result += 10;
  }
}
console.log(result);