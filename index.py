# from ast import comprehension
# from math import ceil
# from math import floor
# from msilib.schema import Directory
# from pyclbr import Function
# from random import sample
# import string
# from tkinter import Variable
# import math

'''
# # Variable

2name="david"
@name="david"
-name="david"
boys-name="david"

name2 = 'david'
boys_name = 'david'
boysName2 = 'david'
Boysnames = 'david'

##_no_touchy_

NAME

'''
# name ='David'
# print(name)

# ##string concatenation
# first_name = 'David'
# last_name = 'Shuaib'

# full_name = first_name + ' ' + last_name
# print(full_name)

# # variable concat
# print('Toyin' + ' Salami')

# print('my last name is', last_name, first_name)
# print('my last name is ' + last_name +" " + first_name)

# name= 'Sugar'
# name += ' Daddy'
# print(name)


# num=8
# print(f'my fullname is {first_name} {last_name} and i love {num}')

# number=11
# player='Timo'
# players='Werner'
# club='Chelsea'
# print(f'{player} {players} wears jersey number {number} for {club}')


### retreiving input from user

# age=int(input('How old are you?\n'))
# age=(input('How old are you?\n'))

# print(f'you said you are {age} years old')

# kilo = int(input('how many kilometer did you walk?\n'))
# mile = (kilo) * 0.6271
# print(f'that means you have walked {mile} miles?\n')

# kms=int(input('how many kms have cycled today?\n'))
# miles=(kms)/0.621271
# # Austine=round(miles,2)
# print(f'your cycling of {kms}kms is {math.floor(miles)}im in miles')

# # # conditional logic

# age=int(input('How old are you?\n'))
# if(age<18):
#     output='you can cant\'t enter the party'
# elif(age>=18 and age<=20):
#     output='you can enter the party but you can\'t drink'
# elif(age>=21):
#     output='you can enter the party and you can drink'
# else:
#     output='enter a valid age'
# print(output)

# city = input("Where do you live?\n")
# if(city == "LOS ANGELES" or city == "SAN FRANCISCO"):
#     print("you live in california")
# else:
#     print("you live somewhere else")
  
#   Truthiness and Falsiness
# animal = input("what's your favourite animal ")
# if animal:
#     status = (f"{animal} is my favourite animal")
# else:
#     status = ("you are not saying anything")
# print(status)

# print("...rock...")
# print("...paper...")
# print("...scissors...")

# player1=input("player1, take your move\n").lower()
# player2=input("player2, take your move\n").lower()

# if(player1==player2):
#     status="it is a tie"
# elif(player1=="rock" and player2=="paper" ):
#     status="player2 wins"
    
# elif(player1=="paper" and player2=="rock" ):
#     status="player1 wins"
    
# elif(player1=="scissor" and player2=="rock" ):
#     status="player2 wins"
    
# elif(player1=="rock" and player2=="scissor" ):
#     status="player1 wins"
    
# elif(player1=="paper" and player2=="scissor" ):
#     status="player2 wins"
    
# elif(player1=="scissor" and player2=="paper" ):
#     status="player1 wins"
# else:
#     status="Enter a valid move"
# print(status)

# # python loop

# letter = "salah"
# for char in letter:
#     print(char)
    
# tea = "coffee"
# for i in tea:
#     print(i*10)
    
# for x in range(4):
#    for y in range(3):
#     print(f"({x}, {y})")
    
# numbers = [5, 2, 5, 2, 2]
# for x_count in numbers:
#     output = ""
#     for count in range(x_count):
#       output += "X"
#     print(output)
# print('X' * x_count)
    
# for X in range(1,30):
#     print(X)

# apology = 100
# for time in range(100):
    # print(f"{time + 1} please forgive Toyin")
    
# name = "David"
# mother = int(input(f"how many times do i have to tell you to clean up your ?\n"))
# for times in range(mother):
#     print(f"{times + 1} Clean up your room")

# for num in range(1,11):
#  print("\U0001F600" * num)

