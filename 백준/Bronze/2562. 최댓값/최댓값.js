const fs = require('fs');

const input = fs.readFileSync('/dev/stdin').toString().split('\n').map(x => +x);

solution(input);

function solution(input) {
  const max = Math.max(...input);
  const index = input.findIndex(num => num === max ? true : false);
  console.log(max);
  console.log(index + 1);
}

