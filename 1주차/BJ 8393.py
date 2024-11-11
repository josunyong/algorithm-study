# 처음 틀린 답
n=int(input())

'''
for i in range(1,n+1):
    a+=i

print(a)
'''

# 다시 풀어 맞은 답
n=int(input())

a=0 # 이렇게 값을 초기화 하지 않으면
    # UnBoundLocalError 발생으로 런타임 에러
for i in range(1,n+1):
    a+=i  # 연산 활동

print(a)