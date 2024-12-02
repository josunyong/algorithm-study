# 카드 2

from collections import deque

que=deque()

n=int(input())

for i in range(1,n+1): # 이게 일단 큐에 다 넣고
    que.append(i)


while len(que)>1: # 큐의 마지막이 남을 때 까지 반복
    que.popleft() # 맨 앞 버리고
    que.append(que.popleft()) # 두번째 껀 맨앞에 넣고

print(que.pop()) # 이렇게 되면 마지막에 남은게 출력