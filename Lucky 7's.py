import random
dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)
print("The first dice is %d" % dice1)
print("The second dice is %d" % dice2)
total = dice1 + dice2
print("the amount of dots is %d" % total)
money = 15

while money > 0:


    if total == 7:
        money += 4
    else:
        money -= 1
    print("the money you have left is %d" % money)
    print (" the total after each roll is %d" % total)