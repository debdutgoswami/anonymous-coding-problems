n = int(input())
l=[]
for i in range(n):
    l.append(input())
i=1
stack = []
stack.append(l[0])
while len(l)>i:
    if stack[len(stack)-1]==l[i]:
        stack.pop(len(stack)-1)
    else:
        stack.append(l[i])
    i+=1
print(len(stack))