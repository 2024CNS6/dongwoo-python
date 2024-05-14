c=int(input())
for i in range(c):
    ns = 0
    ins = 0
    agr = 0
    students=list(map(int,input().split()))
    for j in range(len(students)-1):
        agr+=students[j+1]
    agr/=students[0]
    for k in range(len(students)-1):
        if students[k+1] >agr:
            ns+=1
    print(f"{(ns/students[0])*100:.3f}%")