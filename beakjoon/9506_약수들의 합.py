while 1:
    n=int(input())
    sl=[]
    if n==-1:
        break
    else:
        for i in range(1,n):
            if n%i==0:
                sl.append(i)
        if sum(sl)==n:
            print(f"{n} = ", end="")
            for k in range(len(sl)):
                if k == len(sl)-1:
                    print(sl[k])
                else:
                    print(f"{sl[k]} +",end=" ")
        else:
            print(f"{n} is NOT perfect.")