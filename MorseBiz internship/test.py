fruits = ["apple", "mango"]

basket = iter(fruits)
print(next(basket))
print(next(basket))
print(next(basket, None))

