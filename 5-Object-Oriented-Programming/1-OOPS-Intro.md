# What is Class & Object ?

A class is a logical grouping of data and methods. Instance of a class is called objects. Data and methods are called class attributes. Class functions are called methods. A class is a template or a blueprint of an object. An object can be anything which represent real world.

> [!quote] Object-Oriented Python by Irv Kalb
> To describe a physical object in our everyday world, we often reference its attributes. When talking about a desk, you might describe its color, dimensions, weight, material, and so on. Some objects have attributes that apply only to them and not others. A car could be described by its number of doors, but a shirt could not. A box could be sealed or open, empty or full, but those characteristics would not apply to a block of wood. Additionally, some objects are capable of performing actions. A car can go forward, back up, and turn left or right. To model a real-world object in code, we need to decide what data will represent that object’s attributes and what operations it can perform. These two concepts are often referred to as an object’s state and behavior, respectively: the state is the data that the object remembers, and the behaviors are the actions that the object can do.

```py title:"Syntax"
class ClassName:
    """docstring for ClassName"""

    def __init__(
        self,
        optional_param_1,
        optional_param_2,
    ):
        # initialization code here
        ...

    def method_name(
        self,
        optional_param_1,
        optional_param_2,
    ):
        # body of method
        ...

    # more methods
```

```py
# Real World Example from Python Programming Modular Approach
class Person:
    def __init__(self, name, DOB, address):
        self.name = name
        self.DOB = DOB
        self.address = address

    def get_name(self):
        return self.name

    def get_DOB(self):
        return self.DOB

    def get_address(self):
        return self.address

    def set_name(self, name):
        self.name = name

    def __str__(self):
        return f"Name: {self.name}\nDoB: {self.DOB}\nAddress: {self.address}"


# Object - Instance of class

person_obj = Person("Aravind", "16, May", "Salem")
print(person_obj)

# Access object methods
print(person_obj.get_name())
print(person_obj.get_DOB())
print(person_obj.get_address())
```

### What is Method?

A function defined inside a class. A method always has at least one parameter, which is usually named self.

### What is Instantiation?

We create object from a class which is called instantiation.

### What is Instance variable and it's scope?

Object scope, class scope or instance scope are all pointing the same meaning: the scope consists of all the code inside the class definition.

In a method, any variable with prefix self. Is known as instance variable, which is also object scope.

> [!info] It's a good idea to reference this book - **Object-Oriented Python** by _Irv Kalb_

### Interface vs Implementation

**Interface** - The collection of methods a class provides (and the parameters that each method expects). The interface shows what an object created from the class can do.

**Implementation** - The actual code of the class, which shows how an object does what it does.

## Points to add

- What is composition?
- What is operator overloading?
- What is magic methods?
	- `__dict__()`
	- `__slots__()`
	- `__del__()`
	- `__init__()`
- Extra
	- `vars()`
	- `repr()`
	- what is name mangling
	- `isinstance()`