# 집 N개, 공유기 C개
# 인접한 두 공유기의 길이가 최대가 될 수 있게
# 맨 왼쪽(처음 집)에 공유기 하나 설치 후, 공유기 간의 거리 d를 찾고 그거를 사용하는 식으로

# 공유기 간 최소 거리를 최대로 설정 -> 이분 탐색

# 정답참조 (돌아가는 원리 정리)
# find_d() 이분탐색 수행 -> count_router을 반복 호출하면서 최적의 d를 찾음
# counter_router은 현재 d값으로 공유기를 몇개 설치 할 수 있는지 계산
# C값과 d값을 비교해가며 mid(확인할 거리)를 알맞게 조정해감
def find_d(N,C,postions):
    postions.sort()
    left,right=1, postions[-1]-postions[0] # 각각 최소거리(바로 옆집에 설치했다는 생각), 최대거리(첫집과 맨 마지막 집 사이의 거리)
    d=0
    while left<=right:
        mid=(left+right)//2 # 현재 확인할 거리


        if count_router(postions,mid)>= C: # 공유기 갯수가 충분하면
            d=mid #거리를 더 늘리기 위해
            left=mid+1 # 오른쪽으로 이동


        else: # 공유기 갯수가 부족하면(거리가 너무 멀어 설치하는게 부족하면)
            right=mid-1 # 거리를 줄이기 위해 왼쪽으로 이동
    return d # 거리 찾는게 목적




def count_router(positions, d):
    count=1
    first_router=positions[0]
    for i in range(1,len(positions)): # 인덱스는 0부터 시작 두번째 집 == 인덱스 1
        if positions[i]-first_router >=d: # d가 우리가 구한 인접한 공유기 간 최대 거리보다 특정 집과 첫 집의 거리가 더 크다면
            # 그 특정 집에 공유기를 설치
            count+=1
            first_router=positions[i]

    return count

N,C=map(int,input().split())

positions=[]

for _ in range(N):
    home=int(input())
    positions.append(home)

print(find_d(N,C,positions)) # d 반환해서 출력 하게



