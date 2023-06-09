# -*- coding: utf-8 -*-
"""Python session 04.09.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mmbvvwkz71gbWZPmnoKdNvfMfuA-_SLW
"""

x = 'Hello World'
print(x)

# Loop control
#1. Loop variable initialization
#2. condition for termination
#3. Updation of loop variable

#in Python we have 2 type loops
#1. For Loop 
#2. While Loop

#1. While Loop

Syntax : while (condition):
           statement 1
		       statement 2
		       .
		       .
		       .
		       statement n
		     statement X

#Example: Factorial

number = 6 #Loop Variable
result = 1

while number > 0:  # condition for termination
  result = result * number
  number = number - 1 # updation

print(result)

# find the sumation of 10

number = 10
result = 0
while number > 0:
  result = result + number
  number = number - 1
print(result)

# find the sumation of 100

number = 100
result = 0
while number > 0:
  result = result + number
  number = number - 1
print(result)

# 2. for loop 

 syntax : for i in sequence:
              statement 1
              statement 2
              statement 3
              .
              .
              satement n
          statement x

# All the 3 Loop controls (initialization, termination, updation of loop variable) are performed  in the sequence.
# Sequence could be any collection (Array, List, Tuple, Dictionary)

for i in ["apple", "Banana", "Mango", "Cherry", "Sapota"]:
  print(i)

for i in range(5):
  print(i)

for i in range(1, 50, 5):
  print(i)

# Example: finding the Factorial

result = 1
for i in range(1, 7):
  result *= i
print(result, i)

result = 1
for i in range(1, 9):
  result += i
print(result)

result = 0
for i in range(10,21):
  result += i
print(result)

start = int(input("Enter the first number: "))
stop = int(input("Enter the second number: "))

result = 0
for i in range(start, stop +1):
   result += i
print(result)

While vs For loop

1. while: indefinite and For: definite
2. While: 

Palindrum : when revers the numbers the result will be the same.
for example: 121 palindrum will be 121
             131 palindrum will be 131

# Break

#Break will stop the nearest the loop and it can be used in both For and while.

# break will stop the very nearest loop

number = 6 #Loop Variable
result = 1

while number > 0:  # condition for termination
  result = result * number
  number = number - 1 # updation

print(result)

# this is Do While loop

number = 6
result = 1
while True:
  result = result * number
  number = number - 1
  if number == 0:
    break
print(result)

# continue

# whatever the code is written below the CONTINUE, that will be avoided by the Python control.

for i in range(1, 11):
  if i == 5:
    continue
  print(i)

# zip function
# zip is only used when same number of itmes in both list, otherwise it will not working

fruits = ["apple", "banana", "cherry", "Mango"]
price = [40, 20, 25, 50]

result = zip(fruits, price)

for i in result:
  print(i)

#enumerate function

students = ["Nayak", "Ansari", "Sanjeet", "Mayur"]

result = enumerate(students)

for i in result:
  print(i)

# we can define the start position of indexing through below syntax

students = ["Nayak", "Ansari", "Sanjeet", "Mayur"]

result = enumerate(students, 5)

for i in result:
  print(i)

string = "myprogram.exe"

result = string[9:]
print(result)

string = "myprogram.exe"

result = string[5:-4]
print(result)

# collection - Data Structure - class
# collection means collection of more than 1 item
# Data structure not only have data value it also have the information on how to travrse from one element to another

# 1. String
# 2. List
# 3. Dictionary
# 4. Set
# 5. Tuple
# above all the data structure are class

dir(str)