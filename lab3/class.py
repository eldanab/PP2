#Exercises from w3schools
#Ex.1 & 2 & 3
class MyClass:
  x = 5
p1 = MyClass()
print(p1.x)

#Ex.4
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
p = Person("Eldana", 17)
print(p.name, p.age)