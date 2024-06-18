class Box:
 def __init__(self, weight):
   self.__weight = weight

 @property # getter
 def weight(self):
   """Docstring for the 'weight' property"""
   return self.__weight


 @weight.setter
 def weight(self, weight):
   if weight >= 0:
     self.__weight = weight

 @weight.deleter
 def weight(self):
   del self.__weight


box = Box(23)   
print(box.weight)

box.weight = 100
print(box.weight)

# del box.weight
print(Box.weight.__doc__)
