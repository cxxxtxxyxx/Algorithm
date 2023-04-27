const fs = require('fs');

let input = fs.readFileSync('dev/stdin').toString().split(' ');

solution(input);

function solution(input) {
  if(+input[0] > +input[1]) {
    console.log('>');
  } else if (+input[0] < +input[1]) {
    console.log('<'); 
  } else {
    console.log('==');
  }
}