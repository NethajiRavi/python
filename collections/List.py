class ListClass:

  def __init__(self):
        pass

  def printList(self,listValues):
    for i in listValues:
      print(i)

if __name__ == "__main__":

  listObj = ListClass()
  listValue = [1,2,3,4,5,6]
  #  ordered
  listObj.printList(listValue)
  listValue.append(10)
  listObj.printList(listValue)
  listValue.extend([11,12,13,14,15])
  listObj.printList(listValue)

  listValue.insert(100,0)
  listObj.printList(listValue)




