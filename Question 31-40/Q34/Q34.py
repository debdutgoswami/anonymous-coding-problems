#!/bin/python3

import math

def solve(h: int, wallPoints: list, lengths: list):
    m = 0
    for p, l in zip(wallPoints, lengths):
        per = 0.25*l
        new_p = math.ceil(p-per)
        height = new_p-h
        if height>0 and height>m:
            m=height
    return m

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    h = int(first_multiple_input[1])

    wallPoints = list(map(int, input().rstrip().split()))

    lengths = list(map(int, input().rstrip().split()))

    answer = solve(h, wallPoints, lengths)

    print(answer)
