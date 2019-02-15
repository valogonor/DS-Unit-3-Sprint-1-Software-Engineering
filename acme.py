from random import randint


class Product:
    def __init__(self, name, price=10, weight=20,
                 flammability=0.5, identifier=randint(1000000, 9999999)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def stealability(self):
        ratio = self.price/self.weight
        if ratio < 0.5:
            ans = "Not so stealable..."
        elif ratio < 1.0:
            ans = "Kinda stealable."
        else:
            ans = "Very stealable!"
        return ans

    def explode(self):
        product = self.flammability * self.weight
        if product < 10:
            ans = "...fizzle."
        elif product < 50:
            ans = "...boom!"
        else:
            ans = "...BABOOM!!"
        return ans


class BoxingGlove(Product):
    def __init__(self, name, price=10, weight=10,
                 flammability=0.5, identifier=randint(1000000, 9999999)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def explode(self):
        return "...it's a glove."

    def punch(self):
        if self.weight < 5:
            ans = "That tickles"
        elif self.weight < 15:
            ans = "Hey that hurt!"
        else:
            ans = "OUCH!"
        return ans