# for number in range(1,51):
#     if (number==4 or number==13):
#         state = "Unlucky"
#     elif(number%2==0):
#         state = "Even"
#     elif(number%2 !=0):
#         state = "Odd"
#     else:
#         state="Enter a valid number"  
#     print(f"{number} is {state}")   
    
# admin = int(input("Enter your secrete number\n"))

# for num in range(3):
#     user=int(input("Enter your guess\n"))
#     if admin==user:
#         print(f"Congrat! Your guess of {user} is correct")  
#         break 
#     elif(admin !=user):
#         print(f"oop! your guess of {user} is wrong. You can made {num + 1} move(s)")
#     else:
#         print("Idiot you are not sure what you want")
        
######### while loop

# num=1
# while num<11:
#     print(num)
#     num += 1
    
# num=20  
# while num >=1:
#     print(num) 
#     num -=1 
    
# password =input("Enter your secret password\n")
# while password != "banana":
#     print("You are wrong")
#     password = input("Enter your secret password2\n")
# print("Correct")

# number = 1
# while number<51:
#     if (number==4 or number==13):
#         state = "Unlucky"
#     elif(number%2==0):
#         state = "Even"
#     elif(number%2 !=0):
#         state = "Odd"
#     else:
#         state="Enter a valid number"  
#     print(f"{number} is {state}") 
#     number +=1 

# #  random number

import random 
# random_Number=random.random()

# print(random_Number)

# random_Number=random.randint(1,99)
# print(random_Number)

# num = 1
# while num < 4:
#     random_num=random.randint(1,10)
#     num +=1
#     print(f"The computer choses {random_num}")
#     player=int(input("choose a number\n"))
#     if(random_num<player):
#         print(f"The number {player} you have chosen is higher than number {random_num} chosen by the computer")
#     elif(random_num>player):
#         print(f"The number {player} you have chosen is lower than number {random_num}")
#     else:
#         print("it's a tie")
        
# import random

# player_wins = 0
# computer_wins = 0
# winning_score = 3

# while(player_wins<winning_score and computer_wins<winning_score):
#     print(f"player score = {player_wins} - computer score = {computer_wins}")
    
#     print('...rock...')
#     print('...paper...')
#     print('...scissors...')
#     player = input("take your move ").lower()
#     if(player=="quit" or player =="q"):
#         break
    
#     random_num=random.randint(0,2)
    
#     if(random_num==0):
#         computer = "paper"
#     elif(random_num==1):
#         computer="rock"
#     else:
#         computer="scissors"
#     print(f"computer player {computer}")
    
    
#     if player==computer:
#         print("it's a tie")
        
#     elif player=="rock":
#         if computer=="paper":
#             print("computer wins!")
#             computer_wins +=1
#         else:
#             print("player wins!")
#             player_wins +=1
            
            
#     elif player=="paper":
#         if computer=="rock":
#             print("player wins!")
#             player_wins +=1
            
#         else:
#             print("computer wins!")
#             computer_wins +=1
            
            
            
#     elif player=="scissors":
#         if computer=="rock":
#             print("computer wins!")
#             computer_wins +=1
            
#         else:
#             print("player wins!")
#             player_wins +=1
            
#     else:
#         print("please enter a valid move!")


# print(f"FINAL SCORE: player = {player_wins} - computer = {computer_wins}")
# if(computer_wins==player_wins):
#     print("IT'S A TIE")
# elif(player_wins>computer_wins):
#     print("congrat! you won")
# else:
#     print("OH NO! COMPUTER WON")

            
##########  python list   
# student = ["paul", "sam","David","Daniel"] 
# print(student)

#  #####  append
# a = "Austine"
# student.append(a)

# # ####### join
# print(', '.join(student))

# ###### we work with list insert

# student.insert(1,"Tunde")
# print(student)

# ##### To re-assign

# name = "Oladipo"
# student[1]=name
# print(student)

# # # # EXTEND

# fruits = ['apple', 'mango', 'water melon','banana','mango']
# cars =['Ford', 'toyota', 'lexus','benz']
# fruits.extend(cars)
# print(fruits)

# cars.extend(fruits)
# print(cars)

