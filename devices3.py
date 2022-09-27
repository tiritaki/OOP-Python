class MobilePhone:  # created mobile phone class

    def __init__(self, phoneMake, phoneDesc, phoneModel, phonePrice):  # constructor

        # all the varaibles below are local to the class constructor

        # variables  make, description, model and price

        self.make = phoneMake  # make of phone

        self.description = phoneDesc

        self.model = phoneModel

        self.price = phonePrice



    # create a class method

    def discount(self):

        #calcDisc is a local variable to the class method

        calcDisc = self.price * 0.8

        print(f"The discounted price is {calcDisc}")
        
     # create an inner class

    class MobileStorage:

        def __init__(self, storageSize):

            self.memCard = storageSize
        
    # how do we access values held in the variables/variables  inside the MobilePhone class ?

myphone = MobilePhone(

    phoneMake="Test", phoneDesc="phone", phoneModel="my phone", phonePrice=1234

)



print(

    f" My phone 2 is {myphone.make} and {myphone.description}, model {myphone.model} and cost £{myphone.price}"

)




# how do we access the class method ?

# how do we access values held in the variables/variables inside the inner class MobileStorage?

"method 1"

# Create a new instance

phoneStorage1  = MobilePhone("HTC", "Cheap", "One", 234).MobileStorage("100GB")



print(f"The storage size is {phoneStorage1.memCard}")



"method 2"

# Create a new instance

phoneStorage2  = MobilePhone.MobileStorage("2TB")

print(f"The storage size is {phoneStorage2.memCard}")




"Method 3"

"use an existing class object"

test = myphone.MobileStorage("1PB")

print(f"Storage is{test.memCard}")