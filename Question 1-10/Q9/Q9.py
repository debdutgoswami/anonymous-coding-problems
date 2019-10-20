def longest_consecutive(nums):
    m = 0
    for i in nums:
        k,c = 1, 1
        while True:
            if((i+k) in nums):
                c += 1
                k += 1
            else:
                break
        if(c>m):
            m = c
    return m

l = [int(i) for i in input().split()]
print(longest_consecutive(l))