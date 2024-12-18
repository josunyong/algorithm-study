# 소수 찾기
'''
문제
주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

입력
첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

출력
주어진 수들 중 소수의 개수를 출력한다.

예제 입력 1
4
1 3 5 7
예제 출력 1
3
'''

N=int(input()) # 몇개 인지 입력
M=list(map(int,input().split())) # 입력 받은 각 숫자들을 공백 기준으로 리스트(배열)에 넣고

count=0 # 소수 갯수를 셀 변수 설정

# 리스트에 있는 숫자들이 각각 소수인지를 판별하기 위해 모든 숫자를 i로 돎
for i in M:
    if i==1: # 1이면 pass
        continue
    for j in range(2,int(i**(0.5)+1)): # j가 그 i가 1과 본인(i)의 제곱근으로 나뉘는지 확인
        if i%j==0: # i가 나뉘면 소수가 아님
            break
    else:
        count+=1 # 안나뉘면 그건 소수니까 갯수+1

print(count)