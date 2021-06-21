a=int(input())
b=[300,60,10]
i,j,k=0,0,0
if a%10!=0:
    print(-1)
else:
    i=int(a/b[0])
    a-=b[0]*i
    j=int(a/b[1])
    a-=b[1]*j
    k=int(a/b[2])
print(i,j,k)