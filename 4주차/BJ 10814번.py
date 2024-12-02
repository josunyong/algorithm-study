# BJ 10814번 나이순 정렬


N=int(input())

result=[]

for _ in range(N):
    age,name=input().split() #
    result.append((int(age),name)) # 튜플로 나이, 이름 값을 넣음
    
# 처음에 리스트의 첫 원소로 헤보려고 result.sort(key=result[0]) 이런 식으로 접근해봤는데 안됨
result.sort(key=lambda x:x[0]) #람다식을 이용해서 첫번째 원소(나이)를 key값으로 정렬

for age, name in result:
    print(age,name) 