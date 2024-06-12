# Cat y Dog heredaron propiedades y metodos de Animal
# La clase Cat sobre anulo el metodo make_noise 

class Animal:
  def __init__(self, name):
    self.name = name

  def eat(self):
    print("Nom Nom Nom...eating food!")  

  def make_noise(self):
    print("{} says, Grrrr".format(self.name))
  

class Dog(Animal):
  def bark(self):
    print('Woof!')

class Cat(Animal):
  def meow(self):
    print('Meow!')    
  def make_noise(self):
    print("{} says, Meow because I'm a cat".format(self.name))

Firulais = Dog("Firulais")    
Minimo = Cat("Minimo")

Firulais.bark()
Firulais.eat()
Firulais.make_noise()

Minimo.meow()
Minimo.eat()
Minimo.make_noise()