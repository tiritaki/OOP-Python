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
        # calcDisc is a local variable to the class method
        calcDisc = self.price * 0.8
        print(f"The discounted price is {calcDisc}")

    # create an inner class
    class MobileStorage:
        def __init__(self, storageSize):
            self.memCard = storageSize


# create a child class/sub class (inherittance)
"method 1"


class MobileCPU(MobilePhone):  # passed in the class MobilePhone
    # passed in the class MobilePhone  parameters
    def __init__(
        self, phoneCPU, phoneMake, phoneDesc, phoneModel, phonePrice
    ):  # MobileCPU construtor
        # import the parent class constructor
        MobilePhone.__init__(self, phoneMake, phoneDesc, phoneModel, phonePrice)
        self.processor = phoneCPU


# create a child class/sub class (inherittance)
"method 2"


class MobileSize(MobilePhone):
    def __init__(self, phoneSize, phoneMake, phoneDesc, phoneModel, phonePrice):
        super().__init__(phoneMake, phoneDesc, phoneModel, phonePrice)
        self.screenSize = phoneSize


# Exercise access the child classes

 
myCPU = MobileCPU("Silicom", "Sumbsung", "Big", "x10", 34)
print(f'my phone cpu is {myCPU.processor}, description {myCPU.description}')