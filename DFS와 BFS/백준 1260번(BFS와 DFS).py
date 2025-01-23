# 정점의 갯수 N, 간선의 갯수 M(두 정점 사이에 여러가지 존재 가능), 탐색을 시작한 정점의 번호 V

# DFS와 BFS의 수행한 결과를 V부터 차례대로 출력

# DFS는 스택or재귀로 구현, BFS는 큐로 구현

# graph로 일단 각 노드들만들어 주고 연결시킴 ==> 탐색할 그래프 생성

# 시작점을 잡고 인접 노드가 있고 그 노드를 방문하지않았으면이라는 조건을 사용
# for i in graph[시작]
#   if not visted[i]

# 방문리스트 visited[false] * (입력받은수)로 시작해서 만듦

from collections import deque

def dfs(start):
    visited[start]=True
    print(start, end=" ")
    for i in graph[start]: # start 노드에 연결된 모든 노드들 순회
        # i가 이제 한개의 노드를 표현
        if not visited[i]: # 아직 False라면 == 방문하지 않았다면
            dfs(i) # 재귀

def bfs(start):
    visited[start] = True # 방문 처리된
    queue=deque([start])

    while queue:
        v=queue.popleft() # 시작점은 큐에서 빼며
        print(v, end=" ") # 출력
        for i in graph[v]: # 현재 노드 V와 연결된 모든 노드들 순회
            if not visited[i]: # visted[i]=False -> 방문하지 않았다면?
                visited[i]=True
                queue.append(i)

n,m,v=map(int,input().split())
graph=[[] for _ in range(n+1)]

# 서로 간선 연결해주는 구조 -> 인접 리스트 사용하는 것
for _ in range(m):
    a,b=map(int, input().split())
    # 서로 더해주면서 서로를 연결
    graph[a].append(b)
    graph[b].append(a)

# 그래프 노드들 sort
for i in range(n+1):
    graph[i].sort()

# dfs
visited = [False]*(n+1)
dfs(v)

print()

# bfs
visited=[False]*(n+1)
bfs(v)


