import sys
from collections import deque
input=sys.stdin.readline

N=int(input())
ary=list(map(int,input().split()))

stack=[]
result=[-1]*N
count=[0]*(sorted(ary).pop(-1)+1)

for i in ary:
    count[i]+=1

for i in range(N):
    while stack and (stack[-1][0]<count[ary[i]])  :
        tmp,index=stack.pop()
        result[index]=ary[i]
    stack.append([count[ary[i]],i])
print(*result)