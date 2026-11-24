class Dog :
  species = "canies"

  def __init__(self,name:str,age:int):
    self.name = name
    self.age = age



if __name__ == "__main__":

  dog = Dog("alpha",23)
  print(dog.name)
  print(dog.age)

