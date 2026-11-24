# class Employee:

#   def __init__(self,name,age):
#     self.name = name
#     self._age = age




# class subEmployee(Employee):
#   def show_age(self):
#         print("Age:", self._age)   


# em =  subEmployee("Moorthy",40)

# print(em.name)
# print(em._age)

class Employee:
    def __init__(self, name, age):
        self.name = name       # public
        self._age = age        # protected

class SubEmployee(Employee):
    def show_age(self):
        print("Age:", self._age)   # Accessible in subclass

emp = SubEmployee("Ross", 30)
print(emp.name) 
print(emp._age)        # Public accessible
emp.show_age()         # Protected accessed through subclass