# The decorator @abstractmethod means that any class that inherits from Animal must implement a .say_id() method.
# ABC Abstract Base Class.

from abc import ABC, abstractmethod

class Animal(ABC):
  def __init__(self, name):
    self.name = name

  @abstractmethod  
  def make_noise(self):
    pass

class Cat(Animal):
  def make_noise(self):
    print("{} says, Meow!".format(self.name))

class Dog(Animal):
  def make_noise(self):
    print("{} says, Woof!".format(self.name))

kitty = Cat("Maisy")
doggy = Dog("Amber")
kitty.make_noise() # "Maisy says, Meow!"
doggy.make_noise() # "Amber says, Woof!"