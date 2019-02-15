from acme import Product
from random import randint, sample, uniform


ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    products = []
    for _ in range(num_products):
        name = sample(ADJECTIVES, 1)[0] + ' ' + sample(NOUNS, 1)[0]
        price = randint(5, 100)
        weight = randint(5, 100)
        flammability = uniform(0.0, 2.5)
        products.append(Product(name, price=price, weight=weight,
                                flammability=flammability))
    return products


def inventory_report(products):
    print("ACME CORPORATION OFFICIAL INVENTORY REPORT")
    names = []
    prices = []
    weights = []
    flammabilities = []
    for i in products:
        names.append(i.name)
        prices.append(i.price)
        weights.append(i.weight)
        flammabilities.append(i.flammability)
    print("Unique product names:", len(names))
    print('Average price:', sum(prices)/len(prices))
    print('Average weight:', sum(weights)/len(weights))
    print('Average flammability:', sum(flammabilities)/len(flammabilities))


if __name__ == '__main__':
    inventory_report(generate_products())
