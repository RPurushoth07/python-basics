<!-- <!-- # Python Basics 
 # What is Variable ?
  A vaariable is a container that stores data.
  eg: name ="Purushothaman"
  variable name =name
  vlaue = Purushothaman

  Without variables 
  print("Purushothaman")
  print("Purushothaman")

  With Variables
  name = "Purushothaman"

  print(name)
  print(name)

  is i change name = "Arun"
  Everything will update automatically

  Variable Rules:
  1.Variable names cannot start with a number
  2.Class is an python Keyword

  Different Types of variables
  1.integer (Whole number)
  2.float(Decimal Numbers)
  3.String(Text)
  4.Boolean(True/False)

  Example:
  emp_name="Puru"
  emp_id=101
  salary=25000
  is_active=True
   -->

<!-- In Python we cannot add String + integer -->

# Float 
<!-- =>A float is any number with decimal point -->


# Functions
<!-- 1.Input()
 => It allows the user to enter valuse dynamically

 eg:name= input("Enter your name:")
    print("Welcome",name) -->


In real applications user enters data 
eg:Login form,ATM,Calculator

# Important
# Input () always returns string

Why this is problem?

a= input(input("Enter first number:"))
b= input(input("Enter second number:"))

print(a+b)

o/p:
10
20
1020

=> Python joins strings
"10"+"20" it becomes 1020

# Type Conversion
<!-- => To Convert Text to number
a = input("Enter number: ")
print(type(a))

o/p: <class 'str'> -->

# Conditions
<!-- => Conditions help a program make decisions.

Real World:
 ATM:
 if balance > withdraw amount
     allow withdrawl
 Else
     show insufficient balance -->

 LOGIN:
 if username and password are correct
    Login success
 Else
    Login failed

Calculator:
If secode number is 0
   Don't divide
Else
   Perform division
 -->

# Funtions(def)
 Function help us to 
 =>reuse the code 
 =>reduce duplication
 =>Make code easier to read
 => Organize Programs

#basic Function Sytax
def greet():
  print("Hello")
o/p:
hello
# Function with Parameters
def greeT(name):
    print("Hello",name)

greet("Purushothaman")

O/p:
Hello Purushothaman

# Function returning value
 
 def add(a,b):
   return a + b
 result = add(10,20)

print(result)

o/p:
30

print(a+b)
print(a-b)
print(a*b)
print(a/b)

# with funtions
def add(a,b):
    return a + b
def subtract(a, b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
   if b !=0:
     return a /b
   return "cannot divide by zero"





