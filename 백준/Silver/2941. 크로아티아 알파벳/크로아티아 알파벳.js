const fs = require('fs');

let input = fs.readFileSync('dev/stdin').toString().trim();

const alphaList = [
  'c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z='
];

for(let alpha of alphaList) {
  input = input.split(alpha).join('s');
}
console.log(input.length);