k=0
n=int(input())
if n==0:
    print("장난해?")
for i in range(n):
    m=int(input())
    k+=(m)/1000
if 4.7<=k<=5:
    print("당신은 인간 저울이군.")
else :
    print("이 감자 네가 . 다먹고 다시 가져와.")