# # # # count
# x=fruits.count('mango')
# print(x)

# # # # To slice
# student = ['Tosin', 'Paul', 'Seun', 'Ebun','Olamide']
# print(student[1:3])
# print(student[2:])
# print(student[0:1])

# student.remove('paul')
# print(student)

# # student.clear()
# del student
# print(student)

# # To POP
# student = ['Tosin', 'Paul', 'Seun', 'Ebun','Olamide']
# student.pop()
# student.pop(3)
# print(student)

# count = 0
# Tinubu=[]
# Obi=[]
# Atiku=[]
# Kwakwanso=[]
# Sowore=[]

# while count < 12:
#     cast = input('Cast your vote for you preferred candidate: (A) Sowore (B) Tinubu (C) Obi (D) Atiku (E) Kwakwanso\n').capitalize()

#     if(cast == 'A' or cast=='Sowore'):
#         Sowore.append('A')
        
#     elif(cast=="B" or cast=='Tinubu'):
#         Tinubu.append('B')
        
#     elif(cast=="C" or cast=='Obi'):
#         Obi.append('C')
        
#     elif(cast=="D" or cast=='Atiku'):
#         Atiku.append('D')
        
#     elif(cast=="E" or cast=='Kwakwanso'):
#         Kwakwanso.append('E')
        
#     else:
#         print("Enter a valid vote")
        
#     Sowore_vote = len(Sowore)
#     Tinubu_vote = len(Tinubu)
#     Obi_vote = len(Obi)
#     Atiku_vote = len(Atiku)
#     Kwakwanso_vote = len(Kwakwanso)
    
    
#     print(f'Total valid vote by each candidate are as follow: Sowore={Sowore_vote}, Tinubu={Tinubu_vote}, Obi={Obi_vote}, Atiku={Atiku_vote}, Kwakwanso={Kwakwanso_vote}')
    
#     count +=1
    
#     if(Sowore_vote>Tinubu_vote and Sowore_vote>Obi_vote and Sowore_vote>Atiku_vote and Sowore_vote>Kwakwanso_vote):
#         print('SOWORE WON')
        
#     elif(Tinubu_vote>Sowore_vote and Tinubu_vote>Obi_vote and Tinubu_vote>Atiku_vote and Tinubu_vote>Kwakwanso_vote):
#         print('TINUBU WON')
        
#     elif(Obi_vote>Sowore_vote and Obi_vote>Tinubu_vote and Obi_vote>Atiku_vote and Obi_vote>Kwakwanso_vote):
#         print('OBI WON')
        
#     elif(Atiku_vote>Sowore_vote and Atiku_vote>Obi_vote and Atiku_vote>Tinubu_vote and Atiku_vote>Kwakwanso_vote):
#         print('ATIKU WON')
        
#     elif(Kwakwanso_vote>Sowore_vote and Kwakwanso_vote>Tinubu_vote and Kwakwanso_vote>Obi_vote and Kwakwanso_vote>Atiku_vote):
#         print('kWAKWANSO WON')
        
#     else:
#         print('Enter a valid vote')


    
    # name = ['Austine', 'Toyin', 'Adebayo', 'Kelvin']
    # game = input('enter your name\n')
    # if game in name:
    #     print("your are welcome")
    # else:
    #     print('you are not one of us')
    
    
# student =['Tosin', 'Paul', 'Seun', 'Ebun', 'Olamide', 'Toyin', 'Adebayo', 'Kelvin', 'Ugbodaga']
# guest= input('Enter your name here please\n')
# first_char = (guest[0:1])
# first_char_upper= first_char.upper()
# rem_char= (guest[1:(len(guest))])
# rem_char_lower=rem_char.lower()
# full_name=first_char_upper + rem_char_lower
# if(full_name in student):
#         print(f'You are welcome to class {full_name}')
# else:
#         print(f'you are not one of us {full_name}')
        
