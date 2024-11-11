n = int(input())

# 피라미드 찍기

for i in range(n, 0, -1):  # 위에 역 피라미드

    print(" " * (n - i), end="")
    print("*" * (2 * i - 1))

for i in range(2, n + 1):  # 아래 정 피라미드
    print(" " * (n - i), end="")
    print("*" * (2 * i - 1))
