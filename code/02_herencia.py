# Tenemos 2 clases Dog Y Cat:

# class Dog:

#   def bark(self):
#     print('Woof!')

# class Cat:

#   def meow(self):
#     print('Meow!')

# Ahora queremos agregar el metodo eat a ambas clases.
# Para esto:
#   1. Creamos una clase Animal con el metodo eat.
#   2. Las clases Dog y Cat heredan el metodo eat de la clase Animal. 
    # class ParentClass:
    #   #class methods/properties...

    # class ChildClass(ParentClass):
    #   #class methods/properties...

class Animal:
  def eat(self):
    print("Nom Nom Nom...eating food!")

class Dog(Animal):
  def bark(self):
    print('Woof!')

class Cat(Animal):
  def meow(self):
    print('Meow!')    

Jack = Dog()    
Miau = Cat()

Jack.bark()
Jack.eat()

Miau.meow()
Miau.eat()