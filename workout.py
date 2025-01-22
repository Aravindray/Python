# Importing necessary modules
import math
import keyword


# Defining a custom exception
class CustomError(Exception):
    pass


# Function to demonstrate various keywords and built-ins
# Boolean values
a = True
b = False

# Conditional statements
if a and not b:
    print("a is True and b is False")

# Looping with for and while
for i in range(5):
    print(f"Loop iteration {i}")

count = 0
while count < 5:
    print(f"While loop count: {count}")
    count += 1

# Using try, except, finally
try:
    x = 1 / 0
except ZeroDivisionError as e:
    print(f"Caught an exception: {e}")
finally:
    print("This will always execute")

# Using with statement for file operations
with open("example.txt", "w") as file:
    file.write("Hello, world!")

# Defining and using a lambda function
square = lambda x: x * x
print(f"Square of 3 is {square(3)}")

# Using list comprehensions
squares = [x * x for x in range(10)]
print(f"Squares: {squares}")

# Using built-in functions
print(f"Absolute value of -5: {abs(-5)}")
print(f"All elements are true: {all([True, True, False])}")
print(f"Any element is true: {any([False, False, True])}")
print(f"Binary representation of 10: {bin(10)}")
print(f"Character for ASCII 97: {chr(97)}")
print(f"Divmod of 10 by 3: {divmod(10, 3)}")
print(f"Enumerate list: {list(enumerate(['a', 'b', 'c']))}")
print(f"Filter even numbers: {list(filter(lambda x: x % 2 == 0, range(10)))}")
print(f"Map squares: {list(map(lambda x: x * x, range(10)))}")
print(f"Max of [1, 2, 3]: {max([1, 2, 3])}")
print(f"Min of [1, 2, 3]: {min([1, 2, 3])}")
print(f"Sum of [1, 2, 3]: {sum([1, 2, 3])}")
print(f"Sorted list: {sorted([3, 1, 2])}")

# Using global and nonlocal
global_var = "I am global"


def outer_function():
    outer_var = "I am outer"

    def inner_function():
        nonlocal outer_var
        outer_var = "I am changed outer"
        print(outer_var)

    inner_function()
    print(outer_var)


outer_function()
print(global_var)

# Using assert
assert a == True, "a should be True"

# Using pass, break, continue
for i in range(10):
    if i == 5:
        continue
    if i == 8:
        break
    print(i)
else:
    pass

# Using del
my_list = [1, 2, 3]
del my_list[1]
print(my_list)


# Using yield in a generator
def generator_function():
    yield 1
    yield 2
    yield 3


for value in generator_function():
    print(value)

# Using isinstance and issubclass
print(isinstance(5, int))
print(issubclass(bool, int))

# Using exec to execute a string of code
exec("print('Hello from exec')")

# Using eval to evaluate a string as an expression
result = eval("5 + 5")
print(f"Result of eval: {result}")

# Using format for string formatting
formatted_string = "Hello, {}!".format("world")
print(formatted_string)

# Using frozenset
fs = frozenset([1, 2, 3])
print(fs)

# Using help to get documentation
help(print)

# Using id to get the identity of an object
print(f"ID of a: {id(a)}")


# This code demonstrates the use of various Python keywords, variables, classes, and functions.

print("Python Keywords:", keyword.kwlist)

# Variables
name = "Alice"  # String
age = 30  # Integer
height = 1.75  # Float
is_student = True  # Boolean
my_list = [1, 2, 3]  # List
my_tuple = (4, 5, 6)  # Tuple
my_set = {7, 8, 9}  # Set
my_dict = {"name": "Bob", "age": 25}  # Dictionary

# Data Types
print("Name:", type(name))
print("Age:", type(age))
print("Height:", type(height))
print("Is Student:", type(is_student))
print("List:", type(my_list))
print("Tuple:", type(my_tuple))
print("Set:", type(my_set))
print("Dictionary:", type(my_dict))

# Operators
result = 5 + 3  # Arithmetic
result = 10 - 2  # Arithmetic
result = 4 * 2  # Arithmetic
result = 8 / 2  # Arithmetic
result = 9 % 2  # Modulus
result = 2**3  # Exponent
result = 5 == 5  # Comparison
result = 3 < 10  # Comparison
result = True and False  # Logical
result = True or False  # Logical
result = not True  # Logical

