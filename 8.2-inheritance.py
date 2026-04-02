#### Inheritance In Python
'''Inheritance is a fundamental concept in Object-Oriented Programming (OOP) that allows a class to inherit attributes and methods from another class. This lesson covers single inheritance and multiple inheritance, demonstrating how to create and use them in Python.'''

## Inheritance (Single Inheritance)
## Parent class
class Car:
    def __init__(self,windows,doors,enginetype):
        self.windows=windows
        self.doors=doors
        self.enginetype=enginetype
    
    def drive(self):
        print(f"The person will drive the {self.enginetype} car ")

car1=Car(4,5,"petrol")
car1.drive()

class Tesla(Car):
    def __init__(self,windows,doors,enginetype,is_selfdriving):
        super().__init__(windows,doors,enginetype)
        self.is_selfdriving=is_selfdriving

    def selfdriving(self):
        print(f"Tesla supports self driving : {self.is_selfdriving}")

tesla1=Tesla(4,5,"electric",True)
tesla1.selfdriving()

tesla1.drive()

### Multiple Inheritance
## When a class inherits from more than one base class.
## Base class 1
class Animal:
    def __init__(self,name):
        self.name=name

    def speak(self):
        print("Subclass must implement this method")

## Base class 2
class Pet:
    def __init__(self, owner):
        self.owner = owner


##Derived class
class Dog(Animal,Pet):
    def __init__(self,name,owner):
        Animal.__init__(self,name)
        Pet.__init__(self,owner)

    def speak(self):
        return f"{self.name} say woof"
    

## Create an object
dog=Dog("Buddy","Krish")
print(dog.speak())
print(f"Owner:{dog.owner}")

#### Conclusion
'''Inheritance is a powerful feature in OOP that allows for code reuse and the creation of a more logical class structure. Single inheritance involves one base class, while multiple inheritance involves more than one base class. Understanding how to implement and use inheritance in Python will enable you to design more efficient and maintainable object-oriented programs.'''
