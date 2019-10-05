N = int(input())
L = []
for i in range(N):
    a = int(input())
    L.append([int(x) for x in input().split()])

for i in L:
    count = 1
    l = i
    for j in range(1,len(l)):
        if(j-5<0):
            index = 0
        else:
            index = j-5
        sub = l[index:j]
        if l[j]<min(sub):
            count += 1

    print(count)