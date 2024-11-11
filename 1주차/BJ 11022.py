T=int(input())

for i in range(1,T+1):
		# f-string 사용
    A,B=map(int,input().split())
    # 문자열 앞에 f 문자열 {변수i} : {입력받은 A} + {입력받은 B} = {입력받은 두 수의 합}
    print(f"Case #{i}: {A} + {B} = {A+B}") # f-string 사용