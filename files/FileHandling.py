
#  File Properties
f = open("asset/geek.txt", "r")
print("Filename:", f.name)
print("Mode:", f.mode)
print("Is Closed?", f.closed)

f.close()
print("Is Closed?", f.closed)


#  Read a File Contents
file = open("asset/geek.txt", "r")
content = file.read()
print(content)
file.close()


#  Write a File
with open("asset/geek.txt", "w") as file:
    file.write("Hello, Python!\n")
    file.write("File handling is easy with Python.\n")
    file.write("File handling is easy with Python.")

print("File written successfully")


try:
    with open("geek.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError as e:
    print("Error:", e)