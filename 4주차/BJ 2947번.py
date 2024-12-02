# 나무조각
# 버블정렬 사용

anslst=list(map(int,input().split())) # 받은 숫자 공백으로 잘라서 리스트 삽입

for _ in range(len(anslst)-1): # 전체 돌기
    for i in range(len(anslst)-1): # 각 단계
        if anslst[i]>anslst[i+1]: # 앞에 원소가 뒤 원소보다 크면
            anslst[i],anslst[i+1]=anslst[i+1],anslst[i] # 둘이 자리 바꾸기
            print(*anslst) # 리스트 형식 말고 숫자만을 출력




