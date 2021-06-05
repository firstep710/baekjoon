w,b=0,0
def cut(x,y,n):
    global w,b
    color=p[x][y]
    check=True

    for i in range(x,x+n):
        if not check:
            break

        for j in range(y,y+n):
            if color != p[i][j]:
                check = False
                cut(x,y,n//2)
                cut(x,y+n//2,n//2)
                cut(x+n//2,y,n//2)
                cut(x+n//2,y+n//2,n//2)
                break
    if check:
        if color:
            b+=1
        else:
            w+=1
n=int(input())
p=[]
for _ in range(n):
    p.append(list(map(int,input().split())))

cut(0,0,n)
print(w)
print(b)