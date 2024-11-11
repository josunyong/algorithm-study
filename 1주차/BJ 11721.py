N = input()  # 문자열로 받고

for i in range(0, len(N), 10):  # i가 10씩 증가해야하니까 뒤에 10
    # 작동구조 print(N[0:10]) 후 print(N[10:20] ---> 이런식으로 N의 길이만큼
    print(N[i:i + 10])  # 10개씩 끊어서 출력
