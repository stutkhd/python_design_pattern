amount_dict = {'high': 1.2, 'normal': 1.0, 'low': 0.8}

def main():
    factorya = AbstractPizzaFactory(PizzaFactoryA())
    pizza1 = factorya.make_pizza('high')
    print(pizza1)
    pizza1.check_pizza()

    print('-----------')

    factoryb = AbstractPizzaFactory(PizzaFactoryB())
    pizza2 = factoryb.make_pizza('normal')
    pizza2.check_pizza()

# Abstract Factory
class AbstractPizzaFactory:
    def __init__(self, pizza_factory, amount_str='normal'):
        self.factory = pizza_factory

    def make_pizza(self, amount_str):
        amount = amount_dict[amount_str]
        self.pizza_materials = []
        self.pizza_materials.append(self.factory.add_dough(amount))
        self.pizza_materials.append(self.factory.add_source(amount))
        self.pizza_materials.append(self.factory.add_topping(amount))
        return self # クラスオブジェクトを返さないとNoneTypeになってcheckが実行できない

    def check_pizza(self):
        for pizza_materials in self.pizza_materials:
            pizza_materials.check()

    # create product
    def add_dough(self, amount=1):
        pass

    # create product
    def add_source(self, amount=1):
        pass

    # create product
    def add_topping(self, amount=1):
        pass

# Concrete Factory
class PizzaFactoryA(AbstractPizzaFactory):
    def __init__(self):
        pass

    # create product
    def add_dough(self, amount=1):
        return WheatDough(amount)

    # create product
    def add_source(self, amount=1):
        return TomatoSource(amount)

    # create product
    def add_topping(self, amount=1):
        return CoanTopping(amount)

# ConcreteFactory
class PizzaFactoryB(AbstractPizzaFactory):
    def __init__(self):
        pass

    # createproduct
    def add_dough(self, amount=1):
        return RiceFlourDough(amount)

    # createproduct
    def add_source(self, amount=1):
        return BasilSource(amount)

    # createproduct
    def add_topping(self, amount=1):
        return CheeseTopping(amount)

# この場合は__init__は共通のため、子クラスでは__init__しない
# Abstract Product
class Dough:
    def __init__(self, amount):
        self.amount = amount

    def check(self):
        pass

# Concrete Product
class WheatDough(Dough):
    def check(self):
        print(f'Wheat(amount:{self.amount})')

# Concrete Product
class RiceFlourDough(Dough):
    def check(self):
        print(f'FlourDough(amount:{self.amount})')

# Abstract Product
class Source:
    def __init__(self, amount):
        self.amount = amount

    def check(self):
        pass

# Concrete Product
class TomatoSource(Source):
    def check(self):
        print(f"Tomato(amount: {self.amount})")

# Concrete Product
class BasilSource(Source):
    def check(self):
        print(f'Basil(amount:{self.amount})')

# Abstract Product
class Topping(Source):
    def __init__(self, amount):
        self.amount = amount

    def check(self):
        pass

# Concrete Product
class CoanTopping(Topping):
    def check(self):
        print(f'Coan(amount: {self.amount})')

# Concrete Product
class CheeseTopping(Topping):
    def check(self):
        print(f'Cheese(amount: {self.amount})')

if __name__ == '__main__':
    main()