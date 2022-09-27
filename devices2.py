class MobilePhone:  # created mobile phone class
    def __init__(self, phoneMake, phoneDesc, phoneModel, phonePrice):  # constructor
        # all the varaibles below are local to the class constructor
        # variables  make, description, model and price
        self.make = phoneMake  # make of phone
        self.description = phoneDesc
        self.model = phoneModel
        self.price = phonePrice


# how do we access values held in the variables/variables  inside the MobilePhone class ?


argMake = input("Enter phone make: ")
argDesc = input("Enter phone Description: ")
argModel = input("Enter phone Model: ")
argPrice = float(input("Enter phone price: "))


# print(f" My phone is {argMake} and {argDesc}, model {argModel} and cost £{argPrice}")


myphone1 = MobilePhone(
    argMake, argDesc, argModel, argPrice
)  # create an an object from the MobilePhone class

print(
    f" My phone 1 is {myphone1.make} and {myphone1.description}, model {myphone1.model} and cost £{myphone1.price}"
)

myphone2 = MobilePhone(
    phoneMake="Test", phoneDesc="phone", phoneModel="my phone", phonePrice=1234
)

print(
    f" My phone 2 is {myphone2.make} and {myphone2.description}, model {myphone2.model} and cost £{myphone2.price}"
)


myphone3 = MobilePhone(
    input("Enter phone make: "),
    input("Enter phone Description: "),
    input("Enter phone Model: "),
    float(input("Enter phone price: ")),
)

print(
    f" My phone 3 is {myphone3.make} and {myphone3.description}, model {myphone3.model} and cost £{myphone3.price}"
)
