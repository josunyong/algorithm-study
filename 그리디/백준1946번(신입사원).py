# 둘 다 다른 지원자들에 비해 떨어지면 탈락
# 서류, 면접 형태를 튜플로 입력받음
# 우선 서류순으로 정렬한 뒤 면접 등수를 비교해가며 낮은 사람은 탈락


# 시간초과떠서 입출력 sys 사용
import sys


def passed(list):
    max_score=list[0][1] # 첫번째를 일단 가장 높은 등수로 잡고
    count=1 # 그 첫번째는 반드시 합격이라두고

    # 처음에 11501번 처럼 뒤에서 접근했다가 틀림
    for i in range(1,len(list)): # 다시 앞에서부터 접근

        # 첫번째 튜플의 면접등수보다 낮다면
        if list[i][1]<max_score:
            # 합격생+1
            count+=1
            # 변수명은 score지만 등수니까 올라갈수록 점점 더 작아지는 구조 -> 등수 갱신
            max_score=list[i][1]


    # 서류는 오름차순, 면접은 내림차순
    return count


T=int(sys.stdin.readline())

for _ in range(T):
    N=int(sys.stdin.readline())
    # 반복만큼 튜플 한 쌍을 받아서 그걸 리스트에 넣음
    applicants=[tuple(map(int,sys.stdin.readline().split())) for _ in range(N)]

    # 첫번째(서류등수)를 기준으로 정렬
    applicants.sort()

    print(passed(applicants))

