/**/
//<하영>[o] : 하드코딩이 아닌 test case에 따른 입력값을 받아 적용할수있게 해봐야겠다
coins = [1,2,3,5,16]

const coinArr = coins.sort((a,b) => {
  return a-b;
})

let count = 1;

for(let i=0; i < coinArr.length; i++){
  if(count < coinArr[i]){
    break
  }else{
    count += coinArr[i]
  }
}

console.log(count) // 12출력
/**/
