# 이중 리스트로 종이 만들고 입력받은 숫자 넣기

# 탐색하는 함수 만들기 -> 이중 for문으로 종이를 돌면서 첫색깔과 같은지 확인

# 첫 색깔과 다르다면 종이를 4등분 (분할) 하여 다시 그 안에서 재귀(정복)으로 돈 후 종료

def one_color(x,y,size):
    global count_white, count_blue # 이 함수 안에서 뿐 아니라 이따 출력값에도 바로 쓰기 위해서 전역변수로 설정
    frist_color=paper[x][y] # 첫번째 색깔 설정

    # 첫색깔과 같은지 돌아보는 구조
    for i in range(x, x+size):
        for j in range(y, y+size):
            # 색깔이 다르다면
            if paper[i][j]!=frist_color:
                # 4등분으로 나누어 그 안에서 다시 첫색깔과 비교
                newsize=size//2 # 분할 (쪼개기)

                # 행렬이니까 y가 좌우, x가 위아래
                # 재귀하며 정복(쪼갠 거 사용)

                # 반복문으로도 구현 가능

                one_color(x,y,newsize) # 왼쪽 위
                one_color(x,y+newsize,newsize) # 오른쪽 위
                one_color(x+newsize,y,newsize) # 왼쪽 아래
                one_color(x+newsize,y+newsize,newsize) # 오른쪽 아래

                return # 자르고 난 뒤 종료

    # 각 색종이 색깔에 따라 카운트 수 더해주기
    if frist_color==0:
         count_white+=1
    elif frist_color==1:
         count_blue+=1


N=int(input())

paper=[]

for _ in range(N):
    paper.append(list(map(int,input().split())))


# 각각 하얀 종이를 나타내는 숫자, 파란 종이를 나타내는 숫자
count_white=0
count_blue=0

one_color(0,0,N) # 사이즈는 입력받은 N만큼
print(count_white)
print(count_blue)

