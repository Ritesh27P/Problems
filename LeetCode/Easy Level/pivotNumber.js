const pivotIndex = (nums)=>{
    let S = 0;
    for(let n of nums){
        S += n;
    }
    let lsum = 0;
    for(let i=0; i<nums.length; i++){
        if(lsum == (S - lsum -nums[i])){
            return i;
        } else {
            lsum += nums[i]
        }
    }

    return -1
}

console.log(pivotIndex([1,7,3,6,5,6]));
