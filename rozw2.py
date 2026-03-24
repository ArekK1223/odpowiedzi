cart = ['Jabłka', 'Banany']


def add_to_cart_pure(current_cart, item):
    return current_cart + [item] 

updated_cart = add_to_cart_pure(cart, 'Pomarańcze')

print("Oryginalny koszyk:", cart)               
print("Zaktualizowany koszyk:", updated_cart)   