const fs = require('fs');

const input = fs.readFileSync('dev/stdin').toString().trim().toUpperCase();

solution(input);

function solution(input) {
  let result = new Array(26);
  let max;
  let index;
  result = result.fill(0);
  const upperASCII = 'A'.charCodeAt(0);

  for(let i = 0; i < input.length; i++) {
    result[input[i].charCodeAt(0) - upperASCII]++;
  }
  max = Math.max.apply(null, result);
  
  if(result.indexOf(max) === result.lastIndexOf(max)) {
    console.log(String.fromCharCode(result.indexOf(max) + upperASCII));
  } else {
    console.log("?");
  }
}