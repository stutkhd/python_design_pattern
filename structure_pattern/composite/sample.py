import abc
import sys

# Component
class AbstractItem(metaclass=abc.ABCMeta):
    @abc.abstractproperty
    def composite(self):
        pass

    def __iter__(self):
        return iter([])

# Leaf
class SimpleItem(AbstractItem):

    def __init__(self, name, price=0.00):
        self.name = name
        self.price = price
    
    def print(self, indent='', file=sys.stdout):
        print('{}${:.2f} {}'.format(indent, self.prince, self.name), file=file)

    @property
    def composite(self):
        return False

# Composite
class AbstractCompositeItem(AbstractItem):
    def __init__(self, *items):
        self.children = []
        if items:
            self.add(*items)

    def add(self, first, *items):
        self.children.append(first)
        if items:
            self.children.extend(items)

    def remove(self, item):
        self.children.remove(item)

    def __iter__(self):
        return iter(self.children)

# (Composite)
class CompositeItem(AbstractItem):
    def __init__(self, name, *items):
        super().__init__(*items)

    def print(self, indent="", file=sys.stdout):
        print("{}${:.2f} {}".format(indent, self.price, self.name))
        for child in self:
            child.print(indent + " ")

    @property
    def composite(self):
        return True

    @property
    def price(self):
        return sum(item.price for item in self)
