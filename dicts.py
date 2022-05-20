from pprint import pprint

product = {
    'name': 'iPhone 12',
    'stock': 24,
    'price': 65432.1
}

product['memory'] = 256

#print(product)
#print(product.get('name'))
#print(product.get('size', 0))
del product['stock']
#print(product)

phones = ['iPhone 12', 'Samsung Galaxy S21', 'Xiaomi Mi11']
product['recommended'] = phones
#pprint(product)

product['recommended'].append('iPhone 9')
#pprint(product)

stock = [
    {'name': 'iPhone 12 Plus', 'stock': 24, 'price': 65432.1, 
       'recomended': ['Samsung Galaxy S21', 'iPhone 12']},
    {'name': 'Samsung Galaxy S21', 'stock': 8, 'price': 50000.0, 'discount': 5000},
    {'name': 'Xiaomi Mi11', 'stock': 42, 'price': 38000.5}
]

stock[0]['recomended'].append('Xiaomi Mi11')
stock[2]['price'] -= 30000
#pprint(stock)

climate = {
    'city': 'Москва',
    'temperature': '20'
}

print(climate['city'])
climate['temperature'] = str(int(climate['temperature']) - 5)
pprint(climate)

print(climate.get('country'), 'Россия')
climate['date'] = '27.05.2019'
print(len(climate))