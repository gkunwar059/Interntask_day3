
# 19. Write a Python class to find validity of a string of parentheses, '(',
# ')', '{', '}', '[' and ']. These brackets must be close in the correct order,
# for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid.


class ValidParentheses:
    def __init__(self, str1):
        self.str1 = str1

     # main logic here 
    def is_valid(self):
        stack = []
        opening_brackets = ['(', '{', '[']
        closing_brackets = [')', '}', ']']
        matching_brackets = {')': '(', '}': '{', ']': '['}

        for char in self.str1:
            if char in opening_brackets:
                stack.append(char)


            elif char in closing_brackets:
                if len(stack) == 0 or matching_brackets[char] != stack.pop():
                    return False
                
        return len(stack) == 0

# Test
validator = ValidParentheses("(){}[]")
print(validator.is_valid()) 

validator = ValidParentheses("()[{)}")
print(validator.is_valid()) 

validator = ValidParentheses("()")
print(validator.is_valid()) 
