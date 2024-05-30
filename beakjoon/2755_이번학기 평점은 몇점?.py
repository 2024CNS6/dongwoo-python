n=int(input())
sum=0
hs=0
for i in range(n):
    name,m,score=input().split()
    hs+=int(m)
    if score=="A+":
        score=4.3
    elif score=="A0":
        score=4.0
    elif score=="A-":
        score=3.7
    elif score=="B+":
        score=3.3
    elif score=="B0":
        score=3.0
    elif score=="B-":
        score=2.7
    elif score=="C+":
        score=2.3
    elif score=="C0":
        score=2.0
    elif score=="C-":
        score=1.7
    elif score=="D+":
        score=1.3
    elif score=="D0":
        score=1.0
    elif score=="D-":
        score=0.7
    else:
        score=0
    sum+=int(m)*score
j=(float(str(sum/hs)[0:5]))*1000
if j % 10 >=5:
    j+=(10-j%10)
else:
    j -= (j % 10)
j/=1000
print(f"{j:.2f}")