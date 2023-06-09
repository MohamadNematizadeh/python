import random


while True:
    input("Press entre to Dice")
    dice = random.randint(1, 6)
    print("your dice is: ", str(dice))

    if dice != 6:
        break