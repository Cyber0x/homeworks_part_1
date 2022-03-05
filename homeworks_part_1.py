#3.2
# Write the code to do following:
# Create any variable with name var1
# Check type of var1 with type function
# Check is var1 is True
# Check is var1 is False
# Create var2 that equal to (var1 or True)
# Check is var2 is True
# Check is var2 is False
# Check result for var2 and var1
var1= 10
print(type(var1))
print(var1 is True)
print(var1 is False)
var2= var1 or True
print(var2 is True)
print(var2 is False)
print( var1 and var2)



#3.3
# Write the code to perform following task:
# Generate sequence 5 integers long from range(0, 100)
# Generate random float
# Print variables above
# Find max element from generated sequence
# Make a floor division between max element and generated float
# Find factorial of the result above
# Shorten the code as much as possible
import random
import math
random_number=random.sample(range(100),5)
float_number=random.random()
print(random_number)
print(float_number)
max_number=max(random_number)
print(max_number)
float_division=max_number//float_number
print(float_division)
def factorialOTfloatDivision (float_division):
    if float_division == 0:
        return 1
    return float_division*(float_division-1)
print(factorialOTfloatDivision(float_division))



#except
#try:
    #x=int (input())
#except ValueError:
    #print('Вы ввели строку')
#try:
   # y=int (input())
#except ValueError:
    #print('Вы ввели строку')
#try:
    #res= x/y
#except ZeroDivisionError:
  # print('Вы ввели 0')
#except NameError:
   # print('Вы ничего не ввели')



# 3.4
# Write the code to do following:
# Generate string with lowercase and uppercase alphabet plus numbers
# Print 1st symbol of string
# Print last symbol
# Print 3rd from start and 3rd from the end
# Slice first 8 symbols
# Print only symbols with index, which divides on 3 without remaining - каждый 3ий символ
# Print the symbol of the middle of the string text
# Reverse text using slice
import string
textrandom=string.ascii_letters+string.digits
print(textrandom[0])
print(textrandom[-1])
print(textrandom[2])
print(textrandom[-3])
print(textrandom[:8])
print(textrandom[::3])
print(textrandom[int(len(textrandom)/2+0.5)])
print(textrandom[::-1])



# 3.5
# Write the code to do following:
# Generate string with lowercase and uppercase alphabet plus numbers
# Print 1st symbol of string
# Print last symbol
# Print 3rd from start and 3rd from the end
# Slice first 8 symbols
# Print only symbols with index, which divides on 3 without remaining
# Print the symbol of the middle of the string text
# Reverse text using slice
lst = list(string.ascii_letters + string.digits)
print(lst[0])
print(lst[-1])
print(lst[2])
print(lst[-3])
print(lst[:10])
print(lst[::2])
int_lst = []
for i in lst:
    try:
        int_lst.append(int(i))  # Здесь можно конвертировать только целое число
    except:
        pass
print(int_lst)
print(int_lst[::-1])
print("-".join(lst))



# 3.6
# Write the code to do following:
# create dict with 5 items, where keys will be country name and value -domain name, i.e. {Ukraine:UA}
# create another dict with 5 items, where values of countries will be keys, and values will be the capitals i.e. {'UA': 'Kiev'}
# add one more element to each dict above
# print sentence "Domain for COUNTRY is DOMAIN." for each record in countries with the replace from dicts
# print sentence "The capital of COUNTRY is CAPITAL" for each record in capitals with the replace from dicts
# Merge sentences above together with one cycle
# Add to each value of first dict another two domains: COM and GOV
countries = {
    'Ukraine': 'UA',
    'Israel': 'IL',
    'Japan': 'JP',
    'United States': 'US',
    'Sweden': 'SE'
}
capitals = {
    'UA': 'Kiev',
    'IL': 'Jerusalem',
    'JP': 'Tokyo',
    'US': 'Washington',
    'SE': 'Stockholm'
}
countries['Italy'] = 'IT'
capitals['IT'] = 'Rome'
for key, value in countries.items():
    print("Domain for {} is {}.".format(key, value))
for key, value in capitals.items():
    print("The capital of {} is {}".format(key, value))
for key, value in countries.items():
    print("Domain for {} is {}.The capital is {}".format(key, value, capitals[value]))
for key, value in countries.items():
    countries[key] = [value, 'COM', 'GOV']
for key, value in countries.items():
    print("Domain for {} is {}.The capital is {}".format(key, value, capitals[value[0]]))



