n,m= map(int,input().split())

bunmo=1
bunja=1

for i in range(1,m+1):
    bunmo*=(n-(i-1)) # 분모계산 (조합식의 계산 이걸 생각 못했음)
    # 분모 == n*(n-1)*(n-2) .... (n-m+1) 이 공식을 못유도함
    bunja*=i # 분자

print(bunmo//bunja)



