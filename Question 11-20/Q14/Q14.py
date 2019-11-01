N = int(input())

l = []

# input
for i in range(N):
    n = int(input())
    x= []
    for j in range(n):
        x.append(input())
    l.append(x)

for i in l:
    c = 0

    # logic
    for j in range(10):
        su = 0
        for k in range(len(i)):
            su += int(i[k][j])
        if(su%2 != 0 and su!=0):
            c+=1

    print(c) # result