# 7. Create a list of tuples of first name, last name, and age for your
# friends and colleagues. If you don't know the age, put in None.
# Calculate the average age, skipping over any None values. Print out
# each name, followed by old or young if they are above or below the
# average age.


people=[('Ganesh','Kunwar',29),('Ramesh','Khadka',None),('Abishek','yadhav',26)]


# filter out the none values and calculate the average age
ages=[age for _,_, age in people if age is not None]
average_age=sum(ages)/len(ages)


#print each person's name and wheather they are above or below the average age

for first_name,last_name,age in people:
    if age is not None:
        print(f"{first_name}{last_name} is {'old' if age>average_age else 'Young'}")
