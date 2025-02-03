# -1, 0, 1 존재
# 만약 종이가 모두 같은 수 -> 종이 사용
# 아닐 경우, 9개로 잘라서 사용 -> 2630번과 차이점,

# 같은지 확인하기
def check(x,y,size):
    global count_0, count_1, count_mi

    first_number=paper[x][y] # 첫 숫자 하나 잡고
    # 돌고
    for i in range(x,x+size):
        for j in range(y,y+size):
            # 숫자가 다르다면
            if paper[i][j] != first_number:
                # 3*3 으로 표현하기 위해
                newsize=size//3 # 3의 제곱수로 늘어나니까 //3 사용
                # 분할, size가 3의 제곱으로 늘어나는 구조 (갯수도 3개) -> 어차피 2차원 배열이라 4분위로 접근 -> 오답
                # 앞문제는 4등분하는 거라 가능했지만 이 문제는 9개로 나눠야함

                # 9등분 표현
                # dx 0~2, 상하로 0, 1, 2
                # dy 0~2, 좌우로 0, 1, 2

                # 9개로 등분
                # (0,0), (0,1), (0,2)
                # (1,0), (1,1), (1,2)
                # (2,0), (2,1), (2,2)

                # 3*3을 탐색하겠다는 의미
                for dx in range(3):
                    for dy in range(3):
                        # 재귀적으로 부르며 정확히 9등분
                        check(x+dx*newsize,y+dy*newsize,newsize)

                return

    if first_number==0:
        count_0+=1
    elif first_number==1:
        count_1+=1
    elif first_number==-1:
        count_mi+=1


# 이 부분은 앞선 2630번과 동일
N=int(input())

paper=[]

# 이중 리스트 만들기
for _ in range(N):
    paper.append(list(map(int,input().split())))

# 카운트 할게 하나가 더 는것 뿐
count_0=0
count_1=0
count_mi=0

check(0,0,N)

print(count_mi)  # -1 개수 출력
print(count_0)   # 0 개수 출력
print(count_1)   # 1 개수 출력
