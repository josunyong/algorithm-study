# 오래된것부터 삭제 -> 큐 생각
# 큐 구조의 이중리스트로 접근했었음
# 추천횟수를 표현 불가 -> 정답참조(딕셔너리 사용)

from collections import deque

N = int(input())  # 사진틀 개수
M = int(input())  # 총 추천 횟수
recommand = list(map(int, input().split()))  # 추천받은 학생들

frame = deque()  # 사진틀 (학생 리스트)
votes = {}  # 추천 횟수 저장 딕셔너리

# 학생이 추천을 돌며
for student in recommand:
    # 그 학생 key값이 투표 딕셔너리에 있으면
    if student in votes:
        # 그 value값을 +1
        votes[student] += 1
    else:
        # 사진틀이 꽉 찼으면
        if len(frame) >= N:
            # 최솟값을 찾고
            min_vote = min(votes[student] for student in frame)

            # 학생번호를 다음 frame 리스트를 다 돌면서
            for s in frame:
                # 그 학생번호의 추천수가 가장 작다면
                if votes[s] == min_vote:
                    # 가장 오래된 학생 삭제
                    # remove(값), pop(index) -> 이거 틀렸었음

                    # 사진틀에서 삭제하고
                    frame.remove(s)
                    # 딕셔너리에서도 삭제 -> 추천횟수(value)를 날리기 위해서
                    del votes[s]
                    break  # 하나만 제거하면 되므로 바로 탈출

        # 학생을 추가할 때
        frame.append(student)
        # 추천수는 1부터
        votes[student] = 1

# 최종적으로 사진틀에 남아있는 학생들 정렬 후 출력
# 리스트 형태말고 값만 출력할려고 * 사용
print(*sorted(frame))
