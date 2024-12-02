# 백준 10989번 수 정렬하기3

# 처음엔 그냥 리스트로 다 받고 난 후 .sort하고 리스트 원소 하나하나 출력하는 구조 => 메모리 초과

# 입출력을 sys 써서 좀 좀 빠르게 처리해봤지만 => 메모리 초과



# 인덱스를 활용하여 문제를 푸는 구조로 접근, append가 메모리 초과를 일으키는 원인
import sys

n = int(sys.stdin.readline())
num_list = [0] * 10001 # 리스트를 입력받는 수만큼 만들어 놓고

for _ in range(n):
    num_list[int(sys.stdin.readline())] += 1 # 카운트를 

for i in range(10001):
    if num_list[i] != 0: # 원소들 다 돌면서 그게 인덱스에 +가 되어있다면
        for j in range(num_list[i]):
            print(i) # 그 값 출력