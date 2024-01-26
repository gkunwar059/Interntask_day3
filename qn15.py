# 15. Imagine you are designing a banking application. What would a
# customer look like? What attributes would she have? What methods
# would she have?

class Customer:
    def __init__(self, first_name, last_name, phone_number, pin):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.pin = pin

    def account_no(self):
        return f"{self.first_name}_{self.last_name}"

    def sms_banking(self):
        print("sms banking is done !")

    def mobile_banking(self):
        print("Mobile banking done !")

# Create a customer
customer = Customer("Ambika", "Kunwar", 9810228669, 2580)

# Call the methods
print(customer.account_no())
customer.sms_banking()
customer.mobile_banking()

