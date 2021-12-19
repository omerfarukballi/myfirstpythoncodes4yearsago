a = "Listeler Metodları"
liste = [1,2,3,4,5,6]
print(len(a)+len(liste))

print(a.startswith("List"))
print(a.endswith("ları"))

a = a.replace("ı","i")
print(a)


liste.append("Pyton")
print(liste)

liste.pop(0)
print(liste)
liste.pop()
print(liste)
