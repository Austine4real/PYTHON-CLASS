from cgi import print_arguments
from ctypes.wintypes import BOOLEAN
from distutils.cmd import Command
from logging import PlaceHolder
from typing import Tuple
# from math import floor
import math 


age = 15
print(age)

age = 13
print(age)

# multiple declaration
person1, person2, person3 = "Austine", "Toyin", "Kelvin"
print(person3)

var1 = var2 = var3 = "Apples"
print(var2)

#  concantination

firstName = "Austine"
lastName = "Ugbodaga"
fullName =  firstName + ' ' + lastName
print(fullName)

print('my full name is', firstName, lastName)

print(f'my name is {firstName} {lastName} and i am {age} year old')

# slice

random = "Ugbodaga Austine love python program"
print(random[0:8])

print(random[8:])

# PlaceHolder and list(array)

sen = "Hello %s, you are invited to my birthday"
print(sen%("Austine"))

arr = ["Kelvin","Austine","Toyin","Adebayo"]
for i in arr:
  print(sen%(i))
  
sen = "Hello %s %s, you are invited to my birthday"  
print(sen%('Austine','Ugbodaga'))

sen = "Hello my name is %s and i am %d year old"
print(sen%('Austine',29))

arr[3] = "Mark"
print(arr[3])
print(arr)

# some functions
del arr[2]
print(arr)

arr1 = [40,20,25,10]
arr2 = [100,70,50,90]
arr3 = arr1 + arr2
print(arr3)

print(max(arr3))
print(min(arr3))
print(len(arr))

arr.append("Grace")
print(arr)

print(arr.count("Mark"))

# dictionary

students={"Austine":28, "Adebayo":25,"Toyin":23,"Kelvin":26}
 
print(len(students))

print(students.keys())

print(students.values())

students2={"Mark":30, "Avi":22,"Mary":21,"Daniel":24}

students.update(students2)
print(students)

# Tuple
tup1=("maths",25,"english")
print(tup1[0])

# STRING METHOD

# name = input("what is your name? ")
# color = input("what is favourite color ")
# print(f"{name} likes {color} ")

# birth_year = int(input("birth year "))
# age = 2022 - birth_year
# print(age)

# weight_pounds = int(input("what is your weight in pounds\n"))
# weight_kilo = weight_pounds * 0.45
# print(f"your weight in kilogram is :{weight_kilo}\n")

course = '''
Hi Austine,

Hope you got my mail

and have you acted on it.

I awit your reply 

Goodbye.
'''
print(course.upper())

course = "Python for Beginners"
print(course.replace("Beginners", "Absolute Beginners"))

print("Python" in course)

'''
things you can do with string

len()
course.upper()
course.lower()
course.title()
course.find()
course.replace()
"..." in course

Arimthemetic precedence are:-

parenthesis
exponential
multiplication or division
addition or substraction

built in functions are:-
round()
abs()

maths modules are:-
math.floor() 2.9 = 2
math.ceil() 2.9 = 3
'''

# is_hot_day = True
# is_cold_day = False

# if is_hot_day:
#   output = "it's a hot day"
#   output = "Drink plenty of water"
# elif is_cold_day:
#   output = " it's a cold day "
#   output = " Wear warm clothes "
# else:
#   output = "it's a lovely day"
#   print(output)

# BOOLEAN OPERATORS

is_hot_day = False
is_cold_day = True

if is_hot_day:
  print("it's a hot day")
  print("Drink plenty of water")
elif is_cold_day:
  print("it's a cold day")
  print("Wear warm clothes")
else:
  print("it's a lovely day")
print("Enjoy your day")

'''
price of a house is $1M.
if the buyer has good credit,
they need to put down 10%
Otherwise
they need to put down 20%
print the down payment
'''
price = 1000000
has_good_credit = False

if has_good_credit:
  down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
    
print(f"Down payment: ${math.floor(down_payment)}")  

# LOGICAL OPERATORS  
'''
AND: both condition must be true
OR: at least one condition must be true
NOT

if applicant hsa hight income AND good credit they are 
Eligible for loan
'''
has_high_income = True
has_good_credit = False
if has_high_income and has_good_credit:
  print("You are Eligible for loan")
