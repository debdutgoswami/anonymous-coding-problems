l = [int(i) for i in input().split()]

sort_l = sorted(l)

for i in range(len(l)):
    if l[i]!=sort_l[i]:
        print(i,end=" ")
        break

for i in range(len(l)-1,0,-1):
    if l[i]!=sort_l[i]:
        print(i)
        break