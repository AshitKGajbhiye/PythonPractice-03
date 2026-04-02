#### Decorators
'''Decorators are a powerful and flexible feature in Python that allows you to modify the behavior of a function or class method. They are commonly used to add functionality to functions or methods without modifying their actual code. This lesson covers the basics of decorators, including how to create and use them.'''

### function copy
### closures
### decorators

## function copy
def welcome():
    return "Welcome to the advanced python course"

welcome()

wel=welcome
print(wel())
del welcome
print(wel())

##closures functions

def main_welcome(msg):
   
    def sub_welcome_method():
        print("Welcome to the advance python course")
        print(msg)
        print("Please learn these concepts properly")
    return sub_welcome_method()

main_welcome("Welcome everyone")

def main_welcome(func):
   
    def sub_welcome_method():
        print("Welcome to the advance python course")
        func("Welcome everyone to this tutorial")
        print("Please learn these concepts properly")
    return sub_welcome_method()

def main_welcome(func,lst):
   
    def sub_welcome_method():
        print("Welcome to the advance python course")
        print(func(lst))
        print("Please learn these concepts properly")
    return sub_welcome_method()

main_welcome(len,[1,2,3,4,5])

len([1,2,3,4,5,6])

### Decorator
def main_welcome(func):
   
    def sub_welcome_method():
        print("Welcome to the advance python course")
        func()
        print("Please learn these concepts properly")
    return sub_welcome_method()

def coure_introduction():
    print("This is an advanced python course")

coure_introduction()

main_welcome(coure_introduction)

@main_welcome
def coure_introduction():
    print("This is an advanced python course")

## Decorator

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

## Decorators With arguments
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator


@repeat(3)
def say_hello():
    print("Hello")

say_hello()


#### Conclusion
'''Decorators are a powerful tool in Python for extending and modifying the behavior of functions and methods. They provide a clean and readable way to add functionality such as logging, timing, access control, and more without changing the original code. Understanding and using decorators effectively can significantly enhance your Python programming skills.'''
