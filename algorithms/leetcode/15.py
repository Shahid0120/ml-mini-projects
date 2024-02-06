def threeSum(nums):
    original_left, original_right = 0, len(nums) - 1
    sumArr = []
    if len(nums) < 3:
        return sumArr
    
    while original_left < original_right:
        r = original_right
        l = original_left
        m = l + 1
        while m < r: 
            if nums[l] + nums[r] + nums[m] == 0:
                if [nums[l],nums[r],nums[l + 1]]not in sumArr:
                    sumArr.append([nums[l],nums[r],nums[m]])
            m += 1
        original_right -= 1


    while original_left < original_right:
        r = original_right
        l = original_left
        m = r - 1
        while m < r: 
            if nums[l] + nums[r] + nums[m] == 0:
                if [nums[l],nums[r],nums[l + 1]] not in sumArr:
                    sumArr.append([nums[l],nums[r],nums[l + 1]])
            m -= 1
        original_left += 1
    return sumArr 

nums = [-1,0,1,2,-1,-4]
p = threeSum(nums)
print(p)