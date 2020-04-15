T = int(input())

for _ in range(T):
    N = int(input())
    l = list(map(int, input().split()))

    modulo = 1000000007

    profit = 0

    l = sorted(l,reverse=True)

    for i in range(len(l)):
        if  l[i]-i>0:
            profit += l[i]-i

    print(profit%modulo)