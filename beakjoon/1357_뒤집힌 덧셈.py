n,m=input().split()
n_rv=''
m_rv=''
p_rv=''
for i in n:
    n_rv=i+n_rv
for j in m:
    m_rv=j+m_rv
sum=str(int(n_rv)+int(m_rv))
for p in sum:
    p_rv=p+p_rv
print(int(p_rv))
