# 18. Find a package in the Python standard library for dealing with
# JSON. Import the library module and inspect the attributes of the
# module. Use the help function to learn more about how to use the
# module. Serialize a dictionary mapping 'name' to your name and 'age'
# to your age, to a JSON string. Deserialize the JSON back into
# Python.


import json

# Define a dictionary
data = {"name": "John", "age": 30}

# Convert the dictionary to a JSON string
json_data = json.dumps(data)

# dump to string -> dumps 
print(json_data)

# Convert the JSON string back to a Python dictionary
python_data = json.loads(json_data)
# load the string ->loads
print(python_data)




# import json

# data={"Name":"GAnesh","contact number":981022766,"age":12}

# json_data=json.dumps(data)
# print(json_data)

# deserialize_data=json.loads(json_data)
# print(deserialize_data)


