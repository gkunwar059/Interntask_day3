# 12. Create a function, is_palindrome, to determine if a supplied word is
# the same if the letters are reversed.



def is_palindrome(s):
    return s==s[::-1]
# compare == 
# [::-1] reverse the string 
# s string is compared to the reverse string if reverse string is equal to the string it becomes the palindrome

s="ama"
# string 
answer=is_palindrome(s)


print(answer)

if answer :
    print("Answer is palindrome !")
else:
    print("This is not palindrome !")