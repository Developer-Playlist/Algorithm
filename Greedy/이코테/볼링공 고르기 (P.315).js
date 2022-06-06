/**/
//<하영> [o] : 아직도 입력값 받는 함수를 구현하지 못함..
let N = 8;
let M = 5;

let weight = [1,5,4,3,2,4,5,2]

let count = 0;

for(let i=0; i < weight.length; i++){
  for(let j=i+1; j < weight.length; j++){
    if(weight[i] !== weight[j]){
			count++
    }
  }
} console.log(count) //8 출력
/**/
