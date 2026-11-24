from abc import ABC ,abstractmethod

class Greet(ABC):
  @property
  @abstractmethod
  def say_hello(self):
    pass 



class English(Greet):
  @property
  def say_hello(self):
    return "hi"

if __name__ == "__main__":
  g = English()
  print(g.say_hello)  


