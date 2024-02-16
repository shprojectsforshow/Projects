#!/bin/python3
print("hello")
#yeet
print('\n')

#MATH
print(50+50)
print(50-50)
print(50*50)
print(50/50)
print('\n')

quote="all is fair"
print(quote.upper())
print(len(quote))


name="Scotter"
age = 27
gpa= 2.5 #float
print("My name is "+name+" and im " +str(age)+ " years old")
age += 1
print(age)
birthday = 1
age += birthday
print(age)

print('\n')

#functions
def who_am_i(): # function without parameters
	name = "Scooter" #local variable
	age=27
	print("My name is "+name+" and im " +str(age)+ " years old")
	
who_am_i()

def add_one_hundred(num):
	print(num+100)
	
add_one_hundred(100)

def add(x,y):
	print(x+y)
	
add(7,7)

def nl():
	print('\n')

nl()

#Boolean T/F

bool1=True
bool2=3*3==9
bool3=False
bool4=3*3 !=9

print(bool1,bool2,bool3,bool4)
print(type(bool1))
nl()

#relational  and boolean operators
greater_than=7>5
less_than=5<7
greater_than_equal_to=7>=7
less_than_equal_to=7<=7

test_and=(7 >5) and (5<7) #True
test_and2=(7>5) and (5<7) #false
test_or=(7>5)  or (5<7) #true
test_or2 =(7>5) or (5>7) #true

test_not=not True #false

nl()

#conditonal statements if/else

def drink(money):
	if money >=2:
		return "you bought drink"
	else:
		return "no drink"

print(drink(3))
print(drink(1))
nl()
def alcohol(age,money):
	if (age >= 21) and (money  >=2):
		return "drink allowed"
	elif (age>=21) and (money<5):
		return "broke"
	elif (age<21) and (money>=5):
		return "yikes"
	else:
		return "denied"
print(alcohol(21,3))
nl()
movies=["im gay", "iron man" , "iron giant", "madea"]
nl()

grades=[["bob",82],["alice",90],["jeff",64]]
bobs_grade=grades[0][1]
print(bobs_grade)
grades[0][1]=90
print(grades)
nl()

grades=("a","b","c")
nl()

#looping
#for  loops starts to finish of an iterate
veggie=["beans","gay","meat"]
for  x in veggie:
	print(x)
	
#while loop execute as long as True
i =1
while i<10:
	print(i)
	i+=1
nl()

my_name="scooter"
print(my_name[0]) #first letter

sentence="this sentence"

print(sentence[:4]) #if you know length of what you want
print(sentence.split()) #delimiter default for python is space

nl()

#dictonaries

drinks={"white":7,"old":10,"lemon":8}
print(drinks)
employees={"finance":["bob","linda","tina"],"IT":["gene","Louise","ted"],"HR":["jimmy","mort"]}
print(employees)
employees['legal']=["frond"]
print(employees)
employees.update({"Sales":["andie","ollie"]})
print(employees)

drinks.['white']=8
print(drinks)
