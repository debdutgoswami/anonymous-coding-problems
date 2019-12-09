nums = list(map(int, input().split()))
k = int(input())

# creating a hash table to store the count of each unique element
d = dict()
for num in nums:
    d[num] = d.get(num,0) + 1

# sorted method is of complexity O(n log n)
# but here it is taking no. of unique elements which is less than n (total elements)
# so the complexity is obviously less than O(n log n)
d = sorted(d.items(), key=lambda kv: kv[1], reverse=True)

# storing the first k element keys in a list
l = [d[i][0] for i in range(k)]

print(l)