# student =['Tosin', 'Paul', 'Seun', 'Ebun', 'Olamide', 'Toyin', 'Adebayo', 'Kelvin', 'Ugbodaga']
# guest= input('Enter your name here please\n')
# first_char = (guest[0:1]).upper()
# rem_char= (guest[1:(len(guest))]).lower()
# full_name=first_char + rem_char
# if(full_name in student):
#         print(f'You are welcome to class {full_name}')
# else:
#         print(f'you are not one of us {full_name}')

    
# colors = ['purple', 'teal', 'magenta','crimson', 'red']
# for color in colors:
#     print(color)
    
# index = 0
# while index < len(colors):
#     print(f'{index+1}:{colors[index]}')
#     index += 1

# numbers = [4,5,6,7,8,9,5,8,8,9,10,11]
# numbers.index(6)
# print(numbers.index(6))
# # print(numbers.index[6])
# print(numbers.index(5))
# print(numbers.index(5,2))
# print(numbers.index(8,6,8))

# numbers = [4,5,6,7,8,9,5,8,8,9,10,11]
# def double(lst):
#     for x in lst:
#         x *= 2
#         print(x)
#     return lst
# print(double(numbers))

        # OR
        
# for num in numbers:
#     print(num*2)
        
        # OR
# nub = []      
# for num in numbers: 
#     nub.append(num*2)
# print(f'{nub}')
        
# list comprehension

# numbers = [5,5,6,7,8,9,5,8,8,910,11]
# doubled_numbers=[]
# for number in numbers:
#     doubleNumber=number * 2
#     doubled_numbers.append(doubleNumber)
# print(doubled_numbers)

# print([number*2 for number in numbers])


# name = 'Austine'
# print([char.upper() for char in name])

# name='Austine'
# character=[]
# for char in name:
#     upper=char.upper()
    
#     character.append(upper)
# print(character)

# friends = ['Ashley','Jibril','Junior','Godwin']
# print([friend.upper() for friend in friends])
# print([friend[0].upper() for friend in friends])

# friends = ['Ashley','Jibril','Junior','Godwin']
# friendship=[]
# for friend in friends:
#     frien=friend.upper()
#     friendship.append(frien)
    
# print(friendship)

#  # DICTIONARY

# son=[{'man':'warri', 'x':34, 'valid':True, 'name':'Austine'}]
# print(son)

# instructor={
#     'name':'David',
#     'num_course':4,
#     'owns_dog': True,
#     'fav_language':'python',
#     'is_tall':True,
#     44:'my favorite number'
# }

# print(instructor)

# cat=dict(name='kitty',age=2,color='brown')
# for v in cat.values():
#     print(v)
# print(cat)

###### accessing value in Directory
# .value()
# .key()
# .ittems()

# for v in instructor.values():
#     print(v)
    
# w=[]
# for v in instructor.values():
#     w.append(v)
# print(w)
# print(w[1])

# for k in instructor.keys():
#     print(k)


# l=[]
# for k in instructor.keys():
#     l.append(k)
# # print(w)
# print(l[3])

# playlist={
#     'title':'party mix',
#     'author':'Dj Kaywise',
#     'songs':[
#         {'title':'essence', 'artist':['Big wiz','Tems'],'duration':2.5},
#         {'title':'fem', 'artist':['Davido'],'duration':4},
#         {'title':'kilometer', 'artist':['Burna Boy'],'duration':3.5}
#     ]
# }

# total_duration = 0
# for song in playlist['songs']:
    # print(song['duration'],':', song['title'], ':', song['artist'])
    # print(song['title'])
    
#     total_duration +=song['duration']
# print(f'The total duration for the play list is {total_duration} minutes')

# python Function

# def austine():
#     print('This is a function')
# austine()
# austine()
# austine()


# def austine():
#     playlist={
#     'title':'party mix',
#     'author':'Dj Kaywise',
#     'songs':[
#         {'title':'essence', 'artist':['Big wiz','Tems'],'duration':2.5},
#         {'title':'fem', 'artist':['Davido'],'duration':4},
#         {'title':'kilometer', 'artist':['Burna Boy'],'duration':3.5}
#     ]
#     }

