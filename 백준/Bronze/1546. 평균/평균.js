const fs = require('fs');

const input = fs.readFileSync('/dev/stdin')
                .toString()
                .split('\n');

const testCase = {
  size: input[0],
  array: input[1].split(' ').map(x => +x),
}

solution(testCase);


function solution(testCase) {
  const max = Math.max(...testCase.array);
  let total = 0;
  testCase.array.forEach(element => {
    element = element/max * 100;
    total += element;
  });
  const newAvg = total / testCase.size;
  console.log(parseFloat(newAvg));
}