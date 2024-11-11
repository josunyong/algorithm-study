# 틀린 정답
N = int(input())

for i in range(1, N + 1): # 위
    print("*" * i, end=" ") # 오른쪽

    if i != N:
        print(" " * (2 * N - 2 * i - 1), end=" ") # 왼쪽
        print("*" * i)
    else:
        print()

for i in range(N - 1, 0, -1): # 아래
    print("*" * i, end=" ") # 오른쪽
    print(" " * (2 * N - 2 * i - 1), end=" ") # 왼쪽
    print("*" * i)
'''
*         *
**       **
***     ***
****   ****
***** 
****   ****
***     ***
**       **
*         *
'''
# 출력값이 이렇게 나와서 틀림

# 참조한 코드
n = int(input())
for i in range(1,n+1): # 위
    print("*" * i + " " * 2*(n-i) + "*" * i) # * 공백 * -> 증가하는 식
for j in range(1,n): # 아래
    print("*"* (n-j) + " " * 2*j + "*" * (n-j)) # * 공백 * -> 감소하는 식