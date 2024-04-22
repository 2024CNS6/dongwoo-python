n=int(input())
j=["예","양","성","예","양","성"]
y=["예","양","성","예","양","성"]
s=0
s1=0
print("전우진 : ",end="")
for i in range(n//2):
    if s>2:
        s=0
    print(j[s],end="")
    s+=1
if n%2!=0:
    print(j[s],end="")
print()
print("윤세욱 : ",end="")
for k in range(n//2):
    if s1>2:
        s1=0
    print(y[s1],end="")
    s1+=1


# a, b, ye, n = "", "", "양예성", int(input())
# for i in range(n):
#     if (i%2 == 0): a += ye[i%3]
#     else: b += ye[i%3]
# print(f"{a}\n{b}")