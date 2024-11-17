def uclid(a,b): # 최대공약수 구하는 유클리드 알고리즘
    while b>0:
        r=a%b
        a=b
        b=r

    return a

a=int(input())
b=list(map(int,input().split()))

c=int(input())
d=list(map(int,input().split()))

# 주어진 수들을 합으로 나타내는 것
A=1
B=1
for i in b:
    A*=i

for j in d:
    B*=j

answer=str(uclid(A,B)) # 마지막 9자리 할려고(슬라이싱 하려고) 문자열로 변환

print(answer[-9:]) # (-9 ~ -1) 까지 마지막 9자리 출력