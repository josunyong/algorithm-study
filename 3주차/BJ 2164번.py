# 카드 2

from collections import deque

que=deque()

n=int(input())

for i in range(1,n+1): # 이게 일단 큐에 다 넣고
    que.append(i)


while len(que)>1:
    que.popleft() # 맨 앞 버리고
    que.append(que.popleft())

print(que.pop())