# Q. 다음과 같이 숫자로 이루어진 배열이 두 개가 있다. 
# 하나는 상품의 가격을 담은 배열이고, 하나는 쿠폰을 담은 배열이다. 
# 쿠폰의 할인율에 따라 상품의 가격을 할인 받을 수 있다. 
# 이 때, 최대한 할인을 많이 받는다면 얼마를 내야 하는가?

# 단, 할인쿠폰은 한 제품에 한 번씩만 적용 가능하다.

# [30000, 2000, 1500000] # 상품의 가격
# [20, 40]               # 쿠폰, 할인율의 단위는 % 입니다.

shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]


def get_max_discounted_price(prices, coupons):
    total_price = 0
    while len(prices) != 0:
        max_price = max(prices)
        print("max_price", max_price)
        prices.pop(prices.index(max_price))
        if len(coupons):
            max_coupon = max(coupons)
            coupons.pop(coupons.index(max_coupon))
        else:
            max_coupon = 0
        print("max_coupon", max_coupon)
        total_price += max_price * (1 - (max_coupon/100))
        print(total_price)
        

    return int(total_price)


print(get_max_discounted_price(shop_prices, user_coupons))  # 926000 이 나와야 합니다.