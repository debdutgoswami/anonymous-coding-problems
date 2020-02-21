def leftRotation(arr, n, d):
    d = d%n
    arr = arr[d:]+arr[:d]
    return arr

if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    for element in leftRotation(a, n, d):
        print(element, end=" ")
