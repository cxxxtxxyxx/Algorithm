const fs = require('fs');

// let num = fs.readFileSync('input.txt').toString();
let num = fs.readFileSync('/dev/stdin').toString();

num = Number(num);

console.log(solution(num));

function solution(num) {
  let count = 0;
  let resultNum = num;
  while(true) {
    resultNum = newNum(resultNum);
    count++;
    if(resultNum === num){
      break;
    }
  }
  return count;
}

function newNum(num) {
  let left = parseInt(num / 10);
  let right = num % 10;
  let newnum = left + right;
  return right * 10 + newnum % 10;
}