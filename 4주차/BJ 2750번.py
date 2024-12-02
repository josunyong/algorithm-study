# 수 정렬하기

N=int(input())

numbers=[]

for _ in range(N): # 첫줄에 입력받은 숫자만큼 
    numbers.append(int(input())) # 리스트에 넣고

numbers.sort() # .sort 이용해 바로 정렬

for i in numbers: # 정렬된 리스트 돌면서
    print(i) # 싹 다 출력

