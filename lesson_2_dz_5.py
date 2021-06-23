prices = [27.8, 57.8, 46, 51, 63.03, 98, 13.52, 24, 81.5, 22.96, 14, 40.56, 80.03]
for price in prices:
    total_pennies = int(price * 100 + 0.501)
    rubles, pennies = divmod(total_pennies, 100)
    print(f'{rubles}руб {pennies:02}коп', end=", ")
print('\nid"prices":', (id(prices)))
print()
prices.sort()
print(id(prices))
print(prices)
print()
prices_s = sorted(prices, reverse=True)
print(id(prices_s))
print(prices_s)

