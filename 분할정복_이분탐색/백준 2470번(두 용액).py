# 두개를 합쳐 최대한 0에 가깝게

n=int(input())

arr=list(map(int,input().split()))

arr.sort()

left, right=0,n-1 # 각각 끝 점

answer=abs(arr[left]+arr[right]) # 양 끝값 더한 값
final=[arr[left],arr[right]] # 일단 최종 값은 당장 이거

while left<right: # 이분 탐색
    left_val=arr[left]
    right_val=arr[right]

    sum=left_val+right_val

    if abs(sum)<answer: # abs(sum)이 0이랑 더 가깝다는 소리
        answer=abs(sum)
        final=[left_val,right_val] # 그러므로 마지막 답을 갱신해주고
        if answer==0: # 딱 0이되면
            break # 반복문 종료
    if sum<0: # 만약 sum이 0보다 작으면 왼쪽 값을 키워야하므로 오른쪽으로 이동
        left+=1
    else: # sum이 0보다 크면 값을 오른쪽 값을 줄여야하므로 왼쪽으로 이동
        right-=1

print(final[0],final[1])