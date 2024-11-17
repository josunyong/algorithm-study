N,M=map(int,input().split())

divi=[]

for i in range(1,N+1):
    if N%i==0 and M%i==0: # 둘 다 나뉘면 공약수
        divi.append(i)



multi=N*M//max(divi) # 두수의 곱 == 최소공배수 * 최대공약수



print(max(divi)) # 최대공약수 출력
print(multi)


