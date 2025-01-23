# 정답 참조
# 배추 밭을 2차원 리스트로 생각
# DFS도 2차원 리스트를 도는 구조로 함수를 만들기

# 재귀 호출 횟수를 제한 Recrusion 에러 방지
import sys
sys.setrecursionlimit(10000) # 재귀 깊이 설정

# DFS
def dfs(x,y):
    directions = [(-1,0), (1,0), (0,-1), (0,1)] # 방향 상 하 좌 우
    visited[x][y]=True # 처음 방문 x행 y열 방문
    for dx, dy in directions: #
        # 각각 행과 열의 움직임을 반영
        nx=x+dx
        ny=y+dy
        # 이 부분에서 처음 인덱스에러가 뜸
        # 인덱스는 0부터 싲가이니까 행 끝까지는 N-1이기 때문에 N보다는 작아야함 / 열도 마찬가지
        if 0<=nx<N and 0<=ny<M and graph[nx][ny]==1 and not visited[nx][ny]: # 각 행, 열 움직임이 최대행(N)과 최대열(M) 사이에 있고 방문 한적이 없으면
            dfs(nx,ny) # 재귀 호출



T = int(sys.stdin.readline())
for _ in range(T):
    M,N,K=map(int,input().split())
    graph=[[0]*M for _ in range(N)] # N * M 행렬
    visited=[[False]*M for _ in range(N)] # N * M 짜리 방문 행렬

    for _ in range(K):
        x,y=map(int,input().split())
        # x가 가로 y가 세로
        # 가로는 열이고 세로는 행이니까
        # [y][x] 순서가 행열을 나타내는 것
        graph[y][x]=1
    cnt=0
    for i in range(N):
        for j in range(M):
            if graph[i][j]==1 and not visited[i][j]:
                dfs(i,j)
                cnt+=1
    print(cnt)



