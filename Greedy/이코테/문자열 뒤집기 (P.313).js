/**/
// <하영> [o]
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
