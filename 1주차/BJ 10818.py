N=int(input())

numbers=list(map(int, input().split())) # 숫자 입력받아서 list에 다 넣고(max, min 쓸려고)

# 각각 max, min 매서드 사용해서 최대/최소값 가져오기
max_val=max(numbers)
min_val=min(numbers)

print(min_val, max_val)