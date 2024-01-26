# 10. Write a function that takes camel-cased strings (i.e.
# ThisIsCamelCased), and converts them to snake case (i.e.
# this_is_camel_cased). Modify the function by adding an argument,
# separator, so it will also convert to the kebab case
# (i.e.this-is-camel-case) as well.


import re

def camel_to_snake(camel_string,separator='_'):
    # find all capital letter in the string and replace them with the seperator followed by their lowercase  equivalent
    snake_string=re.sub(r'(?<=[a-z])(?=[A-Z])',separator,camel_string)

    # make first character of the string to lower
    snake_string=snake_string[0].lower() +snake_string[1:]

    return snake_string

# output 
print(camel_to_snake('this_is_snake_case'))
# output for kebab
print(camel_to_snake('ThisIsCamelCased'))   
