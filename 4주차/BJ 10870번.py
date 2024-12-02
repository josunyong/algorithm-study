# 피보나치 수열
def fivo(n): 
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fivo(n-1)+fivo(n-2) # 입력받은 수의 전과 전전 수의 합을 표현하기 위해 fivo 함수 재귀해서 사용


N=int(input())
print(fivo(N))