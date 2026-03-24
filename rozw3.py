from functools import reduce

prices = [10, 20, 30.5, 15]

total_func = reduce(lambda acc, price: acc + price, prices)

print("Suma funkcyjna:", total_func) 