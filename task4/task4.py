import math
n=int(input())
m=((n+1)*n)//2
k=[]
q=[]
for j in range(n):
    k.append(j+1)
if m%2==0 and n%2==0:
    for i in range(0,n//2-1,2):
        k[i]=str('+')
        k[i+1]=str('-')
        k[n-1-i]=str('+')
        k[n-2-i]=str('-')
    print(''.join(k))
elif m%2==0 and n%2!=0:
    for b in range(4,n+1):
        q.append(b)
    for l in range(0,(n-3)//2-1,2):
        q[l]=str('+')
        q[l+1]=str('-')
        q[n-4-l]=str('+')
        q[n-5-l]=str('-')
    print('--+'+''.join(q))
else:
    print('IMPOSSIBLE')