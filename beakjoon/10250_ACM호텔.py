m=int(input())
for i in range(m):
    h,w,n=map(int,input().split())
    if n%h!=0:
        cmd=n%h
        hosu=(n//h)+1
    else:
        cmd=h
        hosu=n//h
    if hosu>9:
        print(str(cmd)+str(hosu))
    else:
        print(str(cmd)+"0"+str(hosu))