# -*- coding: utf-8 -*-
"""Copy of OOP_Mandatory_Assignment.ipynb


Original file is located at
    https://colab.research.google.com/drive/1Dy59YoBicGdbw-VWlFvVvfUpd_7LWKHp

# Object-Oriented Programming (OOP) - Practice Assignment

This assignment will help you understand the basics of Object-Oriented Programming (OOP) in Python.  
Each question is written in a simple way so that you know exactly what to do.

**Structure:**
- 6 Easy Questions  
- 2 Medium Questions  
- 2 Hard Questions

Follow each question carefully and try to run the examples step by step.

### Question 1 (Easy)
**Create a Class and Object**

Create a class named `Student` with one attribute `name`.  
Then create an object of this class and print the student's name.

*Hint:* Use the `__init__` method to initialize the name attribute.
"""

class Student:
    def __init__(self, name):
        self.name = name

student1 = Student("Alice")
print(student1.name)

"""### Question 2 (Easy)
**Add Multiple Attributes**

Create a class `Car` that has two attributes: `brand` and `year`.  
Create two objects of this class for two different cars and print their details using `print()`.
"""

class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

car1 = Car("Toyota", 2020)
car2 = Car("Honda", 2018)

print(f"Car 1: {car1.brand}, {car1.year}")
print(f"Car 2: {car2.brand}, {car2.year}")

"""### Question 3 (Easy)
**Methods in a Class**

Create a class `Circle` with one attribute `radius`.  
Add a method `area()` that returns the area of the circle.

*Formula:* Area = π × radius²
"""

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

circle1 = Circle(5)
print(f"The area of the circle is: {circle1.area()}")

"""### Question 4 (Easy)
**Default and Parameterized Constructor**

Create a class `Book` that takes the book title and author name as parameters when creating an object.  
Also, create one object without any arguments and set default values like `'Unknown Title'` and `'Unknown Author'`.
"""

class Book:
    def __init__(self, title="Unknown Title", author="Unknown Author"):
        self.title = title
        self.author = author

book1 = Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams")
print(f"Book 1: Title - {book1.title}, Author - {book1.author}")

book2 = Book()
print(f"Book 2: Title - {book2.title}, Author - {book2.author}")

"""### Question 5 (Easy)
**Use of Self Keyword**

Create a class `Employee` that has a method `display()` which prints `'This is an Employee class'`.  
Then create one object and call the method using that object.
"""

class Employee:
    def display(self):
        print('This is an Employee class')

employee1 = Employee()

employee1.display()

"""### Question 6 (Easy)
**Simple Calculator Class**

Create a class `Calculator` with methods for addition, subtraction, multiplication, and division.  
Each method should take two numbers as parameters and return the result.
"""

class Calculator:
    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        if num2 == 0:
            return "Error: Division by zero"
        else:
            return num1 / num2

calculator = Calculator()

result_add = calculator.add(10, 5)
print(f"Addition: {result_add}")

result_subtract = calculator.subtract(10, 5)
print(f"Subtraction: {result_subtract}")

result_multiply = calculator.multiply(10, 5)
print(f"Multiplication: {result_multiply}")

result_divide = calculator.divide(10, 5)
print(f"Division: {result_divide}")

result_divide_by_zero = calculator.divide(10, 0)
print(f"Division by zero: {result_divide_by_zero}")

"""### Question 7 (Medium)
**Working with Multiple Objects**

Create a class `Student` with attributes `name`, `marks1`, `marks2`, and `marks3`.  
Add a method `average()` that returns the average marks of the student.  
Create objects for three students and print their average marks.
"""

class Student:
    def __init__(self, name, marks1, marks2, marks3):
        self.name = name
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3

    def average(self):
        return (self.marks1 + self.marks2 + self.marks3) / 3

student1 = Student("Alice", 85, 90, 88)
student2 = Student("Bob", 78, 82, 80)
student3 = Student("Charlie", 92, 88, 95)

print(f"{student1.name}'s average marks: {student1.average():.2f}")
print(f"{student2.name}'s average marks: {student2.average():.2f}")
print(f"{student3.name}'s average marks: {student3.average():.2f}")

"""### Question 8 (Medium)
**Inheritance Concept**

Create a base class `Person` with an attribute `name` and a method `show_name()`.  
Then create a derived class `Teacher` that adds a new attribute `subject` and a method `show_subject()`.  
Create an object of `Teacher` and call both methods.
"""

class Person:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print(f"Name: {self.name}")

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def show_subject(self):
        print(f"Subject: {self.subject}")


teacher1 = Teacher("Mr. Smith", "Math")

teacher1.show_name()
teacher1.show_subject()

"""### Question 9 (Hard)
**Encapsulation Example**

Create a class `BankAccount` with attributes `__balance` (private) and `account_holder`.  
Add methods `deposit(amount)` and `withdraw(amount)` to update the balance safely.  
Print the final balance only through a method `show_balance()`.
"""

class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.__balance = initial_balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: ${amount:.2f}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: ${amount:.2f}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def show_balance(self):
        print(f"Account balance for {self.account_holder}: ${self.__balance:.2f}")


account1 = BankAccount("Alice", 1000)
account1.deposit(500)
account1.withdraw(200)
account1.show_balance()

account1.withdraw(2000)
account1.deposit(-100)
account1.show_balance()

"""### Question 10 (Hard)
**Polymorphism Example**

Create two classes: `Dog` and `Cat`.  
Both should have a method named `speak()` that prints the sound of the animal.  
Write a function `animal_sound(animal)` that calls the `speak()` method of any animal passed to it.

*Hint:* This shows how the same method name can have different behaviors depending on the object type.
"""

class Dog:
    def speak(self):
        print("Woof!")

class Cat:
    def speak(self):
        print("Meow!")

def animal_sound(animal):
    animal.speak()


dog = Dog()
cat = Cat()

print("Demonstrating polymorphism:")
animal_sound(dog)
animal_sound(cat)
