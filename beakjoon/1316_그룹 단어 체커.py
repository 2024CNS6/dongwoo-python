n=int(input())
for i in range(n):
    st=list(input())
    for k in range(len(st)):
        if k<len(st)-1:
            if st[k]==st[k+1]:
                pass
            elif st[k] in st[k+1:]:
                n-=1
                break
print(n)