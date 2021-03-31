amount_dict = {'high': 1.2, 'normal': 1.0, 'low': 0.8}

def main():
    pizza1 = make_pizza(PizzaFactoryA, 'high')
    pizza1.check_pizza()

    print('------')

    pizza2 = make_pizza(PizzaFactoryB, 'normal')
    pizza2.check_pizza()

def make_pizza(PizzaFactory, amount_str):
    pizza = PizzaFactory()
    amount = amount_dict[amount_str]
    pizza.pizza_materials = []
    pizza.pizza_materials.append(pizza.add_dough(amount))
    pizza.pizza_materials.append(pizza.add_source(amount))
    pizza.pizza_materials.append(pizza.add_topping(amount))
    return pizza

class PizzaFactoryA:
    def __init__(self):
        pass

    def check_pizza(self):
        for pizza_material in self.pizza_materials:
            pizza_material.check()

    @classmethod # clsはPizzaFactoryAが渡される
    def add_dough(cls, amount=1):
        return cls.WheatDough(amount) # PizzaFactoryAに在る内部クラスが参照

    @classmethod
    def add_source(cls, amount=1):
        return cls.TomatoSource(amount)

    @classmethod
    def add_topping(cls, amount=1):
        return cls.CoanTopping(amount)

    class WheatDough:
        def __init__(self, amount=1):
            self.amount = amount

        def check(self):
            print(f'Wheat(amount: {self.amount})')

    class TomatoSource:
        def __init__(self, amount=1):
            self.amount = amount

        def check(self):
            print(f'Tomato(amount: {self.amount})')

    class CoanTopping:
        def __init__(self, amount=1):
            self.amount = amount

        def check(self):
            print(f'Coan(amount: {self.amount})')

class PizzaFactoryB:
    def __init__(self):
        pass

    def check_pizza(self):
        for pizza_material in self.pizza_materials:
            pizza_material.check()

    @classmethod
    def add_dough(cls, amount=1):
        return cls.RiceFlourDough(amount)

    @classmethod
    def add_source(cls, amount=1):
        return cls.BasilSource(amount)

    @classmethod
    def add_topping(cls, amount=1):
        return cls.CheeseTopping(amount)

    class RiceFlourDough:
        def __init__(self, amount=1):
            self.amount = amount

        def check(self):
            print("FlourDough(amount: {})".format(self.amount))

    class BasilSource:
        def __init__(self, amount=1):
            self.amount = amount

        def check(self):
            print("Tomato(amount: {})".format(self.amount))

    class CheeseTopping:
        def __init__(self, amount=1):
            self.amount = amount

        def check(self):
            print("Cheese(amount: {})".format(self.amount))

if __name__ == '__main__':
    main()