/**/
//<하영> [o] : 좀더 효율적으로 할수있는 방법이.. 있을텐데.... 분명히..있을텐데....ㅜㅜ
const n = [1,2,3,4,0,2]
const arr = []
const length = n.length;

const division = (n,a) => {
  
const divide = Math.floor(length/(length / 2-1)) 

for(let i = 0; i<divide; i++){
  arr.push(n.splice(0,length / (length / 2-1)))
}return arr; 
}
const result = division(n,(length / (length / 2-1)));

const left = arr[0].reduce((a,b)=>{return a+b},0);
const right = arr[1].reduce((a,b)=>{return a+b},0);

if(left === right){
  console.log("LUCKY")
}else{
  console.log("READY")
}

/**/
