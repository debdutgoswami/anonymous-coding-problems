import numpy as np

n = int(input())

arr = [[0]*n]*n
arr = np.array(arr)
i,j,k=0,0,1

while(k<=n**2):
    while(j<n and arr[i][j]==0):
        arr[i][j] = k
        j += 1
        k += 1
    j -= 1
    i += 1
    while(i<n and arr[i][j]==0):
        arr[i][j] = k
        i += 1
        k += 1
    i -= 1
    j -= 1
    while(j>=0 and arr[i][j]==0):
        arr[i][j] = k
        j -= 1
        k += 1
    j += 1
    i -= 1
    while(i>=0 and arr[i][j]==0):
        arr[i][j] = k
        i -= 1
        k += 1
    i += 1
    j += 1

print(arr)