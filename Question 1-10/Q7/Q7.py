
def findSingle(nums):
    """this function finds the element which is not repeated twice
    
    Arguments:
        nums {list} -- list of integers obtained as input
    
    Returns:
        int -- the element
    """
    res = 0
    for i in nums:
        res = res ^ i
    return res

print(findSingle([7, 3, 5, 5, 4, 3, 4, 8, 8]))