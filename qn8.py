# 8. Write a function, is_prime, that takes an integer and returns True if
# the number is prime and False if the number is not prime.


def is_prime(num):
    # function to check the prime number from the given range of numbers
    for i in range(2,num):
        # numbers starts from two and goes to the infinite number
        if num%2==0:
        # main logic here if it is not divided by the number  and reminder is 0 then it wont be the prime number 
            # prime number is only divisible itself and not divided by any other number
            return False
        
        # when number is divisible by any number they wont be the prime 
        
        else:
            return True
        
print(is_prime(4))