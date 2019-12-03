import numpy as np

def median_window(l: list, k: int):
    for i in range(len(l)-k+1):
        arr = np.array(l[i:i+k])
        print("{} <- median of {}".format(np.median(arr), list(arr)))

median_window([-1,5,13,8,2,3,3,1], 3)