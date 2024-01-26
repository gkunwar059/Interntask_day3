# 4. Create a list. Append the names of your colleagues and friends to it.
# Has the id of the list changed? Sort the list. What is the first item on
# the list? What is the second item on the list?



list_name=['ramesh','amresh','dipesh']
print(id(list_name))
list_name.append('Ganesh')
list_name.append('Rohan')
print(list_name)
print(id(list_name))

list_name.sort()
print(list_name)
print(list_name[0])
print(list_name[1])
