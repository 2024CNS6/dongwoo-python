nums=[i for i in range(1,10001)]
for k in range(1,10000):
    sum=0
    if k>=1000:
        sum+=k+k//1000
        k-=(k//1000)*1000
        sum+=k//100
        k-=(k//100)*100
        sum+=k//10
        k-=(k//10)*10
        sum+=k%10
        if sum in nums:
            nums.remove(sum)
    elif k>=100:
        sum+=k+(k//100)+(k-((k//100)*100))//10+(k-((k//100)*100))%10
        if sum in nums:
            nums.remove(sum)
    elif k>=10:
        sum+=k+k//10+k%10
        if sum in nums:
            nums.remove(sum)
    elif k<10:
        sum+=k+k
        if sum in nums:
            nums.remove(sum)
for o in nums:
    print(o)