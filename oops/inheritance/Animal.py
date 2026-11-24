class Animal:

  def __init__(self,name:str):
    self.name = name

  def info(self):
    print("Name ",self.name)  

  def eat(self):
       print("eat foof")   


class Dog(Animal):
  def __init__(self, name,breed:str):
    super().__init__(name)   # calling the parent class method for initialising the values
    self.breed=breed

  def details(self):
        print(self.name, "is a", self.breed)  

  def eat(self):
     print("eat Non Veg")      


class inheritanceMain:
   dog = Dog("Buddy","Golden Retrival")
   dog.info()
   dog.details()
   dog.eat()