else:
  print("You should go back home")  
   
has_criminal_record = False
has_good_credit = True
if has_good_credit and not has_criminal_record:
  print("You are Eligible for loan")
else:
  print("You should go back home") 
  
  # COMPARISM OPERATORS 
  '''
  if name is less than 3 cnaracters long
      name must be at least 3 characters 
  otherwise if it's more than 50 characters long
      name can be a maximum of 50 characters
  otherwise
      name look good!
  '''
  
name = "J"
if len(name) < 3:
    print("Name must be at least 3 characters")
elif len(name) > 50:
    print("Name can be maximum of 50 characters")
else:
    print("Name look good") 
    
# weight = int(input("Weight: "))
# unit = input("(L)bs or (K)g ")
# if unit.upper() == "L":
#   converted = weight * 0.45
#   print(f"You are {converted} Kilos")
# else:
#   converted = weight / 0.45
#   print(f"You are {converted} pounds")
  
  # GUESSING GAME
# secret_number = 9
# guess_count= 0  
# guess_limit= 3
# while guess_count<guess_limit:
#   guess = int(input('Guess: '))
#   guess_count += 1
#   if guess == secret_number:
#     print('You have won')
#     break
# else:
#   print('Sorry, you failed!')    
  
# CAR GAME
# command = ""
# started = False
# while  True:
#   command = input("> ").lower()
#   if command == "start":
#     if started:
#       print("car is already started!")
#     else:
#       started = True
#       print("Car Started...")
#   elif command == "stop":
#     if not started:
#       print("car is already stopped!")
#     else:
#       started = False
#     print("Car stopped.")
#   elif command == "help":
#     print('''
#         start - to start the car
#          stop - to stop the car
#          quit - to quit      
#       ''')
#   elif command == "quit":
#     break  
#   else:
#     print("Sorry, i don't understant that!")

# FOR LOOP
# prices = [10,20,30,40]
# total = 0
# for price in prices:
#   total += price
# print(f"Total value: {total}")

# for x in range(4):
#   for y in range(3):
#     print(f"({x}, {y})")
    
# numbers = [2, 2, 2, 2, 5]
# for x_count in numbers:
#     output = ""
#     for count in range(x_count):
#       output += "X"
#     print(output)
#   # print('X' * x_count)
  
#   # LIST
# names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
#   #  using index
# print(names[0])  
# print(names[1:3])  
# print(names[2:])  
# print(names[-2])  

# write a program to find the largest number in a list

# numbers = [10, 6, 2, 8, 4, 3]
# max = numbers[0]
# for number in numbers:
#   if number > max:
#     max = number
# print(max)
# print(max(numbers))

# 2 Dimentional list (2D list)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
  for item in row:
    print(item)
    
  # LIST METHOD OR FUNCTION
  '''
  append() = to add a new item to a list
  insert() = to put item at any point in a list(index,object)
  remove() = to remove item from a list remove(item number) 
  clear() 
  pop() = to remove the last time in a list
  index() = to check for an index of number

  '''
  
  
# a=int(input('Enter the valua a'))
# b=int(input('Enter the valua b'))
# c=int(input('Enter the valua c'))

# def quadractic_root(a,b,c):
#     disc=b*b-4*a*c
#     equation_root=math.sqrt(abs(disc))
    
#     if disc>0:
#         print('real but different roots')
#         print((-b + equation_root)/(2*a))
#         print((-b - equation_root)/(2*a))
        
#     elif disc==0:
#         print('real but equal roots')
#         print(-b/(2*a))
        
#     else:
#         print('complex root')
#         print(-b/(2*a),'+ i', equation_root)
#         print(-b/(2*a),'- i', equation_root)
        
# if a==0:
#         print('Input correct quadractic equation')
        
# else:
#         quadractic_root(a,b,c)


# for num in range(1,51):
#   if num%2==0:
#     print(f'{num} is even number')
#   else:
#     print(f'{num} is odd number')
    
# import statistics as st

# def desc(sample):
#   return st.mean(sample), st.median(sample), st.mode(sample)

# sample = [10,2,4,7,3,9,8,6,7]
# mean, median, mode = desc(sample)
# print(desc('sample'))






