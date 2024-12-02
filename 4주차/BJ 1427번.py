N=int(input())

list=list(map(int,str(N))) # 숫자를 문자열로 변환한 후, 각 자릿수를 정수로 리스트에 저장
 
list.sort(reverse=True) # 거꾸로 정렬해서

for i in list:
    print(i,end="") # 줄 바꿈 없이 출력