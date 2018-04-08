from abc import ABCMeta, abstractmethod  #ABC = Abstract Base Class

class Animal(metaclass=ABCMeta):
    def walk(self):
        pass

    @abstractmethod
    def num_legs(self):
        pass


class Dog(Animal):
    def __init__(self, name):
        self.name = name
    def walk(self):
        print('Dog is Walking ... ')

    def num_legs(self):
        return 4


class Monkey(Animal):
    def __init__(self, name):
        self.name = name

    def walk(self):
        print('Monkey is Walking ... ')

    def num_legs(self):
        return 2

#Animal is now an abstract class, you can't instantial a new class any more

d = Dog('Sara')
print('{} has {} legs'.format(d.name, d.num_legs()))  #implemented the abstract method
d.walk()       #implemented the abstract method

m = Monkey('Silly')
print('{} has {} legs'.format(m.name, m.num_legs()))  #implemented the abstract method
m.walk()        #implemented the abstract method

animals = [Dog('Doggy'), Monkey('Babbon')]
for a in animals:
    print(isinstance(a, Animal), type(a))
    print(a.num_legs())