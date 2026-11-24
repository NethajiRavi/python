
class Calculate:

  def getSum(self,num:int) -> int:
    sum:int = 0;
    for i in range(1,num):
      sum +=i
    return sum


  def printList(self,name:list):
    for i in name:
      print(i)

      #  range function

  def printEvenNum(self,num:int):
     for i in range(0,num,2):
        print(i)


  def exampleContinue(self):
    for i in 'geeksforgeeks':
      if i == 'e' or i == 's':
        continue
      print(i)

  def exampleBreak(self):
      for i in 'geeksforgeeks':
        if i == 'e' or i == 's':
          break
        print(i)  

  def examplePass(self):
        for i in 'geeksforgeeks':
          pass
        print(i) 

  def exampleEnumerated(self,values:list):
          for i,j in enumerate(values):
              print(i,j)                


if __name__ == "__main__":

  cal = Calculate()
  nameList = {"a","aa","aaaa","aaa"}
  cal.printList(nameList)
  print(cal.getSum(10)) 
  cal.printEvenNum(100)
  cal.exampleContinue()
  cal.exampleBreak()
  cal.examplePass()

  values = ["apple","orange","dog"]
  cal.exampleEnumerated(values)