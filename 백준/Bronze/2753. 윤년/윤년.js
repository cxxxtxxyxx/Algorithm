const fs = require('fs');

//let input = fs.readFileSync('input.txt').toString();
let input = fs.readFileSync('/dev/stdin').toString();

input = parseInt(input);

solution(input);


function solution(input) {
  if((input % 4 === 0 && input % 100 !== 0) || input % 400 === 0) {
    console.log(1);
  } else {
    console.log(0);
  }
}
