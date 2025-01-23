# 기본 BFS 문제
# 거기에 총 탐색 횟수 cnt를 사용


from collections import deque

# 기본 BFS 함수에 cnt만 추가
def virus(start):

    cnt=0
    queue=deque([start])
    visited[start]=True

    while queue:
        v=queue.popleft() # 맨 앞의것은 pop
        for i in graph[v]: # 시작 노드 v와 연결된 노드 i들을 순회
            if not visited[i]: # 방문하지 않았다면
                visited[i]=True # 방문처리하고
                queue.append(i) # 큐에 넣기
                cnt+=1 # 이때 횟수를 +1

    return cnt

N=int(input()) # 컴퓨터 수를 노드라 생각
M=int(input()) # 연결된 네트워크수를 간선이라 생각
graph=[[]for _ in range(N+1)]

for i in range(M): # 노드끼리 간선으로 연결 시키기
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)


visited=[False]*(N+1) # 방문배열

print(virus(1)) # 시작은 1이니까

