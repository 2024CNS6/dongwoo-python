s=0
o=0
for i in range(20):
    subject,n,score=input().split()
    n=float(n)
    if score !="P":
        if score == "A+":
            score=4.5
        elif score == "A0":
            score=4.0
        elif score == "B+":
            score=3.5
        elif score == "B0":
            score=3.0
        elif score == "C+":
            score=2.5
        elif score == "C0":
            score=2.0
        elif score == "D+":
            score=1.5
        elif score == "D0":
            score=1.0
        elif score == "F":
            score=0.0
        s+=score*n
        o+=n
print(s/o)