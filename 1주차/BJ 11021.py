# 처음 제출한 틀린 답
T = int(input())

for i in range(1, T + 1):
    A, B = map(int, input().split())
    print(f"Case #{i}:{A + B}")  # 틀린 부분

# 다시 풀어 맞은 답
T = int(input())

for i in range(1, T + 1):
    # f-string 사용
    A, B = map(int, input().split())
    # 문자열 앞에 f 문자열 {변수i} : {입력받은 두 수의 합}
    print(f"Case #{i}: {A + B}")