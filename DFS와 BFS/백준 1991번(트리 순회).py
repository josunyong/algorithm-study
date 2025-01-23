# 전,중,후 다 . 이면 자식X ==> 그래서 다 조건문으로 걸어줌
def dlr(start):
    if start != '.':
        print(start, end='')
        dlr(tree[start][0])  # 왼쪽 자식
        dlr(tree[start][1])  # 오른쪽 자식

def ldr(start):
    if start != '.':
        ldr(tree[start][0])  # 왼쪽 자식
        print(start, end='')
        ldr(tree[start][1])  # 오른쪽 자식

def lrd(start):
    if start != '.':
        lrd(tree[start][0])  # 왼쪽 자식
        lrd(tree[start][1])  # 오른쪽 자식
        print(start, end='')

# 입력 처리
n = int(input())
tree = {} # 트리 딕셔너리로

# 트리 구조 입력
for _ in range(n):
    d, left, right = input().split() # 루트, 왼쪽 자식, 오른쪽 자식 입력
    # 여러 이진 트리로 나눌 때
    # d가 루트 노드 (딕셔너리에서 키) 각각 왼쪽 오른쪽 자식들을 튜플 형태로 받음
    # tree{ d:(left, right) --> tree[d][0]=left, tree[d][1]=right
    tree[d] = (left, right)

# 전위, 중위, 후위 순회 출력
# 항상 루트 노드(시작 노드)는 A
dlr('A')
print()
ldr('A')
print()
lrd('A')
