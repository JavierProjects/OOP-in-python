# Manager hereda de Admin y este de Employee

class Employee:
  new_id = 1

  def __init__(self):
    self.id = Employee.new_id
    Employee.new_id += 1

  def say_id(self):
    print(f"My id is {self.id}")

class Admin(Employee):
  def say_id(self):
    super().say_id()
    print("I'm an Admin")

class Manager(Admin):
  def say_id(self):
    print("I'm in charge")    
    super().say_id()
    

e1 = Employee()
e2 = Employee()

e3 = Admin()
e3.say_id()

e4 = Manager()
e4.say_id()

print(Admin.__bases__)
print(NameError.__bases__)