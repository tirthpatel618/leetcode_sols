function productExceptSelf(nums: number[]): number[] {
    let res: number[] = new Array(nums.length).fill(1);
    let prefix: number = 1;
    for (let i = 0; i < nums.length; i++) {
        res[i] *= prefix;
        prefix *= nums[i];
    }
    let postfix: number = 1
    for (let i = nums.length -1; i > -1; i--) {
        res[i] *= postfix;
        postfix *= nums[i]

    }

    return res

    
 }

let nums: number[] = [1, 2, 3, 4, 5]
let result: number[] = productExceptSelf(nums)
console.log(result)

const fruits = ["Banana", "Orange", "Apple"];
fruits.push("Lemon");
console.log(fruits);