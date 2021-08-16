import heapq

ramen_stock = 4
supply_dates = [4, 10, 15]
supply_supplies = [20, 5, 10]
supply_recover_k = 30

# 1. 현재 재고의 상태에 따라 최고 값을 받아야 한다.(동적으로 변경되는 상태)
# 2. 제일 많은 값만 가져가면 된다.

# 1. 데이터를 넣을 때마다 최소, 최대 값을 동적으로 변경시키며
# 2. 최소, 최대 값을 바로 꺼낼 수 있는 자료구조는 바로 "heap"이다.

def get_minimum_count_of_overseas_supply(stock, dates, supplies, k):
    answer = 0
    # while stock < k: # stock이 k 값을 넘기면 함수를 바로 끝내도 상관 없음
    cur_day_index = 0   # 오늘이 며칠인지에 따라 supply에서 가져올 것이 달라지기 떄문에 설정
    supply_heap = []    # 현재 공급량이 떨어지지 않는 선에서 가장 많은 공급을 가져올 수 있는 자료구조 이용
    while stock < k:
        for dates_index in range(cur_day_index, len(dates)):    # 이런식으로 범위를 설정해주면, 이전 값을 신경쓰지 않아도 됨.
            # print(dates_index, supply_heap, stock)
            if dates[dates_index] <= stock:
                heapq.heappush(supply_heap, -supplies[dates_index])
            else:
                cur_day_index = dates_index
                break
        
        stock += -heapq.heappop(supply_heap)
        answer += 1
    return answer

print(get_minimum_count_of_overseas_supply(ramen_stock, supply_dates, supply_supplies, supply_recover_k))