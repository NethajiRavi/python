class Dictionary:

  def __init__(self):
    pass


if __name__ == "__main__":
  data = { "name": "Jake", "age": 22 }
  print(data)   
  a = {"x": 1, "y": 2}
  print(a)
  
  b = dict(name="Sam", age=20)
  print(b)

  d = {"name": "Kat", "age": 21}
  print(d["name"])     # Access using key
  print(d.get("age"))

  d = {"name": "Sam"}
  d["age"] = 21        # Adding a new key-value pair
  d["name"] = "Alex"   # Updating an existing value
  print(d) 

  d = {"a": 1, "b": 2}
  val = d.pop("a")
  print(val)
  print(d)

  d = {"a": 1, "b": 2}
  print(d.popitem())

  d = {"a": 1, "b": 2}
  d.clear()
  print(d)

  d = {"a": 1, "b": 2}
  for key in d:
    print(key)

  d = {"a": 1, "b": 2}
  for value in d.values():
    print(value)  

  d = {"a": 1, "b": 2}
  for key, value in d.items():
    print(key, value)  

  d = {
    "student": {
        "name": "Sam",
        "age": 20
    }
}

print(d["student"]["name"])  