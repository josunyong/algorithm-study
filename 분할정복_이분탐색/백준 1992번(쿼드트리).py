# 흰점 0, 검은색 1 -> 4개씩 묶어서 출력
# 일단 4등분 하는 식으로 접근 출력값 바꾸는 구조로
# 출력하는 부분 result라는 변수를 만들어서 괄호와 값을 넣어줌

def check(x,y,size):

    # 첫번째 값 고르는 것
    first_color=paper[x][y]
    # 전체 돌고 -> 영역이 같은 색인지 확인
    for i in range(x,x+size):
        for j in range(y,y+size):
            # 4등분 하는구조
            if paper[i][j]!=first_color: # 이렇게 숫자가 첫 숫자와 다른 경우에만 result가 생기는데
                newsize=size//2
                # result라는 변수를 만들어서
                # ( 넣고
                result="("

                # 0~1, 0~1 로 표현하니까 2*2 리스트 (원소 4개), 재귀보단 반복이 시간복잡도면에서 이득 같아서 사용
                # 새롭게 잘린(newsize) 그 판 안에서 dx-> 상하, dy->좌우로 움직이는 구조
                for dx in range(2):
                    for dy in range(2):
                        # 결과값 넣고
                        result+=check(x+dx*newsize, y+dy*newsize, newsize)

                # ) 넣으며 닫아줌
                result+=")"
                return result


    return str(first_color) # 이렇게 바로 문자열로 처리하여 모든 숫자가 같은 경우도 값이 나오게 함
N=int(input())

paper=[]

for _ in range(N):
    paper.append(list(map(int,input().strip()))) # 여기 split일땐 오류 떴었음 -> 문제에서 주어진 입력이 공백이없으니까 split는 indexerror + 오히려 공백제거 strip

print(check(0,0,N)) # 이게 0,0 이라는 가장 첫행 첫열