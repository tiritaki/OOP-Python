class Person():
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
    def multage(self, num1):
        multiplication = self.age*num1
        print(f"this is age {self.age} multiplyed by {num1} {multiplication}")
    
class Kid (Person):
    def __init__(self, color, name, surname, age):
        Person.__init__(self, name, surname, age)
        self.color = color
    def sleep (self, hour):
        self.hour = hour
        print(f"The kid goes to sleep at {hour} hour")

person = Kid (
    name = input('pls enter Kid name'),
    surname = input('pls enter Kid surname'),
    age = int(input("pls enter Kid age")),
    color = (input("pls enter Kid hair color"))
)
person.sleep(21)

print (f"Kid name is {person.name} and surname is {person.surname} and his age is {person.age} and his hair color is {person.color}")


