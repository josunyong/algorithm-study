# sudo code
# 해결하고자 하는 문제 명시
# 어떻게 해결할지 작성

# 정답 참조

# fibo(0)은 0을 반환한다
# fibo(1)은 1을 반환한다
# fibo(N)은 fibo(N-1)과 fibo(N-2)를 호출한다

# fibo(N)을 호출했을 때, 0과 1이 각각 몇번 출력되는지 구해라

# 동적알고리즘이므로 0호출, 1호출 배열 fibo(0~2)까지 만들어 사용한다
# 0호출과 1호출도 각각 피보나치 규칙에 적용받는 것을 찾는다
# fibo(n)의 각각 0,1 호출은 == fibo(n-1)의 0,1 호출 + fibo(n-2)의 0,1 호출

'''
피보 함수생성
0~2까지의 0 호출 배열, 1 호출 배열 생성
zero 배열 
one 배열

if 숫자 >= 3이면
    for 3부터~N까지
        (N-1) 0 호출 횟수 + (N-2) 0 호출 횟수
        (N-1) 1 호출 횟수 + (N-2) 1 호출 횟수
        

케이스 수 입력
for 케이스 수
    숫자입력
    피보(입력받은 숫자)
'''


def fibo(N):
    
    zero=[1,0,1] # 0 호출 배열
    one=[0,1,1] # 1 호출 배열
    
    if N>=3:
        for i in range(3,N+1): # 0~2까지는 배열을 생성해뒀으니 3~N까지
            # N까지 그 전과 그 전전 값을들 더해가며 ==> 규칙
            zero.append(zero[i-1]+zero[i-2])
            one.append(one[i-1]+one[i-2])

    print(zero[N],one[N])


T=int(input())
for _ in range(T):
    N=int(input())
    fibo(N)