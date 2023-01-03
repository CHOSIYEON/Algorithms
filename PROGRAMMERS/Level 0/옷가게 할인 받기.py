def solution(price):
    if price < 100000:
        return price
    elif 100000 <= price < 300000:
        return int(price * 0.95)
    elif 300000 <= price < 500000:
        return int(price * 0.9)
    else:
        return int(price * 0.8)

###

def solution(price):
    discount_rates = {500000: 0.8, 300000: 0.9, 100000: 0.95, 0: 1}

    for discount_price, discount_rate in discount_rates.items():
        if price >= discount_price:
            return int(price * discount_rate)