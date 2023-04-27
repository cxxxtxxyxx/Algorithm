const fs = require('fs');

const input = parseInt(fs.readFileSync('dev/stdin').toString());

solution(input);

function solution (input) {

  if(input < 100) {
    console.log(input);
    return;
  }
  else {
    let count = 0;
    let flag = 0;
    for(let i = 100; i <= input; i++) {
      let d = parseInt(String(i)[0]) - parseInt(String(i)[1]);
      for(let j = 0; j < String(i).length - 1; j++) {
        if(parseInt(String(i)[j]) - parseInt(String(i)[j + 1]) !== d) {
          flag = 1;
          break;
        }
      }
      if(flag === 0) {
        count++;
      }
      flag = 0;
    }
    console.log(count + 99);
  }
  

  
}