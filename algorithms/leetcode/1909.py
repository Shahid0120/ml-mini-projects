def canBeIncreasing(nums):
    for idx in range(len(nums)):
        if  nums[idx - 1] >= nums[idx] and idx != 0 :
            if idx - 2 < 0:
                lowest_index = 0
                if nums[lowest_index] >= nums[idx]:
                    return False
            elif nums[idx - 2] >= nums[idx]:
                    return False
    return True

nums = [1,2,10,5,7]
idx = 0
p = nums[-2]
print(p)
p = canBeIncreasing(nums)
print(p)