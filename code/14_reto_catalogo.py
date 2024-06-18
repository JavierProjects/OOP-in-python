class School:
  def __init__(self, name, level, numberOfStudents):
    self.name = name
    self.level = level
    self.numberOfStudents = numberOfStudents

  def get_name(self):
    return self.name

  def get_level(self):
    return self.level

  def get_numberOfStudents(self):
    return self.numberOfStudents 

  def set_numberOfStudents(self, number):
    self.numberOfStudents = number

  def __repr__(self):
    return f'A {self.level} school named {self.name} with {self.numberOfStudents} students'

class PrimarySchool(School):
  def __init__(self, name, numberOfStudents, pickupPolicy):
    super().__init__(name, 'primary', numberOfStudents)
    self.pickupPolicy = pickupPolicy

  def get_pickupPolicy(self):
    return self.pickupPolicy

  def __repr__(self):
    return f"{super().__repr__()} and a pickup policy of {self.pickupPolicy}"
  
class MiddleSchool(School):
    def __init__(self, name, numberOfStudents):
        super().__init__(name, 'middle', numberOfStudents)  

class HighSchool(School):
  def __init__(self, name, numberOfStudents, sportsTeams):
    super().__init__(name, 'high', numberOfStudents)
    self.sportsTeams = sportsTeams

  def get_sportsTeams(self):
    return self.sportsTeams
  
  def __repr__(self):
    return f'{self.sportsTeams}'


# 'primary', 'middle', or 'high'
itsoeh = School("Itsoeh", "high", 100)  
itsoeh.set_numberOfStudents(77)  
print(itsoeh.get_name())
print(itsoeh.get_level())
print(itsoeh.get_numberOfStudents())
print(itsoeh)

upp = PrimarySchool("UPP", 100, "Pickup after 3pm")  

upp.set_numberOfStudents(33)  
print(upp.get_name())
print(upp.get_level())
print(upp.get_numberOfStudents())
print(upp)


utt = HighSchool("UTT", 100, ["Bulls", "Lobos"])  

utt.set_numberOfStudents(11)  
print(utt.get_name())
print(utt.get_level())
print(utt.get_numberOfStudents())
print(utt)

