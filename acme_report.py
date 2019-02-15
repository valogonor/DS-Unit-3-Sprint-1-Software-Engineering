from acme import Product
from random import randint, choice, uniform


adjectives = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
nouns = ['Anvil', 'Catapult' 'Disguise' 'Mousetrap', '???']


def generate_products(number_of_products=30):
    products = []
    for i in range(number_of_products):
        product = Product(name=choice(adjectives) + " " + choice(nouns),
                          price=randint(5, 100), weight=randint(5, 100),
                          flammability=uniform(0.0, 2.5))
        products.append(product)
    return products

def inventory_report(products):
    print("ACME CORPORATION OFFICIAL INVENTORY REPORT")
    names = []
    for i in products:
        names.append(i.name)
    print("Unique product names: ", len(names)


if __name__ == '__main__':
    inventory_report(generate_products())