# create python virtual environment
# python3 -m venv .venv
#
# activate python virtual environment
# .venv/bin/activate
#
# leave python virtual environment
# deactivate
#
# freeze pip requirements
# pip freeze > requirements.txt
#
# install pip requirements
# pip install -r requirements.txt
#
# code begins here #
#
import math
from decimal import Decimal, getcontext

print("hello world")
name = "chris"
one = 1
print(type(name))
print(type(one))
someDictionary = { "key1": "value1", "key2": "value2" }
print(type(someDictionary))
someList = [ "oranges", "apples", "blueberries" ]
print(type(someList))
print("first item in the list is " + someList[0])
someTuple = ("Honda", "Mazda", "Tesla", 1, 3, {"key1": "value1"}) # tuple can't be modified
print(type(someTuple))
print("second item in the tuple is " + someTuple[1])
car1, car2, car3, num1, num2, anotherDictionary = someTuple
print("car 1 is " + car1)
print("num2 is " + str(num2))
print("the value of anotherDictionary['key1'] is " + anotherDictionary["key1"])
someSet = {"morning", "afternoon", "evening", "night"}
print(type(someSet))
print("morning" in someSet)
a = True
if a:
    print("a is true")
else:
    print("a is false")

def multiply_by_three(val):
    return val * 3

print(type(None))

class Cat:
    def __init__(self, name):
        self.name = name
        self.paws = 4

    def speak(self):
        print(self.name + " says meow")

my_cat = Cat("Fuzzlekins")
print(my_cat.speak())

print(int(8.999)) # python will round down to 8, use round function
print(round(14/3, 2))

getcontext().prec = 3
print(Decimal(1) / Decimal(3))

name = "my name is fuzzlekins"
print(name[0])
print(name[:7])
print(name[5:])
print(len(name))
print(f'number is {4}') # prior to python 3.6, you had use string.format()
print('Pi is {}'.format(math.pi))

print(bytes(4))
print(bytes('😃', 'utf-8'))
print(bytes('😃', 'utf-8').decode('utf-8'))
