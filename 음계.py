a=list(map(int,input().split()))
b=[1,2,3,4,5,6,7,8]
if a==b:
    print('ascending')
elif a==b[::-1]:
    print('descending')
else:
    print('mixed')

#########################################
a=list(map(int,input().split()))

asc=True
desc=True

for i in range(1,len(a)):
    if a[i]>a[i-1]:
        desc=False
    elif a[i]<a[i-1]:
        asc=False
if asc:
    print('ascending')
elif desc:
    print('descending')
else:
    print('mixed')