# Control Flow
if age >= 18:
    print("Adult")
else:
    print("Minor")

for i in range(5):
    print(i)

while age > 0:
    age -= 1


# Functions
def greet(name):
    print("Hello,", name + "!")


greet("Alice")


# Classes
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print("My name is", self.name, "and I am", self.age, "years old.")


person1 = Person("Bob", 25)
person1.introduce()

# Exception Handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero")

print("Square root of 25:", math.sqrt(25))

# Input/Output
user_input = input("Enter your name: ")
print("Hello,", user_input)

# This code demonstrates a basic usage of many Python keywords, variables, data types, operators, control flow, functions, classes, and more.
# It's a starting point for exploring the vast capabilities of the Python language.


# Define a class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass


# Define a subclass
class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def speak(self):
        return "Woof!"


# Define a function
def example_function():
    # Using various keywords and variables
    try:
        animal = Animal("Generic Animal")
        dog = Dog("Buddy", 5)

        for i in range(3):
            if i == 2:
                print(dog.speak())
            else:
                print("Not yet!")
    except Exception as e:
        print(f"An error occurred: {e}")
    else:
        print("No errors occurred")
    finally:
        print("Execution finished")


# Main execution block
if __name__ == "__main__":
    example_function()

    # Using more keywords
    with open("output.txt", "w") as file:
        file.write("Example output\n")

    lambda_function = lambda x: x * 2
    print(lambda_function(10))

    # Using assert
    assert lambda_function(5) == 10, "Lambda function test failed"

# Example code containing all Python keywords, variables, classes, and functions

# Variables and literals
x = 10  # Assign integer
y = 3.14  # Assign float
z = True  # Assign boolean


# Function definition with def and return
def calculate_area(radius):
    """Calculate the area of a circle."""
    if radius <= 0:
        raise ValueError("Radius must be positive")  # raise, if, <=
    return math.pi * radius**2  # return, **


# A class with methods
class Shape:
    """A simple class representing shapes."""

    def __init__(self, name):  # class, def, self, __init__
        self.name = name  # self
        self.dimensions = []

    def add_dimension(self, dimension):  # Method definition
        """Add a dimension to the shape."""
        self.dimensions.append(dimension)

    def is_valid(self):  # is
        """Check if the shape has at least one dimension."""
        return bool(self.dimensions)  # bool()


# while, break, and continue example
def find_first_even(numbers):
    """Find the first even number in a list."""
    for number in numbers:  # for
        if number % 2 == 0:
            return number
        continue  # continue


# try, except, else, and finally example
def safe_divide(a, b):
    try:
        result = a / b  # try, /
    except ZeroDivisionError:  # except
        print("Cannot divide by zero!")
        return None
    else:  # else
        return result
    finally:  # finally
        print("Division attempt finished.")  # print()


# Lambda function
square = lambda x: x * x  # lambda

# with and as example (context manager)
with open("example.txt", "w") as file:
    file.write("This is an example.")  # with, as

# global and nonlocal
count = 0  # global variable


def increment_count():
    global count  # Use global keyword
    count += 1


def outer_function():
    n = 10  # Local variable

    def inner_function():
        nonlocal n  # Use nonlocal keyword
        n += 1
        return n

    return inner_function()


# assert and pass
def test_positive_number(num):
    assert num > 0, "Number must be positive!"  # assert
    pass  # pass


# del and None
a = [1, 2, 3]
del a[1]  # del
nothing = None  # None


# if, elif, else
def classify_number(num):
    if num < 0:  # if
        return "Negative"
    elif num == 0:  # elif
        return "Zero"
    else:  # else
        return "Positive"


# Examples demonstrating all keywords in action
if __name__ == "__main__":  # __name__, __main__
    shape = Shape("Circle")  # Instantiate a class
    shape.add_dimension(10)
    print("Shape is valid:", shape.is_valid())  # Function calls

    print("Area of circle:", calculate_area(5))
    print("First even number:", find_first_even([1, 3, 5, 6, 9]))
    print("Safe division:", safe_divide(10, 2))
    print("Incremented count:", increment_count())
    print("Classify number:", classify_number(-5))

    try:
        test_positive_number(-10)
    except AssertionError as e:
        print(e)
