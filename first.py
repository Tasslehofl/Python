#!/bin/python3

#Print string
print("Hello, world!") #double quotes
print('Hello, world!')# single quotes

print("""This string runs
multiple lines!""") #triple quote for multip-line

print("This string is "+"awesome!") #can also concatenate

print('\n') #new line

#MATH
print(50 + 50) #adding
print(50 - 50) #subtracting
print(50 * 50) #multiply
print(50 / 50) #divide
print(50 + 50 - 50 * 50 / 50) #PEMDAS
print(50 ** 2) #exponents
print(50 % 6) #modulo - takes what is left over.. the remainder
print(50 / 6) #division with decimals
print(50 // 6) #division with no leftovers / remainder
print('\n') #new line

#VARIABLES AND METHODS
quote = "All is fair in love and war"
print(quote)

print(quote.upper()) #uppercase
print(quote.lower()) #lowercase
print(quote.title()) #title case (capatilized every first letter)
print(len(quote)) #counts characters (including spaces)

name = "Quint" #string
age = 42 #int
gpa = 3.9 #float (has a decimal)

print(int(age))
print(int(30.1))
print(int(30.9)) #doesn't care what's on the right of the decimal..

print("My name is " + name + " and I am " + str(age) + " years old.")
#in order to convert an int to a string, you have to do the above.

age +=1 #can change variables.. in this case, added 1 to age
print(age)

birthday = 1
age += birthday
print(age)
print('\n') #new line

#FUNCTIONS - mini programs
print("Here is an example function:")
def who_am_i(): #this is a function
	name = "Quint"
	age = 42
	print("My name is " + name + " and I am " + str(age) + " years old.")
who_am_i()
#whatever is part of the function, stays in the function.. so like age, will stay here, and if you call it later, it won't work, or will use age somewhere else

print(age)

#adding parameter
def add_one_hundred(num):
	print(num + 100)
add_one_hundred(100)

#multiply paramters
def add(x,y):
	print(x + y)
add(7,7)

def multiply(x,y):
	return x * y #stores and can recall later
multiply (7,7)	
print(multiply (7,7))

def square_root(x):
	print(x ** .5)
square_root(64)

def nl():
	print('\n')
nl()

#BOOLEAN EXPRESSIONS (true or false)
print("Boolean expressions:")

bool1 = True
bool2 = 3*3 == 9
bool3 = False
bool4 = 3*3 != 9

print(bool1, bool2, bool3, bool4)
print(type(bool1)) #tells you what the printed line is.. in this case, boolen

bool5 = "True"
print(type(bool5)) #this one is a string, so it tells me it is a string

nl()

#Relational and Boolean Operators
greater_than = 7 > 5

less_than = 5 < 7
greater_than_equal_to = 7 >= 7
less_than_equal_to = 7 <= 7

test_and = (7 > 5) and (5 < 7) #true
test_and2 = (7 > 5) and (5 > 7) #false
test_or = (7 > 5) or (5 < 7) #true (one one value has to be true)
test_or2 = (7 > 5) or (5 > 7) #still true because only one has to be true)

test_not = not True #False

nl()
#CONDITIONAL STATEMENTS (if/else)
def drink(money):
	if money >= 2:
		return "You've got yourself a drink!"
	else:
		return "No drink for you!"
print(drink(3)) #if you have $3 
print(drink(1)) #if you have $1

def alcohol(age,money):
	if (age >= 21) and (money >= 5): 
		return "We're getting a drink!"
	elif (age >= 21) and (money < 5):
		return "Come back with more money."
	elif (age < 21) and (money >= 5): 
		return "Nice try, kid!"
	else:
		return "You're too poor and too young!"
print(alcohol(21,5))
print(alcohol(21,4))
print(alcohol(20,5))
print(alcohol(20,4))

