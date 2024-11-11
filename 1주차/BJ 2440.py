N=int(input())

for i in range(N,0,-1): # for문에서 큰 수부터 하나씩 줄여가며
    for j in range(1,i+1): # 여기도 5개부터 줄여가니 i 따라서
        print("*",end="")
    print()

