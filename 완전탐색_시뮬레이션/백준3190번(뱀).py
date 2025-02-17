# 판은 이중리스트, 사과는 각 인덱스 입력받은 곳을 1로 표현
# 머리를 벽에 박는 것은 0<=움직임<=유효한 판의 크기로 판단

# 몸이 늘어나는 코드, 머리를 자기 몸에 박는 코드, (L,D)의 움직임 표현(머리 위치에 따라 연산이 다르다 생각) -> 정답참조

# 큐를 사용하여 뱀을 표현
from collections import deque

N=int(input()) # 게임판
K=int(input()) # 사과 개수

# 게임판 만들기(이중리스트 사용)
board=[[0]* N for _ in range(N)]

# 사과 넣기
for _ in range(K):
    x,y=map(int,input().split())
    # 인덱스는 0부터 시작이니 행과 열 -1씩
    board[x-1][y-1]=1

# 방향 정보
L=int(input())
# 딕셔너리 사용
directions={}
for _ in range(L):
    X,C=input().split()
    # {시간 : 방향} 구조
    directions[int(X)]=C

# 방향 벡터
dx=[0,1,0,-1]
dy=[1,0,-1,0]

# 처음에는 맨 왼쪽 시작
direction=0

# 게임시작
time=0

# 뱀의 머리는 큐의 맨 뒤에 요소 / 뱀의 꼬리는 큐의 맨 앞에 요소를
snake=deque([(0,0)]) # 뱀을 큐로 표현(머리가 앞쪽)
board[0][0]=2 # 0은 그냥 판 / 1은 사과 / 2는 뱀

while True:
    time+=1
    head_x, head_y = snake[-1]  # 머리 위치
    nx, ny = head_x + dx[direction], head_y + dy[direction]  # 다음 이동한 위치

    # 벽이나 자기 자신에게 부딪히면 종료
    if nx < 0 or nx >= N or ny < 0 or ny >= N or board[nx][ny] == 2:
        break

    # 사과가 있는 경우
    if board[nx][ny] == 1:
        # 사과의 위치에 뱀의 머리가 가고
        board[nx][ny] = 2  # 사과를 먹은 곳을 뱀의 머리가 있는 곳으로 갱신

        # 머리가 그쪽으로 이동한것을 표현
        snake.append((nx, ny))  # 뱀의 머리가 이동한 위치를 큐에 추가
        # 오로지 더하기만 있기때문에 뱀의 길이가 늘어났음을 표현

    # 사과가 없는 경우
    else:
        # 사과의 위치에 뱀의 머리가 가고
        board[nx][ny] = 2  # 사과를 먹은 곳을 뱀의 머리가 있는 곳으로 갱신

        # 머리가 그쪽으로 이동한 것을 표현
        snake.append((nx, ny))  # 뱀의 머리가 이동한 위치를 큐에 추가

        # 꼬리 부분 큐에서 제거
        tail_x, tail_y = snake.popleft()
        # 판의 꼬리를 나타내는 부분을 0으로 초기화 하며 꼬리를 잘라 길이를 유지
        board[tail_x][tail_y] = 0

    # 시간이 방향 딕셔너리에 있고
    if time in directions:
        # 그 시간의 value가 L이면
        if directions[time] == 'L':
            # 반시계로 돌고
            direction = (direction - 1) % 4
        # 그 시간의 value가 D이면
        else:
            # 시계 방향으로 돈다
            direction = (direction + 1) % 4

print(time)
