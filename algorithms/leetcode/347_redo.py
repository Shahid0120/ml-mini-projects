def topKfrequency(nums, k):
    count = {}
    freq = [[] for i in range(len(nums))]
    # put it into the hashmap 
    for n in nums:
        count[n] = 1 + count.get(n, 0)
    # array of count values from hashmap 
    for n,c in count.items():
        freq[c].append(n)
    # from the last index go and remove until len(arr) == k
    res = [] 
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res

nums = [1,1,1,1,2,2,2,3,3,3]
k = 2
p = topKfrequency(nums, k)
print(p)