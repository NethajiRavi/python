class Employee:

  def __init__(self,name):
    self.name = name


  def show_name(self):
    return self.name


em = Employee("Moorthy")
print(em.show_name())