#3.7
# Write the code to do following:
# Generate two sets with not unique numbers and few symbols
# Print 1st set
# Create tuple from intersection of first and second set
# Create tuple from difference first and second set
# Slice first 3 symbols from first tuple
# Print only symbols with numbers from second set
# Reverse tuple using slice
# Convert both tuples into list
set_1=set(string.ascii_letters + string.digits[3:7] + string.digits[:5])
set_2=set(string.ascii_letters + string.digits[3:7] + string.digits[6:])
print(set_1)
print(set_2)
tpl_intersection=tuple(set_1.intersection(set_2))
tpl_difference=tuple(set_1.difference(set_2))
print(tpl_intersection)
print(tpl_difference)
print(tpl_intersection[:3])
print(set(string.digits).intersection(set_2))
print(tpl_intersection[::-1])
print(list(tpl_intersection),list(tpl_difference))



#4.4
# Write a program, which takes a year as input and returns message if this is a leap year or note.
# Please handle the exceptions which may arise is a user will enter non-numeric symbols.
# Additional task – to show the closest leap year in case if entered year is not leap
# Optional task - Add a possibility to print all the leap years within given range
while True:
	response = (input('Do you want to enter the range? (Y/N) '))
	if response == 'Y':		# If a user wants to see all leap years within the range
		start_year = int(input('Enter the start year: '))
		end_year = int(input('Enter the end year: '))
		for year in range(start_year, end_year + 1):		# Checking all years within the range
			if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
				print('Leap year is: {}'.format(year))
		break
	else:
		year = int(input('Enter the year to check: '))
		if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):   # if year divides to 4 and (100 or 400) without remaining it's a leap year
			print('It is a leap year! 366 days in a year!\n')
		else:
			print('It is not a leap year! 365 days in a year!\n')
			for item in (year + 1, year -1, year + 2, year - 2, year + 3, year -3 ):  # Check close years is they are leap.
				if (item % 4 == 0) and (item % 100 != 0) or (item % 400 == 0):
					print ('The closest leap year is: {}'.format(item))
					break
	break



# some classwork
import time
def printer(func):
    def wrapped(*args,**kwargs):
        print('in wrapped')
        current_time_1=time.time()
        b=func(*args,**kwargs)
        current_time_2=time.time()
        print(current_time_2 - current_time_1)
        return b
    return wrapped

@printer
def some():
    time.sleep(2)
    return 1



# some classwork
#import argparse
#def some (args):
   # print(args)
   # return args[-1]
#parser = argparse.ArgumentParser(description='something')
#parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer for the accumulator')
#parser.add_argument('-sum', dest='accumulate', action='store_const', const=sum, default=some,
    #                help='sum the integers(default: find the max)')
#args = parser.parse_args()
#print(args.accumulate(args.integers))


#print(args)



#4.6
# Write a program that will take username and password, checks if they are in registered,
# users dictionary, if they are present – print “Access Granted”, if not – handle it using
# KeyError Eception handling. Raise RuntimeError and handle it if the name is empty.
# For registered user, which is logged - let him know if their password has unacceptable,
# symbols (non alphanumeric) and propose to change it using a dialog.
import string
import getpass
authorized_users={'OTOVI':'BYp9y9r9',
                'DAN':'e22bEp3V',
                'VIROHELM':'TEks679h',
                'ERMEGOL':'rL42dTf9'}

while True:
    try:
        name = input('Please enter your name: ')
        if name == '':
            raise RuntimeError
        print('Hello, {}'.format(name))
        password = getpass.getpass('Please enter your password: ')
        if authorized_users[name] == password:
            print('Access Granted!')
            break
    except KeyError:
        print("There's no such user registered!")
    except RuntimeError:
        print('Empty names are considered as a breach try!')

for symbol in authorized_users[name]:
    if symbol in string.punctuation:
        new_password = getpass.getpass(
            'Your password has unacceptable symbol in it: {} Please change your password: '.format(symbol))
        authorized_users[name] = new_password
        print('Your password is successfully updated!')



class Pet:
    def __init__(self, name, pet_type, age, wool):
        self.name = name
        self.__pet_type = pet_type
        self.age = age
        self.wool = wool

    def rename(self, new_name):
        self.name = new_name
        return new_name

    def __gt__(self, other):
        if isinstance(other, Pet):
            return self.age > other.age
        raise NotImplemented


    def pet_type(self):
        return self.__pet_type

a = Pet('Alex', 'cat', 10, '')
b = Pet('Sanek', 'dog', 3, '')

class Dog(Pet):
    def bark(self):
        print('bark!')

dog = Dog('Gerom', 'Sharpey', 10, 'wool=yes')

print(dog.name, dog.pet_type(),dog.wool)
dog.bark()