
import sys
from collections import deque
input = sys.stdin.readline


n=int(input())

graph=[[0] for _ in range(n+1)] # 각 노드들 만들기

# 연결리스트를 활용하여 각 노드들 연결 하기
for _ in range(n-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

parent=[0]*(n+1) # 부모정보 저장 노드
parent[1]=0 # 루트노드(1)은 부모가 X
que=deque()
que.append(1)

# 큐가 빌 때 까지
while que:
    v=que.popleft() # 루트노드를 제외한 첫노드 (부모는 루트 노드)
    for i in graph[v]:
       if parent[i]==0:
          parent[i]=v # 처음 큐에 들어있던 노드가 i의 부모가 되고
          que.append(i) # i도 큐에 들어감으로 누군가의 부모 or 큐가 비면 단말 노드로 끝

print('\n'.join(map(str,parent[2: ])))