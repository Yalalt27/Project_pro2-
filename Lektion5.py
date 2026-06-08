#1 Övning
'''
class Book:
      def __init__(self, title, author,year):
            self.title = title
            self.author = author
            self.year = year
      def describe(self):
            return f"{self.title} by {self.author}, published in {self.year}"
book1 = Book("The Stockholm city","Yalalt",2018)
print(book1.title)
print(book1.describe())
 
#2 Övning
class Customer:
      def __init__(self, name, age):
            self.name = name
            self.age = age
      def greet(self):
            return f"Jag heter {self.name} och jag är {self.age} år gammal"
object = Customer("Anna","30")
print(object.name)
print(object.greet())

# Övning 3
class Student:
      def __init__(self, name, year):
            self.name = name
            self.year = year
      def introduce(self):
            return f"Hej, jag heter {self.name} och går årskurs {self.year}."
obj = Student("Emma","9")
print(obj.introduce())

'''
# Övning 4

class Car:
      def __init__ (self, brand, model, year, speed):
            self.brand = brand
            self.model = model
            self.year = year
            self.speed = speed
      def introduce(self):
            return f"{self.brand}\n{self.model}\n{self.year}\n{self.speed}km/h\n"
      
obj = Car ("Toyota","Corolla","2022",(180))
obj1 = Car ("Honda", "Civic","2021","160" )
print(obj.introduce())
print(obj1.introduce())
      
      

