# Q. 배달의 민족 서버 개발자로 입사했다.
# 상점에서 현재 가능한 메뉴가 ["떡볶이", "만두", "오뎅", "사이다", "콜라"] 일 때, 유저가 ["오뎅", "콜라", "만두"] 를 주문했다.
# 그렇다면 현재 주문 가능한 상태인지 여부를 반환하시오.


# Tip : 배열 정렬하는 방법(python에서는 .sort()를 통해 배열을 정렬할 수 있다. )
# sort가 이 문제에서 필요한 이유?? 이진 탐색을 하기 위해
shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]


def is_available_to_order(menus, orders):
    menus.sort() # 정렬 (nlog n)의 시간 복잡도 소요
    for order in orders:
        if not find(menus, order):
            return False
    return True
            

def find(menus, order):
    n = len(menus)
    low = 0
    high = n-1

    while low <= high:
        mid = (low+high)//2 # 이진 탐색!
        if (menus[mid] == order):
            return True
        elif (menus[mid] > order): 
            high = mid - 1
        else:
            low = mid + 1
    return False


result = is_available_to_order(shop_menus, shop_orders)
print(result)