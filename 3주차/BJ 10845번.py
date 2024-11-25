# 큐 문제

# deque는 리스트처럼 작동 / queue는 리스트처럼 작동X -> 큐의 앞 뒤를 확인하기 어려운 이유
# 단일 스레드에선 deque를 그냥 que처럼 활용하기도

from collections import deque # 기본 큐 라이브러리도 존재 그걸 써도되고 리스트로 표현해도 될거같은데
# front, back 명령어를 쉽게 쓰기 위해 deque 사용 10866번도 이런식으로 접근 할듯

import sys # 빠른 입출력을 사용하기 위해 sys 라이브러리

que=deque() # que라는 이름으로 덱 객체 생성

n=int(sys.stdin.readline()) # 입력받고

for i in range(n): # 입력받은 만큼
    command=sys.stdin.readline().split() # 받은 거 공백으로 잘라서 command라는 리스트에 넣고

    if command[0]=="push": # 넣고
        que.append(command[1]) # pop()은 존재하는데 push는 없으니 append로

    elif command[0]=="pop": # pop
        if not que:
            print(-1)
        else:
            print(que.popleft()) # .pop()은 맨 뒷값 즉 맨 마지막으로 들어온값 하지만 큐는 FIFO 구조 -> .popleft() 맨 앞값(처음 들어온 값)

    elif command[0]=="size": # 크기 반환
        print(len(que))

    elif command[0]=="empty":
        if not que:
            print(1)
        else:
            print(0)

    elif command[0]=="front": # 맨 앞값 확인
        if not que:
            print(-1)
        else:
            print(que[0]) # 큐의 맨앞

    elif command[0]=="back": # 맨 뒷값 확인
        if not que:
            print(-1)
        else:
            print(que[-1]) # 큐의 맨뒤




