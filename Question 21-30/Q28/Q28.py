l = list(map(int, input().split()))
k = int(input())

# dividing the list with range of k
l = l[k:]+l[:k]

print(l)