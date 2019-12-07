'''
The no. of such pairs is only possible if and only if we have more than one same no. of elements,
i.e. Ai + Aj = Ai * Aj is only possible when Ai = Aj
'''

T = int(input())

for i in range(T):
    N = int(input())
    l = list(map(int, input().split()))
    s = 0

    # used hasshing technique to count the occurence of each element
    d = dict() 
    for index in range(N): 
        if l[index] in d.keys(): 
            d[l[index]] += 1
        else: 
            d[l[index]] = 0
    
    # calculating the sum of the counts using n*(n+1)/2
    for value in d.values():
        s += value*(value+1)//2

    print(s)