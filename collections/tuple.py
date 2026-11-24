class tuplepy:

  def __init__(self):
    pass


if __name__ == "__main__":

  tu = ()
  print(type(tu))

  tup = ('Geeks', 'For')
  print(tup)

  li = [1, 2, 4, 5, 6]
  print(tuple(li))

  tup = tuple('Geeks')
  print(tup)


  tup = tuple("Geeks")
  print(tup[0])
  print(tup[1:4])  
  print(tup[:3])

#  unpacking
  tup = ("Geeks", "For", "Geeks")
  a, b, c = tup
  print(a)
  print(b)
  print(c)

# Concatenation 
  tup1 = (0, 1, 2, 3)
  tup2 = ('Geeks', 'For', 'Geeks')
  tup3 = tup1 + tup2
  print(tup3)

# slicing

  tup = tuple('GEEKSFORGEEKS')
  print(tup[1:])
  print(tup[::-1])
  print(tup[4:9])

  # deleting 

  # tup = (0, 1, 2, 3, 4)
  # del tup
  # print(tup)

  # Tuple Unpacking with Asterisk (*)

  tup = (1, 2, 3, 4, 5,6)
  a, *b, c = tup
  print(a) 
  print(b) 
  print(c)