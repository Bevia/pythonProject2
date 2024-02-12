from abc import ABC, abstractmethod


# In Python, the `ABC` (Abstract Base Class) module is used when you want to define abstract base classes.
# Abstract base classes are classes that are meant to be subclassed but not instantiated themselves.
#
# By using the `ABC` module and the `abstractmethod` decorator, you can create abstract methods within
# your classes that must be implemented by any subclass. This helps to define a blueprint for classes
#     that inherit from your abstract base class.
#
# In the context of the example we discussed earlier, using the `ABC` module and `abstractmethod`
# decorator allows you to create an interface-like structure where the `Interface` class defines
#     a method that must be implemented by any class that inherits from it. This way, you can ensure
#     that certain methods are implemented in the subclasses, providing a clear structure and
#     ensuring consistency in your codebase.

class Interface(ABC):
    @abstractmethod
    def my_method(self):
        pass
