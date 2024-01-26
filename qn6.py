# 6. Create a list with the names of friends and colleagues. Search for the
# name ‘John’ using a for a loop. Print ‘not found’ if you didn't find it.



names=['Alica','john','max','Roy']
name='john'

# using for loop here
for item in names:
    if item==name:
        print("Name Found !")
        break

else:
    print("Not Found any name !")