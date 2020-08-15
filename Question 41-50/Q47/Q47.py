class Solution:
    def __init__(self, N, arr):
        self.N = N
        self.arr = arr

    def getLocalMaximaMinima(self):
        """for finding all the local maxima and minima"""
        maxima, minima = list(), list()
        for i in range(self.N):
            if i-1<0:
                if self.arr[i]>self.arr[i+1]:
                    maxima.append(self.arr[i])
                elif self.arr[i]<self.arr[i+1]:
                    minima.append(self.arr[i])
            elif i+1==N:
                if self.arr[i]>self.arr[i-1]:
                    maxima.append(self.arr[i])
                elif self.arr[i]<self.arr[i-1]:
                    minima.append(self.arr[i])
            else:
                if self.arr[i]>self.arr[i-1] and self.arr[i]>self.arr[i+1]:
                    maxima.append(self.arr[i])
                elif self.arr[i]<self.arr[i-1] and self.arr[i]<self.arr[i+1]:
                    minima.append(self.arr[i])
        return maxima, minima

    def result(self):
        maxima, minima = self.getLocalMaximaMinima()
        profit = 0
        for maxi, mini in zip(maxima, minima):
            profit += maxi - mini
        return profit

if __name__ == "__main__":
    N = int(input())
    arr = list(map(int, input().split()))
    sol = Solution(N, arr)
    print(sol.result())