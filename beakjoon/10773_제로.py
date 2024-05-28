n=int(input())
sum_list=[]
for i in range(n):
    nums=int(input())
    if nums!=0:
        sum_list.append(nums)
    if nums==0:
       del sum_list[-1]

print(sum(sum_list))