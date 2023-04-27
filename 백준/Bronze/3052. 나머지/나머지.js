const fs = require('fs');

const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n').map(x => x % 42);

solution(input);

function solution(input) {
  let unique = [];

  input.forEach(element => {
    if(!unique.includes(element)) {
      unique.push(element);
    }
  });

  console.log(unique.length);
}