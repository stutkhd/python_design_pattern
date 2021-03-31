def main():
    cow_factory = Factory(Cow)
    cow_factory.check_animal()

    chiken_factory = Factory(Chicken)
    chiken_factory.check_animal()

class Factory:
    def __init__(self, animal_class):
        self.animal = animal_class()

    def check_animal(self):
        self.animal.eat()
        self.animal.speak()

# Animalを継承しなくなった
class Cow:
    def eat(self):
        print('Cow:eat')

    def speak(self):
        print('Cow:speak')

# 同じく継承しない
class Chicken:
    def eat(self):
        print('Chicken:eat')

    def speak(self):
        print('Chicken:speak')

if __name__ == '__main__':
    main()