n=(int(input()))
s=0
p=0
if n==0:
    print(1)
else:
    if n<10:
        s10=n*10
        s1=0
    s10=n//10
    s1=n%10
    while s!=n:
        s=(s10+s1)%10+s1*10
        s10=s//10
        s1=s%10
        p+=1
    print(p)