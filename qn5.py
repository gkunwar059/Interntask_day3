
# 5. Create a tuple with your first name, last name, and age. Create a list,
# people, and append your tuple to it. Make more tuples with the
# corresponding information from your friends and append them to the
# list. Sort the list. When you learn about sort method, you can use the
# key parameter to sort by any field in the tuple, first name, last name,
# or age.

people=[]
tuple1=('Ganesh','kunwar',26)
tuple2=('Rohan','prajuli',21)
tuple3=('ramesh','yadhav',33)

people.append(tuple1)
people.append(tuple2)
people.append(tuple3)
print(people)

# sort the method using sorted  
first_name=sorted(people,key=lambda x:x[0])
print(first_name)
last_name=sorted(people,key=lambda x:x[1])
print(last_name)
age=sorted(people,key=lambda x:x[2])
print(age)



