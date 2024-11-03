list1 = ["Ganesh", "Salunkhe", 10, 23.45, 45]

#Print List
print(list1)

#Printing 3rd index of List
print(list1[3])

#Appending new item at last in list
list1.append("Swastika")
print(list1)
print(list1.index("Swastika"))

#Removing item from list
list1.remove("Salunkhe")
print(list1)


list2 = [100, 200, 300 , "Ganesh", "Salunkhe", 10, 23.45, 45]
#Fetch Range of index
print(list2[2:4])

#Fetch value from starting index 2 till end
print(list2[2:])

#Fetch value from starting index till 5th index
print(list2[ :5])

#Updating 5th index value
list2[5] = 50.55
print(list2)

list2.insert(3, "ABCD")
print(list2)