from abc import ABC, abstractmethod

class Person(ABC):
    
    @abstractmethod
    def get_gender():
        pass

class Male(Person):
    def get_gender(self):
        print("Male")

class Female(Person):
    def get_gender(self):
        print("Female")

obj1 = Male()
obj1.get_gender()

obj2 = Female()
obj2.get_gender()

obj3 = Person()  #This will throw error since Person is an abstract class

