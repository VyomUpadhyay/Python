t1 = (11, 22, 33, 44, 33, 22, 33)
list = list(t1)
value = int(input("Enter the value -> "))
index = list.index(value) + 1
t1 = tuple(list)
print("The index of the value is", index )