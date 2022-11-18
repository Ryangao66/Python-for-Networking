# price = 10
# rating = 4.9
# name = "Ryan"
# is_published = True
# print(print)
#
# print('=' * 40)
# Full_name = "John Smith"
# age = 20
# is_new = True
#
# name = input('What is your name? ')
# print('Hi ' + name)
#
# name1 = input('What is your name? ')
# color = input('What is your favorite color? ')
# print(name + ' Like ' + color)
#
print('=' * 40)

# birth_year = input("Birth year: ")
# print(type(birth_year))
# age = 2022 - int(birth_year)
# print(type(age))
# print(age)

# weight_in_pounds = input("Hi, What's your weight, lady? ")
# weight_in_kilo = int(weight_in_pounds) * 0.45
# print(weight_in_kilo)

#单引号和双引号的用法区别
# course = "Python's course for Beginners"
# print(course)
# course1 = 'Python for "Beginners"'
# print(course1[-1])
# print(course1[:6])
# course2 = '''
# Hi Laura,
#
# This is our first email to you.
#
# Thank you,
# The support team
'''
print(course2)

name = "Jennifer"
print(name[1:-1])

#John [smith] is a coder
first = 'John'
last = 'Smith'
message = first + " [" + last + "] " + "is a coder"
msg = f"{first} [{last}] is a coder"
print(message)
print(msg)
'''

# course = "Python for beginners"
# print(len(course))
# print(course.upper())
# print(course.find('P'))
# print(course.replace("beginners", "rookies"))
# print('th' in course)



# Arithmetic Operations
'''
print(10 ** 3)
x = 10
# x = x + 3
# x += 3
x -= 3
print(x)
'''

# Operator Precedence
'''
x = 10 + 3 * 2
print(x)
y = 10 + 3 * 2 ** 2
print(y)
'''

# Math Functions
'''
import math

x = 2.9
# print(round(x))
# print(abs(-2.9))

print(math.ceil(2.9))
print(math.floor(2.9))
'''

# If statements

'''
# is_hot = True
is_hot = False
# is_cold = True
is_cold = False

if is_hot:
    print("It's hot day!")
    print("Drink plenty of water!")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's lovely day")
print("Enjoy your day!")



# good_credit = True
good_credit = False
price = 1000000
if good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down Payment: ${down_payment}")



# Logical Operators

has_high_income = True
# has_good_credit = True
has_good_credit = False
if has_good_credit and has_high_income:
    print("Eligible for loan")
else:
    print("Need to think about this again")


temperature = 35
if temperature > 30:
    print("It's a hot day!")
elif temperature < 10:
    print("It's a cold day!")
else:
    print("It's neither hot nor cold!")


name = 75
if name <= 3:
    print("Name must be at least 3 characters.")
elif name >= 50:
    print("Name can be a maximum of 50 characters.")
else:
    print("Name looks good!!")


# Weight Converter

weight = int(input("Weight: "))
unit = input("(L)bs or (K): ")
if unit.upper() == "L":
    converted = weight * 0.45
    print(f"You are {converted} kilos")
else:
    converted = round(weight / 0.45)
    print(f"You are {converted} pounds")

input("start - to start the car")
input("stop - to stop the car")
input("quit - to exit")

# While Loop

i = 1
while i <=6:
    print("*" * i)
    i = i + 1
print("Done")



# Guseeing game

secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("Guess the number: "))
    guess_count += 1
    if guess == secret_number:
        print("Congrats, you won!!")
        break
else:
    print("Sorry, you failed!!")



# Racing car

weight = int(input("Weight: "))
unit = input("(L)bs or (K): ")
if unit.upper() == "L":
    converted = weight * 0.45
    print(f"You are {converted} kilos")
else:
    converted = round(weight / 0.45)
    print(f"You are {converted} pounds")


unit = input("start - to start the car \nstop - to stop the car\nquit - to exit ")
if unit() == "start":
    print("Car started....Ready to go!")
elif unit() == "stop":
    print("Car stopped...")
elif unit() == "quit":
    print("Gave over")
'''

command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car is already started!!! You IDIOT")
        else:
            started = True
            print("Car started...Ready to go!")
    elif command == "stop":
        if not started:
            print("Car is already stopped! Are you trying to break me, you NUTS")
        else:
            started = False
            print("Car stop...")
    elif command == "help":
        print('''
              start - to start the car 
              stop - to stop the car
              quit - to exit 
              ''')
    elif command == "quit":
        break
    else:
        print("I don't understand WTF is this, you biatch! try 'help' !!!")


