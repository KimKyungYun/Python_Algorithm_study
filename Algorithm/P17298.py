import sys
from collections import deque
input=sys.stdin.readline

N=int(input())
ary=list(map(int,input().split()))

stack=deque()
result=[-1]*N

for i in range(N):
    while stack and (stack[-1][0]<ary[i]):
        tmp,index=stack.pop()
        result[index]=ary[i]
    stack.append([ary[i],i])
print(*result)