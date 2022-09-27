"A getter method gets the value of a property and setter method sets the value of a property"

# In OOP this helps to set the values of private attributes in a class

# Using setters and getters ensures data encapsulation


class Developer:

    def __init__(self, name, salary):

        self.name = name

        self.salary = salary

        # create getter methods

    def getName(self):

        return self.name  # return the value passed in the variable name


    def getPay(self):

        return self.salary  # return the value passed in the variable salary



    def getJob(self):

        return self.job  # return the value passed in the variable job



    # create a setter method

    def setJob(self):

        self.job = ""



    # how do we acces the class properties/variables  and their respective values

dev2 = Developer("Paulina", 103 )

print(f"{dev2.getName()} is paid {dev2.getPay()} as a developer")

