# 처음에 그냥 max 값 구해서 sum < M 할떄까지 max-1로 생각 -> 시간초과 오류
# 이분 탐색 방법



N=int(input())

requests=list(map(int,input().split()))

M=int(input())

# 왼쪽 0, 오른쪽 가장 큰값 1 이런 일직선이 있다고 생각
left,right=0,max(requests)

# 답을 넣을 변수
answer=0


# left가 right보다 작거나 같을 때까지 -> left가 넘어가면 답을 찾아냈단 소리
while left<=right:
    mid=(left+right)//2 # 미드는 정중앙 이게 결국 최대 상환액
    total=sum(min(mid, req)for req in requests) # 각 원소를 중앙값과 비교해서 작은 것을 누적해서 더해감, 이 구조가 최대 상환액 찾기가 편함

    if total <=M: # 만약 총합이 최대 예산보다 작다면 최대상환액은 더 커질수 있으니
        answer=mid # 일단 이렇게 주고
        left=mid+1 # 미드를 기준으로 왼쪽을 다 버리고 다시

    # 요청 총합이 최대 예산보다 크다면 최대 상환액은 작은 쪽으로 가야하니
    else:
        right=mid-1 # 오른쪽을 다 버림

print(answer)

