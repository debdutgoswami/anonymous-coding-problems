T = int(input())

def maintain(QUEUE: list, N: int) -> str:
    for i in range(0,N):
        c = 0
        if QUEUE[i]:
            c += 1
        try:
            if QUEUE[i+1]:
                c += 1
        except IndexError:
            pass
        try:
            if QUEUE[i+2]:
                c += 1
        except IndexError:
            pass
        try:
            if QUEUE[i+3]:
                c += 1
        except IndexError:
            pass
        try:
            if QUEUE[i+4]:
                c += 1
        except IndexError:
            pass
        try:
            if QUEUE[i+5]:
                c += 1
        except IndexError:
            pass

        if c>1:
            return "NO"
    return "YES"

for _ in range(T):
    N = int(input())
    QUEUE = list(map(int, input().split()))

    print(maintain(QUEUE, N))