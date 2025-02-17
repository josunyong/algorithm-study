# 재료 N개
# 재료는 적어도 하나를 사용하지만 N개 다 안써도 됨
# 신맛 S, 쓴맛 B -> 신맛은 재료의 곱으로 쓴맛은 재료의 합으로 표현

# 백준에 나와있는 예제 입력 2번까지는 성공
# 3번에서 막힘 -> 4개중 최소가 되는 3개만 사용하는 경우
# 지금 내가 짠건 모든 신맛, 쓴맛 다 계산해서 그 차이를 내는 것 -> 최소가 되는 조건에 부합 X

# 정답 참조
# 재귀로 접근 -> 인덱스로 접근하여 그 맛(쓴맛, 신맛)을 선택하거나 안하거나 -> 최솟값 비교해가며 값을 냄

N=int(input())

taste=[]

# 이중 리스트 사용
for _ in range(N):
    taste.append(list(map(int,input().split())))

# 최솟값 초기화
min_taste=float('inf') # 초기값을 무한대로 설정 -> 어떤 값과 비교하든지 그 값이 더 작아서 갱신


# 재귀 함수용
def dfs(index, S, B, count):
    global min_taste # 최솟값을 전역변수로

    if count>0: # 한가지맛 이상을 반드시 써야하기에 한 번 이상 재귀 호출된 경우만 비교
        min_taste = min(min_taste, abs(S-B)) # 여기서 갱신해가면서 최솟값을 찾음

    if index==N: # 다 돌았으면 끝
        return

    dfs(index+1,S,B,count) # 선택 X, 배열만 한칸 옆으로
    dfs(index+1,S*taste[index][0], B+taste[index][1], count+1) # 선택 O -> 신맛은 곱, 쓴맛은 덧셈 호출횟수+1

# 초기 값 설정
# 인덱스 0, S는 곱을 위한 1, B는 0, 횟수도 0
dfs(0,1,0,0)
print(min_taste)