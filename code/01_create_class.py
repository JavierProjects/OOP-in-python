# 
# Crear una clase Employee
# Cada instancia de Employee tiene un id unico
# El método say_id imprime el id de Employee.

class Employee:
  new_id = 1

  def __init__(self):
    self.id = Employee.new_id
    Employee.new_id += 1

  def say_id(self):
    print(f"My id is {self.id}")

e1 = Employee()    
e2 = Employee()    

e1.say_id()
e2.say_id()