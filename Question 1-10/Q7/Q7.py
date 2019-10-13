
def findSingle(nums):
    res = 0
    for i in nums:
        res = res ^ i
    return res

print(findSingle([7, 3, 5, 5, 4, 3, 4, 8, 8]))