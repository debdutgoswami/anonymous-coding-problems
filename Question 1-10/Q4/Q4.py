N = int(input())
K, L = [], []
for i in range(N):
    a = tuple(int(x) for x in input().split())
    K.append(a[1])
    L.append([int(x) for x in input().split()])

for i in range(N):
    l = L[i]
    k = K[i]
    n = len(l)
    for j in range(k):
        l[j%n] = l[j%n] ^ l[n-(j%n)-1]
    
    [print(x, end=" ") for x in l]
    print()