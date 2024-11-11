n = int(input("입력= "))

for i in range(1, n + 1):
    # 각 줄의 시작 공백을 n - i 만큼 출력
    print(" " * (n - i), end="")

    # 별과 공백을 번갈아가며 출력
    for j in range(i):
        print("*", end=" ")

    print()  # 줄바꿈
