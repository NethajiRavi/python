class WhileLoops:

  def printNValues(self, num:int):
    n = num
    while(n>0):
      print(n)
      n-=1


  def exampleWhileWithOutBreak(self,num :int):
    while(num<0):
      num += 1
      print(num)
    else:
      print("NO BREAK")


if __name__ == "__main__":
  whileLoop = WhileLoops()
  whileLoop.printNValues(100)
  whileLoop.exampleWhileWithOutBreak(12)
