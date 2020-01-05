import sys

#input
n: int = int(input('N = '))
mat: list = []
for _ in range(n):
    row = list(map(int, input().split()))
    # for sanity checking
    if len(row) != n:
        print("diagonal is only possible for square matrix")
        sys.exit(0)

    # inserting each row in the 2-D list or matrix
    mat.append(row)

# left is for left diagonal and right is for right diagonal
left, right = 0, n-1

# storing the squares of the diagonal elements
sq_left, sq_right = [], []

# a single for loop, hence, time complexity is O(n)
for i in range(n):
    sq_left.append(mat[i][left]**2)
    left += 1
    sq_right.append(mat[i][right]**2)
    right -= 1

# output
print(sq_left)
print(sq_right)