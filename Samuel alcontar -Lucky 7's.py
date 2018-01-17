import random
TopMoney = 0
best_Turn = 0
money = 15
plays = 0
while money > 0:

    if TopMoney < money:
        TopMoney = money
        best_Turn = plays

    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    print("The first dice is %d" % dice1)
    print("The second dice is %d" % dice2)
    total = dice1 + dice2
    print("the amount of dots is %d" % total)

    if total == 7:
        money += 4
        plays += 1
    else:
        money -= 1
        plays += 1
    print("the money you have left is %d" % money)
    print(" the total after each roll is %d" % total)
    print(plays)
print("it took you %s turns to run out of money." % plays)
print("On turn %s you had the most money %s" % (best_Turn, TopMoney))