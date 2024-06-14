class Employee():
    def __init__(self):
        self.id = None # Public, access from everywhere
        # Write your code below
        self._id = 8 # Protected only access from the module
        self.__id = "ALexys" # Private only access from the class
        

e = Employee()
print(dir(e))