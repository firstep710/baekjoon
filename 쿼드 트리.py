answer=''
def cut(x,y,n):
    global answer
    num=v[x][y]
    check=True
    if n==1:
        answer+=v[x][y]
        return
    for i in range(x,x+n):
        if not check:
            break

        for j in range(y,y+n):
            if num!=v[i][j]:
                check=False
                break
    if check:
        answer+=str(v[i][j])
    else:
        answer+="("
        cut(x,y,n//2)
        cut(x,y+n//2,n//2)
        cut(x+n//2,y,n//2)
        cut(x+n//2,y+n//2,n//2)
        answer+=")"

n=int(input())
v=[]
for _ in range(n):
    v.append(list(input()))

cut(0,0,n)
print(answer)