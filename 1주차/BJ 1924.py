# 처음 틀린 답
import datetime  # 이 모듈도 참고함(아 날짜를 나타내는 모듈이 있었는데? 느낌이 들어서)

x, y = map(int, input().split())

try:
    date = datetime.date(2007, x, y)  # datetime.date(2007년, 월, 일)
    days = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    print(days[date.weekday()])  # 이 객체는 월요일:0 / 화요일: 1 ~~ 일요일 : 6
# 여기에 예외처리를 그냥 실패! 느낌으로 달아야할듯...? 뭐 올바르지 않은 값을 입력받을시 어케처리 ~ 이런게 없어서
# except:
# print("실패")

# ----------------------------------------------------------------------#
# 참조해서 푼 답
days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]  # 각 요일

month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # 각 월의 최대 일수

day = 0  # 이전까지의 일 수

m, d = map(int, input().split())  # 월/일 입력받는 함수

for i in range(m - 1):
    day += month[i]  # 이전 월까지의 총 일수 더하기

# 이렇게 해서 이전까지의 일수와 내가 입력한 일수 더해서 몇번째를 가야할지 알아냄
answer = (day + d) % 7  # 숫자는 결국 0~6사이로 돔 => days에 일~토까지만 반환 가능

print(days[answer])



