'''
문제
정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

명령은 총 다섯 가지이다.

push X: 정수 X를 스택에 넣는 연산이다.
pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 스택에 들어있는 정수의 개수를 출력한다.
empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
입력
첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.

출력
출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.
'''

# 못품(정답참조) => 스택은 구현을 했으나, 입출력 부분을 해결 못했음(런타임에러, 시간초과)

import sys # sys를 이용하기 위해
n = int(sys.stdin.readline())

# sys 사용해서 문제 해결
# sys는 입출력 중(input(), raw_input()등)속도가 가장 빠름

stack=[] # 리스트로 스택 구현
for i in range(n):
    command = sys.stdin.readline().split() # 표준입력장치로 입력받은 명령어를 공백 단위로 잘라 command 라는 리스트에 저장

    if command[0]=='push': # 내가 만약 push 2 란 값을 넣으면 command 라는 리스트에 [push, 2] 로저장
                           # 그러므로 command[0] = push, command[1]=2
        stack.append(command[1]) # 입력받은 수를 넣겠다는 뜻

    elif command[0]=='pop': # pop 하나만 입력받으면 command[0]=pop 이니까
        if len(stack)==0: # 비어있으면
            print(-1)
        else:
            print(stack.pop())
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        if len(stack)==0: # 비어있으면
            print(1)
        else:
            print(0)
    elif command[0] == 'top':
        if len(stack)==0: # 비어있으면
            print(-1)
        else:
            print(stack[-1])

# "sys 입출력"