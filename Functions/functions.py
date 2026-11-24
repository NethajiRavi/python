class TypeFunction:

  def myFun(self):
    print("HI")

  def withArguments(self,value):
    print(value)    

  def withReturnValues(self,values):
    return values*12  

  def withArgsAndKwargs(self,*args,**kwargs):
    
    # agrgs
    for arg in args:
      print(arg)

    # kwArgs
    for key, value in kwargs.items():
      print(f"key {key}, value {value}")


if __name__ == "__main__":
  myfun = TypeFunction()
  myfun.myFun()
  myfun.withArguments(12)
  myfun.withReturnValues(10)
  myfun.withArgsAndKwargs("as","ad",name="John", age=25)

  # List Comprehensions 

  func = [lambda arg=x: arg * 10 for x in range(1, 5)]

  for f in func:
    print(f())




