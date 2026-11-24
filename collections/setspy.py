class setpy:


  def __init__(self):
    pass



if __name__ == "__main__":

  s = {10, 50, 20}
  print(s)
  print(type(s))

  s = set(["a", "b", "c","c"])
  print(s)

  # a set cannot have duplicate values
  s = {"Geeks", "for", "Geeks"}
  print(s)

  # values of a set cannot be changed
  # s[1] = "Hello"
  # print(s)

  s = set(["a", "b", "c"])
  print("Normal Set:", s)
  
  fs = frozenset(["e", "f", "g"])
  print("Frozen Set:", fs)