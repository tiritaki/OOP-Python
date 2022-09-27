
class Person():
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
    def multage(self, num1):
        multiplication = self.age*num1
        print(f"this is age {self.age} multiplyed by {num1} {multiplication}")
    
    class Kid:
        def __init__(self, agi):
           self.agi = agi

person2 = Person (
    name = input('pls enter name'),
    surname = input('pls enter surname'),
    age = int(input("pls enter age"))
)
print (f"person 2 name is {person2.name} and surname is {person2.surname}")
person2.multage(5)

person3 = Person.Kid(5)
print(f"kid's age is {person3.agi}")
