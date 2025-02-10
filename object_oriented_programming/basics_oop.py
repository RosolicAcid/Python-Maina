"""
"""
"""This file contains the basic of oop.
So, the oop refers to "Object Oriented Programming", object oriented programming basically is a concept that stores objects in  a class with it's nature and functionality. We can call a class as a template where we can put the objects with it's nature and functionality.
If we took a example, there can be class that is 'Dog'. Let's take a dog has name, age.
"""


# basic class declaration
# class > Keyword
class Dog:
    def __init__(self):
        pass


"""
In Python, the __init__ method is a constructor that is automatically called when a new object (instance) of a class is created. It is used to initialize the attributes of the class.

Why Do We Use __init__?
Automatic Initialization – When an object is created, the __init__ method is executed automatically.
Sets Up Instance Variables – It allows us to assign values to instance variables (attributes) at the time of object creation.
Provides Default Values – We can define default values for attributes if none are provided during object creation.
"""


class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("bark bark!")

    def doginfo(self):
        print(self.name + " is " + str(self.age) + " year(s) old.")

    def birthday(self):
        self.age += 1

    def setBuddy(self, buddy):
        self.buddy = buddy
        buddy.buddy = self


"""
Object-Oriented Programming (OOP) in Python is a way to structure code by creating objects that represent real-world entities. In the given example,
 a Dog class is defined to represent dogs with attributes like name and age, which are initialized through the __init__ constructor method. This constructor ensures that each dog object has unique properties, 
 encapsulating its data. The class also includes behaviors such as bark, which prints a barking sound, and doginfo, which displays the dog’s details. The birthday method increases the dog’s age, simulating
  a real-life passage of time. Additionally, the setBuddy method establishes a relationship between two dog objects, allowing them to reference each other as friends. This demonstrates key OOP principles: 
  Encapsulation, by binding attributes to objects; Abstraction, by hiding implementation details and providing useful methods; Polymorphism, which could be extended to allow different dog breeds to have unique behaviors; 
and Inheritance, which could be used to create specialized dog classes like GuardDog or PetDog. Through this structured approach, OOP makes Python code more organized, reusable, and closer to real-world modeling.
"""
