N = int(input())

for i in range(1, N + 1):  # 행 별출력

    for j in range(1, i + 1):
        print("*", end="")  # 열 별출력
    print()  # 삼각형의 한줄 바꿔주기