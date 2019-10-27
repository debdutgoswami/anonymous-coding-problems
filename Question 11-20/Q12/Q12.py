class Solution:
    def findDisappearedNumbers(self, nums):
        missing = []
        n = len(nums)
        for i in range(1,n+1):
            if i not in nums:
                missing.append(i)
        return missing

nums = [4,6,2,6,7,2,1]
print(Solution().findDisappearedNumbers(nums))