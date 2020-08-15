class Solution:
    def __init__(self, N, arr):
        self.N = N
        self.arr = arr

    def getLeftMax(self):
        _max = 0
        maxList = []
        for ele in self.arr:
            if ele>_max:
                _max = ele
            maxList.append(_max)
        return maxList

    def getRightMax(self):
        _max = 0
        maxList = []
        for index in range(self.N-1, -1, -1):
            if self.arr[index]>_max:
                _max = self.arr[index]
            maxList.append(_max)
        return maxList

    def result(self):
        leftMax = self.getLeftMax()
        rightMax = self.getRightMax()
        s = 0
        for index in range(1, self.N-1):
            intermidiate_sum = min(leftMax[index], rightMax[index]) - self.arr[index]
            if intermidiate_sum > 0:
                s += intermidiate_sum
        return s

if __name__ == "__main__":
    N = int(input())
    arr = list(map(int, input().split()))
    sol = Solution(N, arr)
    print(sol.result())