import sys
from collections import deque

# 시간 초과가 나길래 입출력 빠른 sys 사용
input = sys.stdin.readline


# 기본 bfs
def bfs(start):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)


N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)] # 빈 그래프 만들고

# 간선 연결해주고
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 방문처리
visited = [False] * (1 + N)
count = 0  # 노드 개수 저장

# 1~N번 노드를 각각돌면서
for i in range(1, N + 1):
    if not visited[i]:  # 만약 방문하지 않았다면
        if not graph[i]:  # 만약 그래프가 비어있다면 == 지금 방문한 노드가 단말노드이면
            count += 1  # 개수 1개 추가
            visited[i] = True  # 방문 처리
        # 기존 BFS와 다른 부분 요소를 다 세기 위한
        else:  # 만약 그래프가 비어있지 않다면(어느 점과 연결된 점이 있다면 == 단말노드가 아니라면)
            bfs(i)  # 해당 i를 시작노드로 bfs를 돈다.
            count += 1  # 연결요소 를 +1개 해준다.

print(count)