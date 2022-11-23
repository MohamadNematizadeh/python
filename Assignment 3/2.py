import random 
number = []
number2 = int(input("Enter your number : "))

Numbercounter = 0 

while  Numbercounter != n :


    r = random.randint(0 , 90)

    if r not in number:

       number.append(r)

       Numbercounter += 1 
       
print(number)