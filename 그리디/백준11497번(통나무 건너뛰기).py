# 처음에 지그재그 배치를 구현했음
# 오른쪽 왼쪽 나누어서 인덱스 짝/홀마다 다르게 배치하도록
# 근데 NZEC 에러로 답 X

T=int(input())

for _ in range(T):

    N = int(input())
    array = list(map(int, input().split()))
    array.sort()
    height = 0

    # 지그재그 배치법의 원리를 가져온 구조

    # 중앙 숫자 기준으로 앞에 있는 숫자를 뺴야
    # 각 통나무들의 높이 차이가 최소가 됨

    # ex) N=5,
    # list  2, 4, 5, 7, 9
    # index 0, 1, 2, 3, 4
    # abs(list[i]-list[i-2])
    # |5-2|, |7-4|, |9-5|
    for i in range(2, N):
        height = max(height, abs(array[i] - array[i - 2]))

    print(height)


# 이렇게 표현해도 NZEC 오류 해결 X
# GPT랑 구글링에선 다 이렇게 푸는데 왜 뜨는지 모르겠음...