#     total_duration = 0
#     for song in playlist['songs']:
#         print(song['duration'],':', song['title'])
#         print(song['title'])
    
#         total_duration +=song['duration']
#     print(f'The total duration for the play list is {total_duration} minutes')

# austine()


# adding parameter to a function

# def dami(num1,num2):
#     print(num1*num2)
#     print(num1+num2)
# dami(4,5)  
# dami(3,5)


# def austine(name):
#     for song in range(1,3):
#         sing=('Happy birthday to you')
#         print(sing)
#     print(f'{sing} dear {name}')
#     print(sing)
# austine('David')



# functions return

# def BBN(name,age):
#     names='Governor'
#     # print(names)
    
#     result=(f'{name} of age {age} was a member of BBN')
#     return result

# print(BBN('Boma',36))


# def find_average(marks):
#     sum_of_marks=sum(marks)
#     total_subjects=len(marks)
#     average_marks=sum_of_marks/total_subjects
#     return average_marks


# def compute_grade(average_marks):
#     if average_marks>=80:
#         grade='A'
#     elif (average_marks>=60):
#         grade='B'
#     elif (average_marks>=40):
#         grade='C'
#     else:
#         grade='D'
        
#     return grade

# marks=[55,64,75,80,65,100,100,100,99]
# average_marks=find_average(marks)
# print(f'Your average mark is :', average_marks)
# grade = compute_grade(average_marks)
# print(f'Your grade is: {grade}')


    
# a=int(input('enter a'))
# b=int(input('enter b'))
# c=int(input('enter c'))
   
# def mark(a,b,c):
#     dis_form = b*b-4*a*c
#     sqrt_value = math.sqrt(abs(dis_form))
    
#     if dis_form>0:
#         print('real and different roots')
#         print(-b + sqrt_value/(2*a))
#         print(-b - sqrt_value/(2*a))
        
#     elif dis_form==0:
#         print('real and same roots')
#         print(-b/(2*a))
        
#     else:
#         print('complex roots')
#         print(-b/(2*a), '+ i', sqrt_value)
#         print(-b/(2*a), '- i', sqrt_value)
    

#     if a ==0:
#              print('input correct quadratic equation')
    
#     else:
#             mark(a,b,c)
         
## ##  ##  quadractic Equation

# a=int(input('Enter the valua a\n'))
# b=int(input('Enter the valua b\n'))
# c=int(input('Enter the valua c\n'))

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
#         print(f'{-b/(2*a)} + i {equation_root}')
#         print(-b/(2*a),'- i', equation_root)
        
# if a==0:
#         print('Input correct quadractic equation')
        
# else:
#         quadractic_root(a,b,c)
        
        
        
# a=int(input('Enter side\n'))
# b=int(input('Enter side\n'))
# h=int(input('Enter height\n'))  

# def area(a,b,h):
#     top = (a+b)*h
#     calc = top * 0.5 
#     return calc
# print(area(a,b,h))


# def valid_isbn(isbn):
#     if len(isbn) != 10:
#         return False
    
#     # initialize sum_num to 0
#     sum_num = 0
    
#     # iterate through isbn
#     for num in range(10):
        
#     # for each character, multiply by a different decreasing number:10-num    
#         if 0<= int(isbn[num]) <= 9:
#             sum_num += int(isbn[num]) * (10-num)
#         else:
#             return False
        
#     print(sum_num)
     
#     if sum_num % 11 == 0:
#         print('valid')
#     else:
#         print('invalid') 
# valid_isbn('0074625438')



# isbn = input('Enter your Isbn number\n')
# def valid_isbn(isbn):
#     isbn=isbn.replace('_','').replace(' ','')
    
#     if len(isbn) != 10:
#         return False
    
#     if not isbn[0:8].isdigit() or isbn[9].lower()=='X':
#         return False
    
#     result = 0
#     for i in range(9):
#         result += int(isbn[i]) * (10-i)
    
#     if isbn[9].lower()=='x':
#         result += 10
#     else:
#         result += int(isbn[9])
#     print(result)
        
#     if result % 11 == 0:
        
