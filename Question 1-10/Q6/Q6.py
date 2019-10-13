l=[int(i) for i in input("enter the list: ").split()]
c=0

while(len(l)!=0):
    m=max(l)
    i=l.index(m)
    l=l[i+1:]
    c+=1
print(c)