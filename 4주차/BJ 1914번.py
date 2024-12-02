# BJ 1914번 하노이탑

def hanoi(n,a,b,c):
    if n==1:
        print(a,c)
    else:
        hanoi(n-1,a,c,b) #a->b
        hanoi(1,a,b,c) # a->c 
        hanoi(n-1,b,a,c) # b->c
 
n=int(input())
print(2**n-1) # 총 이동횟수


# 이 부분 아직
if(n<=20): 
    hanoi(n,1,2,3)