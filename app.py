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
import math, time, threading
from decimal import Decimal, getcontext

print("hello world")
first_name = "chris"
one = 1
print(type(first_name))
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

cat_name = "my name is fuzzlekins"
print(cat_name[0])
print(cat_name[:7])
print(cat_name[5:])
print(len(cat_name))
print(f'number is {4}') # prior to python 3.6, you had use string.format()
print('Pi is {}'.format(math.pi))

print(bytes(4))
print(bytes('😃', 'utf-8'))
print(bytes('😃', 'utf-8').decode('utf-8'))

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print([2*item for item in mylist]) # list comprehension

def perform_op(num1, num2, op):
    if op == 'sum':
        return num1 + num2
    if op == 'multiply':
        return num1 * num2

print(perform_op(1, 2, 'multiply')) # keyword args must come after positional args, and can be in any order
print(perform_op(op='sum', num2=3, num1=4))

def many_args(*args): # can use an asterisk for 1 or more args for positional arguments (not keyword args)
    return args # this is a tuple

print(many_args(1, 2, 3))

def key_word_args(**kwargs): # use for keyword args
    return kwargs # this is a dictionary

print(key_word_args(key='val', anotherkey='anotherVal'))

print((lambda x: x + 3)(5))

class Person:
    company = "Best IT Services" # this is a static variable
    _years_in_biz = 19 # this is a private static variable
    def __init__(self, name, age, dept):
        self.name = name
        self.age = age
        self.dept = dept

    def get_years_in_biz(self):
        return self._years_in_biz

    def some_static_method():
        return "static method"

person1 = Person("Chris", 34, "IT")
print(person1.name)
print(person1.get_years_in_biz()) # self is inferred from the object call (refers to person1)
print(Person.company)
print(Person.get_years_in_biz(person1)) # need to pass in an object here
print(Person.some_static_method())

class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "woof"

    def run(self):
        return "I am running dog"

class Chihuahua(Dog): # inheritance
    def speak(self):
        return "yap"

    def move(self):
        return super().run() # get instance of parent class

dog = Chihuahua("Carlos")
print(dog.speak())
print(dog.move())

def excption_handling():
    start = time.time()
    try:
        answer = 2/1
        print(f"this answer is {answer}")
    except Exception as e:
        print(type(e))
    finally:
        print(f"this took {time.time() - start} seconds to execute")

excption_handling()

# raise exception
def raise_error(n):
    if n == 0:
        raise Exception()
    print(n)

try:
    raise_error(0)
except Exception as e:
    print(f"an exception of type {type(e)} occurred")

# custom exception
class CustomException(Exception):
    pass

# def cause_error():
#     raise CustomException("Called cause_error function")
#
# cause_error()

# threads
results = {}
def long_square(num, results):
    time.sleep(1)
    results[num] = num**2

# [long_square(n, results) for n in range(10)]

# create threads
# t1 = threading.Thread(target=long_square, args=(1, results))
# t2 = threading.Thread(target=long_square, args=(1, results))

# start threads
# t1.start()
# t2.start()

# join threads
# t1.join()
# t2.join()
#
# print(results)

# typically add to list
# threads = [threading.Thread(target=long_square(n, results)) for n in range(0, 10)]
# [t.start() for t in threads]
# [t.join for t in threads]
# print(results)
