class Animal:
    def num_legs(self):
        return 4

    def walk(self):
        print('Walking ... ')


class Dog(Animal):
    def __init__(self, name):
        self.name = name


class Monkey(Animal):
    def __init__(self, name):
        self.name = name

    def num_legs(self):
        return 2

a = Animal()
print(a.num_legs())  #not all animals have 4 legs

d = Dog('sara')
print(d.num_legs())  #uses inhereted method

m = Monkey('monkey')
print(m.num_legs())  #uses Monkey method
