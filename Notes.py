# print("Hello world")
# # Samuel Alcontar
# A = 4
# B=3
# print(3+5)
# print(3*5)
# print(3-5)
# print(3 ** 2)
#
# print()
# print(" try to figure out how this works")
# print(13 % 12)
# # the "%" sign is a modulus. It finds the remainder.
# car_name = "The wiebe mobile"
# car_type = "BMW"
# car_cylinder = 8
# car_mpg = 5000.9
#
# print("I have a car called %s. its a pretty nice." % (car_name)) # watch the order
#
# # here is where we get a little fancy
# print("What is your name?")
# name = input(">_")
# print("Hello %s." % name)
#
# age = input("How old are you?")
# print("%s?! That's really old. You belong in a retirement Home")
#
# print("Your rude!")

# Functions



def print_hw():
    print("Hello World!.")
    print("Enjoy the day.")


print_hw()


def say_hi(name): # Name is a ''parameter''
    print("Hello %s" % name)
    print("Coding is Great!")



say_hi("Samuel")



def print_age(name,age):
    print("%s is %d years old" % (name, age))
    age += 1 #age = age + 1
    print("Next year, %s will be %d years old" % (name, age))


print_age("He",14)


def algebra_hw(x):
    return x**3 + 4*x**2  + 7 * x - 4

print(algebra_hw(3))
print(algebra_hw(4))
print(algebra_hw(5))
print(algebra_hw(6))
print(algebra_hw(7))


# if statements

def grade_calc(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 80: # else if
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"


print(grade_calc(100))


def happy_bday(name):
    print("Happy birthday to you")
    print("Happy birthday to you")
    print("Happy birthday dear " + name)
    print("Happy birthday to you")


happy_bday("Samuel")

# loops

for num in range(10):
    print(num + 1)
# While loops (BEWARE!!!!!)

a =1
while a < 10:# This is the condition,
               # it must be true to execute
    print(a)
    a += 1 # This iterates so that we can break the loop

# Random Numbers

import random # This should be on line 1
print(random.randint(0,1000))

#RECASTING
c = '1'
print(c == 1)
print(c == 1) # we have a string amd an integer
print(int(c) == 1)
print(c == str(1))

# COMPARISON

print(1 == 1) # use a double equal sign
print(1 !=2) #  1 is not equal to 2
print(not False)






import random
n = random.randint(0, 50)
print(n)
print("what is your guess")
guess = input (">_")
if n == guess:
    print("You win")


print(n)














import random
n = random.randint(1, 50)
guess = int(input("Enter a number from 1 to 50: "))
while n = "guess":
    print
    if guess < n:
        print("guess is low")
        guess = int(input("Enter a number from 1 to 50: "))
    elif guess > n:
        print("guess is high")
        guess = int(input("Enter a number from 1 to 50: "))
    else:
        print("you guessed it!")
        break
        print

