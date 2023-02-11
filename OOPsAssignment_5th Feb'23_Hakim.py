#!/usr/bin/env python
# coding: utf-8

# # Data Science Masters
# ## OOPS_Assignment_5th Feb'23
# ### Name: Hakim Brbaa

# #####

# ##### Q#1. Explain Class and Object with respect to Object-Oriented Programming. Give a suitable example.
# 
# Class and Object are the two fundamental concepts in Object-Oriented Programming (OOP). A class is a blueprint for creating objects (a particular data structure), providing initial values for state (member variables or attributes), and implementations of behavior (member functions or methods). An object is an instance of a class, created at runtime, with a unique identity and state, and behavior as defined in its class.
# 
# For example, consider a class named "Person", which represents a person's name, age, and address. We can create multiple objects of this class, such as John, Sarah, and Alex, each having their own unique values for name, age, and address.

# ##### Q#2. Name the four pillars of OOPs.
# 
# 1. Abstraction: Hides the implementation details and shows only the necessary information to the user.
# 2. Encapsulation: Wraps the data and behavior into a single unit (object) and protects it from external access and modification.
# 3. Inheritance: Allows creating a new class that is a modified version of an existing class, without changing the existing class.
# 4. Polymorphism: Allows using a single entity to represent different types of objects, based on the context in which they are used.

# ##### Q#3. Explain why the __init__() function is used. Give a suitable example.
# 
# The __init__ function is used in OOPs as a constructor for the class. It is called when an object of the class is created, and it allows the class to initialize its state. The __init__ method takes the first argument as "self", which refers to the newly created object itself.
# 
# For example, consider a class named "Person", which has name, age, and address attributes. The __init__ function can be used to initialize these attributes as follows:

# In[2]:


class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address


# ##### Q#4. Why self is used in OOPs?
# 
# self is used in OOPs to refer to the instance of an object from within the object's methods. It allows the object's methods to access and modify the object's state. Without self, it would not be possible to determine which object's state is being referred to, as a class can be used to create multiple objects.
# 
# For example, consider a class named "Person", which has name, age, and address attributes and a method named get_details:

# In[4]:


class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}, Address: {self.address}"


# ##### Q#5. What is inheritance? Give an example for each type of inheritance.
# 
# Inheritance is a mechanism in OOPs that allows creating a new class that is a modified version of an existing class, without changing the existing class. The new class is called the derived class, and the existing class is called the base class. Inheritance allows the derived class to inherit the attributes and behaviors of the base class, and to add or override the attributes and behaviors as necessary.
# 
# There are several types of inheritance:
# 
# 1. Single Inheritance: A derived class inherits from a single base class.
# 2. Multiple Inheritance: A derived class inherits from multiple base classes.
# 3. Hierarchical Inheritance: Multiple derived classes inherit from a single base class.
# 4. Multi-level Inheritance: A derived class inher

# #####

# In[ ]:




