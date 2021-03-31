import abc

def main():
    cow = CowFactory()
    cow.check_animal()

    chiken = ChickenFactory()
    chiken.check_animal()

# Creator
class Factory:
    def __init__(self):
        self.animal = self.factory_method()

    # template_method
    def check_animal(self):
        self.animal.eat()
        self.animal.speak()

    @abc.abstractmethod
    def factory_method(self):
        pass

# Product
class Animal:
    @abc.abstractmethod
    def eat(self):
        pass

    @abc.abstractmethod
    def speak(self):
        pass

# ConcreteCreator
class CowFactory(Factory):
    def factory_method(self):
        return Cow()

# ConcreteCreator
class ChickenFactory(Factory):
    def factory_method(self):
        return Chicken()

# ConcreteProduct
class Cow(Animal):
    def eat(self):
        print('Cow:eat')

    def speak(self):
        print('Cow:speak')

# ConcreteProduct
class Chicken(Animal):
    def eat(self):
        print('Chicken:eat')

    def speak(self):
        print('Chicken:speak')

if __name__ == '__main__':
    main()