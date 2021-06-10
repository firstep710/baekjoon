from itertools import permutations
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(permutations(b,3))
for i in range(len(c)):
    c[i]=sum(c[i])
    if c[i]>a[1]:
        c[i]=0
print(max(c))

###################################################
n,m=list(map(int, input().split()))
data=list(map(int, input().split()))

result=0
length=len(data)

count=0
for i in range(length):
    for j in range(i+1,length):
        for k in range(j+1,length):
            sum_value=data[i]+data[j]+data[k]
            if sum_value<=m:
                result=max(result,sum_value)
print(result)