def twoSum(numbers, target):
    l,r = 0, len(numbers) - 1
    while l < r:
        curSum = numbers[l] + numbers[r]
        if curSum < target:
            l += 1
        elif curSum > target:
            r -= 1
        else:
            return [l + 1, r + 1]

numbers = [5,25,75]
target = 100
p = twoSum(numbers, target)
print(p)
