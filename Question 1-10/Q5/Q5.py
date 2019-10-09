N = int(input())
L = []
for i in range(N):
    a = int(input())
    L.append([int(x) for x in input().split()])

for i in range(N):
    l = L[i]
    m = []
    ma=0
    for j in range(1,len(l)):
        sub = l[0:j]
        count = 0
        for k in sub:
            if k%l[j]==0 and k>=l[j]:
                count += 1
        if count>ma:
            ma=count
    print(ma)
