# 14. Write a function that reads a CSV file. It should return a list of
# dictionaries, using the first row as key names, and each subsequent
# row as values for those keys.
# For the data in the previous example it would return:
# [{'name': 'George', 'address': '4312 Abbey Road', 'age': 22}, {'name':
# 'John', 'address': '54 Love Ave', 'age': 21}]


import csv

def read_csv(filename):
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        data = [row for row in reader]
    return data

# Test
data = read_csv('output.csv')
print(data)
