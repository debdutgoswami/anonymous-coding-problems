T = int(input())

for i in range(T):
    N, M, Q = tuple([int(x) for x in input().split()])
    m = [int(x) for x in input().split()]
    q = [int(x) for x in input().split()]
    s = 0

    for j in q:
        c = 0
        for k in m:
            if(k%j==0):
                c += 1

        s += N//j - c

    print("case #{}: {}".format(i+1,s))
