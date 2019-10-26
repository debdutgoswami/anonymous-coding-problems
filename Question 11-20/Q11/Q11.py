class Solution:
    def longest(self, l: list) -> int:
        m = 0
        for i in l:
            t = Solution().helper(l, i, 1)
            if t>m:
                m=t
        return m

    def helper(self, l, num, c):
        if num in l:
            count = 1 + Solution().helper(l,num+1,c+1)
            return count
        else:
            return 0

print(Solution().longest([100, 4, 200, 1, 3, 2]))