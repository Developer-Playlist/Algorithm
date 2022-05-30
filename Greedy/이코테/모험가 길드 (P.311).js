/**/
// 1. <하영>[o]
const nums = [2,3,1,2,2]

const arr = nums.sort(function (a,b){
  return a - b;
})
console.log(nums) // [1,2,2,2,3]

let group = 0; 
let people = 0; 

for(let b of arr){
  people += 1; // 배열 각 요소에 접근하여 그룹안에 사람 추가
	if(people >= b){ // 현재 그룹에 포함된 사람수가 공포도보다 이상이라면
    group += 1; // 그룹 생성
    people = 0; // 그룹 안 사람 수 초기화 시키기
  }
}

console.log(group) // 2
/**/

/**/
// 2. <하영>[x]
const mOrP = s => {
  const numArr = s.split("").map(x => +x);
  let result = numArr[0];
  
  for (let i = 1; i < numArr.length; i++) {
    if (result <= 1) {
      result += numArr[i];
    } else if(numArr[i] <= 1) {
      result += numArr[i];
    } else {
      result *= numArr[i];
    }
  }
  
  return result;
};
