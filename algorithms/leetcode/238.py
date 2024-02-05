def productExceptSelf(nums):
    res = {}
    freq = [0] * len(nums)
    for n in nums:
        res[n] = 1 + res.get(n, 0)

    idx = 0
    while idx < len(nums) - 1:
        key = list(res.keys())[0]
        value = list(res.values())[0]
        res.pop(key)
        sum_one *= [key * value for key, value in res.items()]        
        print(sum_one)
        freq[idx] = sum_one
        sum_one = 0
        idx += 1
        res[key] = value
    return freq
nums = [1,2,3,4]
product = productExceptSelf(nums)
print(product)