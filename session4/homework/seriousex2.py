prices = {
    'banana':4,
    'apple':2,
    'orange':1.5,
    'pear':3
}
stock = {
    'banana': 6,
    'apple':0,
    'orange':32,
    'pear':15
}

for k in prices:
    print(k)
    print('price:', prices[k])
    print('stock:', stock[k],'\n')

total = 0
for k in prices:
    price = prices[k]*stock[k]
    print(k,':',price)
    total += price
print('If I sold all my food, I would make:', total)