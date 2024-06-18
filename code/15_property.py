class Box:
  def __init__(self, weight):
    self.__weight = weight

  def getWeight(self):
    return self.__weight
 
  def setWeight(self, weight):
    if weight >= 0:
      self.__weight = weight

  def delWeight(self):
    del self.__weight

  peso = property(getWeight, setWeight, delWeight, "Docstring for the 'weight' property")


box = Box(10)

print(box.peso) #this calls .getWeight()

box.peso = 5 #this called .setWeight()
print(box.peso) #this calls .getWeight()
del box.peso #this calls .delWeight()

box.peso = -5 #box.__weight is unchanged   
print(Box.peso.__doc__)