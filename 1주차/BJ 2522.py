
# 2455번 풀때 위아래로 두고 증가, 감소 형식 사용
N = int(input())

for i in range(1, N + 1): # 위
    print(" "*(N-i),end="")
    print("*" * i)

for i in range(N-1,0,-1): # 아래
    print(" "*(N-i),end="")
    print("*" * i)
