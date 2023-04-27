const fs = require('fs');

const input = fs.readFileSync('dev/stdin').toString().trim().split('\n');

const N = parseInt(input.shift());
let counter = N;

for(let i = 0; i < N; i++) {
  const charMap = {};
  for(let j = 0; j < input[i].length; j++) {
    if(!charMap[input[i][j]]){
      charMap[input[i][j]] = true;
    } else if (input[i][j] !== input[i][j - 1]) {
      counter--;
      break;
    }
  }
}
console.log(counter);