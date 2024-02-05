#Exercises from w3schools
#Ex.1&2
def my_function():
  print("Hello from a function")
my_function()

#Ex.3
def my_function(fname, lname):
  print(fname)
my_function("Tony", "Stark")

#Ex.4
def my_function(x):
  return x + 5
print(my_function(3))

#Ex.5
def my_function(*kids):
  print("The youngest child is " + kids[2])
my_function("John", "Laura", "Alice")

#Ex.6
def my_function(**kid):
  print("His last name is " + kid["lname"])
my_function(fname = "Peter", lname = "Parker")