def calculate_discounted_price(price: float, discount: float) -> float:
    return price - (price * discount/100)


print(calculate_discounted_price(1000,20))