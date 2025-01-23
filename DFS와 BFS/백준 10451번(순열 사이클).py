# 기본 DFS에 방문 노드가 가리키는 다음 노드를 결정 지어주는 느낌
# visted[start]에 있는 값이  다음 노드인 numbers[start]에 있는 값을 가리킴
# 그러므로 방문 노드가 가리키는 다음 노드인 numbers[start]를 number이라는 변수로 받아 처리

def dfs(start):
    # 이렇게 현재 방문 노드와 다음 방문 노드 ( <- 이 표현이 어려웠음) 를 표현한뒤 DFS
    visited[start]=True # 현재 방문 노드
    number=numbers[start] # 방문 노드가 가리키는 다음 노드
    if not visited[number]: # 그 노드가 아직 방문하지 않은 상태라면?
        dfs(number) # 재귀 호출


T=int(input())
for _ in range(T):
    N=int(input())
    numbers=[0]+list(map(int,input().split())) # 리스트 입력순서대로 받는 것
    visited=[False]*(N+1) # 방문 노드 생성
    result=0

    for i in range(1,N+1):
        if not visited[i]:
            dfs(i)
            result+=1
    print(result)

