T = int(input())

for i in range(T):
    N = int(input())
    P = [int(x) for x in input().split()]
    h = 0
    print("Case #{}: ".format(i+1), end="")
    for j in range(len(P)):
        l = P[:j+1]
        c=0
        for k in l:
            if k>h:
                c+=1
        if c>h:
            h+=1
        print(h,end=" ")
    print()
