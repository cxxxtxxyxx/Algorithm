const fs = require('fs');

let input = parseInt(fs.readFileSync('/dev/stdin').toString());

solution(input);



function solution(input) {
  const result = input - 543;
  console.log(result);
}