#         return True
#     else:
#         return False
    
# if valid_isbn(isbn):
#     print('Isbn is valid')
# else:
#     print('Invalid Isbn')
    
    # 007462542x
    
    
# ERROR 
# ZeroDivisionError
# IndexError

# def error_handling():    
#     try:
    
#         numerator=int(input('Enter the numerator: '))
#         denominator=int(input('Enter the denominator: '))
#         result=numerator//denominator
#         print(result)
        
#         my_list=[1,2,3]
#         i=int(input('Enter index: '))
#         print(my_list[i])
            
#     except ZeroDivisionError:
#         print('Numbers cannot be divisible by zero. try again')
        
            
#     except IndexError:
#         print('Index out of range')
        
#     else:
#         print('There are no exceptions')
        
#     finally:
#         print('i must ran')
        
# error_handling()

# def div():
#     try:
#         numerator=int(input('Enter the numerator: '))
#         denominator=int(input('Enter the denominator: '))
#         result=numerator/denominator
#         print(result)
#     except:
#         denominator+=1
#         result = numerator/denominator
#         print(result)
#     finally:
#         print('i must run')
# div()

# using date in pyyhon

# from datetime import date, datetime 

# david = date.today()
# print('current date: ', david)


# # # # formatting datetime string

# d= datetime.today()
# print(d.strftime('%B %d %Y %I:%S %p'))

# nameless or lamda function

# def double(n):
#     return n*2
# print(double(10))


# double= lambda n :n*2
# print(double(5))

# larger = lambda a,b:a if a>b else b
# print(larger(10,47))


# age = int(input('Enter your age '))
# dave = lambda age: "you are welcome to the party" if age>18 else "you are not allow here"
# print(dave(age))

# sorting with lambda
# names=['Alan', 'Gregory', 'Zlatan', 'Jonas','Tom','Augustine']
# names.sort(key=lambda k:len(k))
# print(names)

# names=['Alan', 'Gregory', 'Zlatan', 'Jonas','Tom','Augustine']
# names.sort(key=lambda y:(y))
# print(names)

### map

# nums=[2,4,6,8,10,12]
# double=map(lambda x: x*2,nums)
# print(list(double))

# import statistics as st

# def desc(sample):
#     return st.mean(sample), st.median(sample), st.mode(sample)
# sample = [10,2,4,7,3,9,8,6,7]
# print(desc(sample))

people = ['Dacy','Christiana','Diana','Annabel']
# peep = map(lambda x:x.upper(),people)
# print(list(peep))

# list=[]
# for peoples in people:
#     person=peoples.upper()
#     list.append(person)
# print(list)
   
# names=[
#     {'first':'David','Last':'shuaib'},
#     {'first':'John','Last':'Doe'},
#     {'first':'Austine','Last':'Ugbodaga'}
# ]

# first_name=list(map(lambda x:x['first'],names))
# last_name=list(map(lambda x:x['last'],names))
# print(first_name)
# print(last_name)

 
  ########## Filter method 

# def filters(a):
#     return a%2==0
# l = [1,2,3,4,5,6,7,8]
# even = list(filter(filters,l))
# print(even)


# users=[
#     {'username':'Samuel','tweets':['I love cake','I love pie']},
#     {'username':'katie','tweets':['I love cat']},
    
#     {'username':'Jeff','tweets':[]},
#     {'username':'bob123','tweets':[]},
#     {'username':'katie','tweets':['Dogs are the best','I am hungry']},
#     {'username':'Felicia','tweets':[]},
# ]

# username=list(map(lambda user: user['username'].upper(),filter(lambda u : not u['tweets'],users)))
# print(username)


###   python maths
# import math
# a=int(input('Enter a number\n'))
# result=math.sqrt(a)
# print(result)

# a=int(input('enter your base number\n'))
# b=int(input('enter your index number\n'))

# x=math.pow(a,b)

# x=math.ceil(2.6)
# y=math.floor(2.6)
# print(x)     
# print(y)   

import requests  

# res=requests.get('https://news.ycombinator.com/')
# print(res)

