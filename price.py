def discounted(price, discount, max_discount = 20):
    price = abs(price)
    discount = abs(discount)
    max_discount = abs(max_discount)
    if max_discount >= 100:
        raise ValueError('Максимальная скидка не должна превышать 100')
    if discount >= max_discount:
        price_with_discount = price
    else:
        price_with_discount = price - (price * discount / 100)
    return price_with_discount

#print(discounted(100, 5))
#print(discounted(100, 50))
#print(discounted(100, 50, max_discount=200))

def get_summ(one, two, delimiter='&'):
    return f'{str(one)}{delimiter}{str(two)}'.upper()

my_var = get_summ('Learn', 'Python')
#print(my_var)

def format_price(price):
    return f'Цена: {int(price)} руб.'

my_var2 = format_price(56.24)
print(my_var2)
