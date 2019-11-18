T = int(input())
answer = []
for i in range(T):
    N, K = tuple(int(x) for x in input().split())
    init = 0
    calories = [int(x) for x in input().split()]
    flag = None
    for j in range(N):
        A = calories[j]
        summ = A+init
        if(summ>=K):
            init = summ-K
        else:
            flag = j+1
            break
    if(flag):
        answer.append("NO {}".format(flag))
    else:
        answer.append("YES")

[print(i) for i in answer]
