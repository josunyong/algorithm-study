N=int(input())


for i in range(2,int(N**0.5)+1): # 제곱근 이용 소수
    while N%i==0: # 만약 소수로 나누어 떨어진다면?
        print(i) # 출력하고
        N=N//i # 그 몫을 다시 소수로 나누기 위해 값 갱신

if N>1:
    print(N) # 마지막 값
