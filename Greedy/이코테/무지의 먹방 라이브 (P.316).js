/**/
//<하영> [x]: 어렵다 while(true)무한루프로 사용해서 리턴하면 될것같으면서도 ... 어떻게 접근할지 어려움
function solution(food_times, k) {
    let count=0;
    let queue=food_times.map((a,b)=>[a,b]).sort((a,b)=>a[0]-b[0]);
    const total = food_times.reduce((a,b)=>{return a+b},0);
    if(total<=k) return -1;
    
    let idx=0;
/**/
