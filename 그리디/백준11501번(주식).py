import sys

# 3가지 행동
# 하나 사거나, 원하는 만큼 팔거나, 아무것도 X
# N일 -> 주가 N개, 1~N번을 3가지 행동 중 하나

# 첫날은 반드시 사고, 주가가 꺾이기 시작하기 전(고점)에 팔아
# 이득 => 매도 가격 - 매수 가격(매수 가격은 그때 마다 다를 수 있으니 다 더해주면 됨)



# 일단 매수 리스트를 하나 만들어서 산거를 거기에 넣고
# 고점을 만나면 매수 리스트가 빌 때까지 고점 - 매수 리스트.pop() 을 다 더해주는 식으로 접근

# 그럼 고점을 어떻게 찾나
# def action(list):
#     masulist=[] # 매수 리스트
#     gain=0 # 이득 값
#     여기보면 시간 복잡도가 O(N^2)
#     for i in list: # 받은 리스트에 있는걸 넣는데
#         masulist.append(i)
#         # 가장 고점 == 매도 시점
#         if masulist and i == max(list):
#             while masulist:
#                 buy_price=masulist.pop(0) # 고점 전 매수가 하나씩 꺼내서
#                 gain+=i-buy_price # 고점 - 매수가 를 더해가며 이득
#
#
#     return gain
#
#
#
# # sys도 생각은 해야함
# T=int(sys.stdin.readline().strip())
#
# # 입력받는 코드
# for _ in range(T):
#     N=int(sys.stdin.readline().strip())
#     price=list(map(int, sys.stdin.readline().split()))
#
#
# print(action(price))
# 시간초과로 틀림

# 정답 참조 -> 뒤에서 부터 접근하여 최고가를 갱신해가며 풀면 시간복잡도가 O(N)으로 줄어듦

def action(prices):
    max_price=0
    gain=0
    # 이러면 시간복잡도가 O(N)
    for i in range(len(prices)-1,-1,-1): # 거꾸로 탐색
        if prices[i]>max_price:
            max_price=prices[i] # 뒤에서부터 비교하며 최고가 갱신

        gain+=max_price-prices[i] # 최고가에서 현재가 이득 갱신

    return gain
# 나머진 동일
T = int(sys.stdin.readline().strip())

for _ in range(T):
    N = int(sys.stdin.readline().strip())
    price = list(map(int, sys.stdin.readline().split()))

    print(action(price))