T = int(input())

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A = sorted(A)
    B = sorted(B)
    s = 0

    for i in range(N):
        if A[i]<B[i]:
            s+=A[i]
        else:
            s+=B[i]

    print(s)