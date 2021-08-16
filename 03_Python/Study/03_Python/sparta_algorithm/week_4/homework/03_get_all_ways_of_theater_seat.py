# seat_count = 9
# vip_seat_array = [4, 7]


# def fibo_dynamic_programming(n, fibo_memo):
#     if n in fibo_memo:       # 그냥 fibo_memo[n]을 하게되면 해당 키가 없을 때 key error를 반환한다. 
#         # 따라서 .get()을 통해 판단하는 것이 좋다. 또는 n in fibo_memo로 해도 좋음.
#         return fibo_memo[n]
#     else:   # fibo_memo[n]이 없다면,
#         nth_fibo = fibo_dynamic_programming(n-1, fibo_memo) + fibo_dynamic_programming(n-2, fibo_memo)
#         fibo_memo[n] = nth_fibo
#         return fibo_memo[n]

# memo = {
#     1:1,
#     2:2
#     }
# def get_all_ways_of_theater_seat(total_count, fixed_seat_array):
#     final = 1
#     cur_seat = 0
#     for fixed_seat in fixed_seat_array:
#         fixed_seat_index = fixed_seat - 1
#         number = fibo_dynamic_programming(fixed_seat_index - cur_seat, memo)
#         final *= number
#         cur_seat = fixed_seat_index + 1
#     number = fibo_dynamic_programming(total_count - cur_seat, memo)
#     final *= number 
#     return final


# # 12가 출력되어야 합니다!
# print(get_all_ways_of_theater_seat(seat_count, vip_seat_array))

import heapq

example_heap = []
heapq.heappush(example_heap, 1)
heapq.heappush(example_heap, 5)
heapq.heappush(example_heap, 2)
heapq.heappush(example_heap, 7)

print(example_heap)

heapq.heappop(example_heap)
print(example_heap)