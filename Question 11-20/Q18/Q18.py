matches = {
    0: 6, 1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8:7,9: 6
}

T = int(input())

for i in range(T):
    A, B = tuple(int(i) for i in input().split())

    S = str(A+B)

    total = 0
    for num in S:
        total+=matches[int(num)]

    print(total)