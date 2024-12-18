'''
문제 4948번
베르트랑 공준은 임의의 자연수 n에 대하여, n보다 크고, 2n보다 작거나 같은 소수는 적어도 하나 존재한다는 내용을 담고 있다.

이 명제는 조제프 베르트랑이 1845년에 추측했고, 파프누티 체비쇼프가 1850년에 증명했다.

예를 들어, 10보다 크고, 20보다 작거나 같은 소수는 4개가 있다. (11, 13, 17, 19) 또, 14보다 크고, 28보다 작거나 같은 소수는 3개가 있다. (17,19, 23)

자연수 n이 주어졌을 때, n보다 크고, 2n보다 작거나 같은 소수의 개수를 구하는 프로그램을 작성하시오.

입력
입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 케이스는 n을 포함하는 한 줄로 이루어져 있다.

입력의 마지막에는 0이 주어진다.

출력
각 테스트 케이스에 대해서, n보다 크고, 2n보다 작거나 같은 소수의 개수를 출력한다.

제한
1 ≤ n ≤ 123,456
예제 입력 1
1
10
13
100
1000
10000
100000
0
예제 출력 1
1
4
3
21
135
1033
8392
'''

# 소수인지 아닌지를 판단하는 prime 함수
def prime(x):
    if x==1:
        return False
    for i in range(2,int(x**0.5)+1): # 연산 줄이기 위해 제곱근 활용
        if x%i==0:
            return False
    else:
        return True

# 그냥 일일히 계산하지 않기 위하여 리스트에 소수만 넣어놓고 꺼내는 방식을 활용
eratos_list=list(range(1,246913)) # 이 범위는 1 ≤ n ≤ (123,456)*2 -> n~2*n이니까 백준 문제의 제한 범위

prime_list=[] # 소수만 담을 리스트

for i in eratos_list: # 모든 수 돌면서
    if prime(i): # 소수만 소수 리스트에 넣기
        prime_list.append(i)

while True:
    n=int(input())
    count = 0
    if n==0:
        break


    for i in prime_list: # 소수 리스트를 돌면서
        if n<i<=n*2: # 이 범위 안에 있으면 -> 일일히 그 수가 소수인지 아닌지 판단하는 식을 쓸 필요X == 연산 빨라짐
            count+=1 # 카운트만 올리면 됨
    print(count)

# 이해를 못해서 사용은 못한..
# 에라토스테네스의 체는 소수를 효율적으로 찾아내는 알고리즘
# 배수의 성질을 이용해 소수가 아닌 수들을 걸러내는 것
# 2~N까지의 리스트를 만들어서 2의 배수부터 없애고, 3의 배수 없애고, 4의 배수는 이미 2의 배수에서 없어졌고 그 후 5의 배수 없애고 이런 식으로 쭈욱 해가는 구조

