file = open("dosya.txt", "a")

file.write("Omer Faruk Balli\n")

file.write("Omer Faruk Balli\n")

file.write("Omer Faruk Balli\n")

file.write("Omer Faruk Balli\n")

file.close()


"""
file = open("dosya.txt", "w")
file.write("Omer Faruk Balli\n")
file.close()
"""

file = open("dosya.txt", "r")


for i in file:
    print(i)

veri = file.read()
print(veri)

file.close()