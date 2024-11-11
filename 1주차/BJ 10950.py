# 제출한 오답
T = int(input("테스트케이스 갯수: "))  # 이 부분 오답..

for _ in range(T):
    A, B = map(int, input().split())
    print(A + B)

# 수정한 정답
T = int(input())
# 여기서도 0~T까지만 돌겠다는 의미
for _ in range(T):
    A, B = map(int, input().split())
    print(A + B)