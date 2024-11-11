n = int(input())

for i in range(1, n + 1):
    # 기본 피라미드 모양을 만들기 위한 왼쪽 공백 출력
    print(" " * (n - i), end="")

    # 첫번째 줄, 마지막줄, 중간(공백이 있는 줄)
    if i == 1:  # 첫 번째 줄
        print("*")
    elif i == n:  # 마지막 줄
        print("*" * (2 * n - 1))
    else:  # 중간 줄
        print("*" + " " * (2 * i - 3) + "*") #요 규칙을 찾는게 오래걸렸음