# x=res.ok
# print(x)
    
# x=res.headers
# print(x)

# x=res.text
# print(x)


# url='https://www.google.com/'
# response=requests.get(url)
# print(f'Your request to {url} came back with status code {response.status_code}')
    
# url='https://icanhazdadjoke.com/'
# response=requests.get(url, headers={'accept':'text/plain'})
# print(response.text)

# response=requests.get(url, headers={'accept':'application/json'})
# data=response.json()
# print(data['joke'])
# print(data['id'])
    
# url='https://icanhazdadjoke.com/search'
# response=requests.get(url, headers={'accept':'text/plain'})
# print(response.text)

# response=requests.get(url, headers={'accept':'application/json'},params={'terms':'girl','limit':2}).json()
# print(response)
# print(response['joke'])


# import requests
# from random import choice
# from pyfiglet import figlet_format
# from termcolor import colored
# header = figlet_format('MY JOKE API')
# header = colored(header,color='magenta')
# print(header)
# user_input = input('what do you want to search for\n')  
# url='https://icanhazdadjoke.com/search'
 
# response=requests.get(url, headers={'accept':'application/json'},params={'term':user_input}).json()
# # print(response)
# num_jokes=response['total_jokes']
# results=response['results']
# if num_jokes>1:
#     print(f'I found {num_jokes} joke(s) about {user_input}, Here is one of them')
#     print(choice(results)['joke'])
    
# elif num_jokes == 1:
#     print(f'I found one joke about {user_input}. Here is it')
#     print(results[0]['joke'])
    
# else:
#     print(f'sorry, could\'t find any joke with your term {user_input}')

# a = int(input('enter the side of triangle A\n'))
# b = int(input('enter the side of triangle B\n'))
# c = int(input('enter the side of triangle C\n'))

# def type_of_triangle(a,b,c):
#     if a==b and b==c:
#         print('it is an ideal trangle')
        
#     elif a==90 or b==90 or c==90:
#         print('it is a right angle')
    
#     elif a==b or b==c or a==c:
#         print('it is an isoselece')   
#     else:
#         print('it is scalen') 
        
# type_of_triangle(a,b,c)

# import math
# def triangle():
#     count=0
#     degree=[]
#     while count<3:
#         angle=int(input('Enter an angles for the triangle\n'))
        
#         degree.append(angle)
        
#         summation=sum(degree)
#         count +=1
        
#         if summation==180:
#             print('An ideal triangle')
    
#     if summation==180:
        
#         if(degree[0] == degree[1] and degree[0]==degree[2] and degree[1]== degree[2]):
#             print('An equilateral triangle')
            
#         elif(degree[0] == degree[1] and degree[0] != degree[2] or degree[0] == degree[2] and degree[0] != degree[1] or degree[1] == degree[2] and degree[1] != degree[0]):
#          print('An isosceles triangle')
            
#         elif(degree[0] == 90 or degree[1]== 90 or degree[2]== 90):
#             print('A right angled triangle')
            
#         elif(degree[0] != degree[1] and degree[0] !=degree [2] or degree[1] != degree[2]):
#             print('An scalene triangle')
            
#         else:
#             print('Enter a valid angle')    

#     else: 
#         print('enter a valid angle') 
            
# triangle()


from datetime import datetime
from playsound import playsound
alarm_time = input("Enter the time of alarm to be set:HH:MM\n")
alarm_hour = alarm_time[0:2]
alarm_minute = alarm_time[3:5]
alarm_seconds = alarm_time[6:8]
alarm_period = alarm_time[9:11].upper()
print("setting up alarm..")
while True:
    now = datetime.now()
    current_hour = now.strftime("%I")
    current_minutes = now.strftime("%M")
    current_seconds = now.strftime("%S")
    current_period = now.strftime("%p")
    if(alarm_period==current_period):
        if(alarm_hour==current_hour):
            if(alarm_hour==current_minutes):
                if(alarm_seconds==current_seconds):
                    print("Wake Up")
                    playsound('audion.mp3')
                    break
    





        
    
    
    
    



            
    
    
