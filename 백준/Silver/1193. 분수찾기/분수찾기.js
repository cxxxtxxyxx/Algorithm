const fs = require('fs');

const input = Number(fs.readFileSync('dev/stdin').toString().trim());

/*
1: 1/1
2: 1/2
3: 2/1
4: 3/1
5: 2/2
6: 1/3
7: 1/4
8: 2/3
9: 3/2
10: 4/1
11: 5/1
12: 4/2
13: 3/3
14: 2/4
15: 1/5
16: 1/6
17:

first Range : 1
last Range : 1
interval : 1;

i = 2;

lastRange += i;
firstRange = lastRange - interval;
interval++;

1~1 1/1 0
2~3 1/2 2/1 1
4~6 3/1 2/2 1/3 2
7~10 1/4 2/3 3/2 4/1 3
11~15 5/1 4/2 3/3 2/4 1/5 4

interval 값이 짝수면 1/? 홀수면 ?/1로 시작
interval 값 + 1 총 수

*/

solution(input);

function solution(input) {
  let firstRange = 1;
  let lastRange = 1;
  let interval = 1;
  let i = 2;
  let first;
  let last;
  while(1) {
    if(firstRange <= input && input<= lastRange) {
      break;
    } else {
      lastRange += i;
      firstRange = lastRange - interval;
      interval++;
      i++;
    }
  }
  if((lastRange - firstRange) % 2 == 1) {
    first = 1;
    last = interval;
    let a = input - firstRange;
    for(let i = 0; i < a; i++) {
      first++;
      last--;
    }
    console.log(`${first}/${last}`);
  } else {
    first = interval;
    last = 1;
    let a = input - firstRange;
    for(let i = 0; i < a; i++) {
      first--;
      last++;
    }
    console.log(`${first}/${last}`);
  }
}