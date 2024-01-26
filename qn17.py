# 17. Write a program that serves as a basic calculator. It asks for two
# numbers, then it asks for an operator. Gracefully deal with input that
# doesn't cleanly convert to numbers. Deal with division by zero errors.


number_one=int(input("Enter First Number"))
operator=input("Enter the operator(+,-,/,%,)")
number_two=int(input("Enter Second Number"))

try:
    if operator=='+':
        print("The result is ",number_one + number_two)
    
    elif operator=='-':
        print("The result is ",number_one-number_two)

    elif operator=='*':
        print("The result is :",number_one*number_two)

    elif operator=='%':
        print("The result is :",number_one%number_two)

    elif operator=='/':
        if number_two==0:
            raise Exception(" number cannot be divided by the zero")
            
        else:
            print("The result is :",number_one/number_two)
    else:
        print("Enter the valid numbers")
    

except Exception as e:
    print(e)
        

# need more generic to the users