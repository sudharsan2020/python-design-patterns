from myclass import MyClass
from nullclass import NullClass

class MyObjectFactory:
    @staticmethod
    def create_object(value):
        return MyClass() if value == 'myclass' else NullClass()
