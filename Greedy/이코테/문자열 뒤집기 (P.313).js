/**/
// <하영> [o] : count로 조건넣어주는 로직보다 더 좋은 방법이 있을듯한데 모르겠다 힝 ㅠ
const result = s =>{
  let count = 0;
  for(let i = 1; i < s.length; i++) {
    if(s[i-1] !== s[i]){
      count += 1;
    }
  }
  if(count % 2 === 0){
    return (count / 2)
  }else if(count % 2 !== 0){
    return Math.ceil(count / 2)
  }
}
console.log(result("1010101010111")) // 5출력
/**/
