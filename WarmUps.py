#New python File: Warmups.py

# 12.4.17
# Write a Python function
# which accepts the user's
# first and last name
# with a space between them.


def Name(first_name,last_name):
    print("%s, %s" % (last_name, first_name))


# 12.5.17
"""Write a function called add_py
that takes one parameter called "name"
and prints out name.py
"""


def add_py(name):
    print("%s.py" % name)


def add(num1, num2, num3):
    print(num1 + num2 + num3)


add(15, 18, 9000)
add(80, 90, 100)




# 12.7.17
# Write a function called ''repeat''
# that takes one parameter (string)
# and prints it three times
#
# example:
# repeat(''Hello'') prints:
# Hello
# Hello
# Hello


def repeat(string):
    for x in range(3):
        print(string)


