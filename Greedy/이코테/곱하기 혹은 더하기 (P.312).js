
/**/
// <하영>[x]
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
