"""To understand the meaning of classes we

have to understand the built-in __init__() function.

All classes have a function called __init__(), which is

 always executed when the class is being initiated.

 Use the __init__() function to assign values to object

 properties, or other operations that are necessary to do

 when the object is being created:"""
 
class MobilePhone: #created mobile phone class  
    def __init__(self): # constructor
    # all the varaibles are local to the class constructor
    # variables  make, description, model and price
        self.make = "Samsung"
        self.description = "Slim Build"
        self.model = "Galaxy S10+"
        self.price = 456.67
        
myphone13 = MobilePhone()
print(myphone13.make, myphone13.description, myphone13.price )

# create a new object with new values passed in to the respective variables

myphone2 = MobilePhone()
myphone2.make = "Apple"  #
myphone2.model = "XR"
myphone2.description = "IPS Display"
myphone2.price = 1234.89

print(myphone2.make)
print(myphone2.model)
print(myphone2.description)
print(myphone2.price)

# create a new object with new values passed in using the input function

myphone3 = MobilePhone()
myphone3.make = input("Enter phone make: ")
myphone3.model = input("Enter phone Model: ")
myphone3.description = input("Enter phone Description: ")
myphone3.price = float(input("Enter phone price: "))

print(f" My phone is {myphone3.make} and {myphone3.description}, model {myphone3.model} and cost £{myphone3.price}")