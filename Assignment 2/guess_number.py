import random
us=0
computer_number= random.randint(10 , 40)
while True:
    us+=1
    user_number = int(input())

    if computer_number == user_number:
        print("barikala")
        break
    

    elif computer_number>user_number:
        print("boro bala")
        
    elif computer_number < user_number:
        print("bia peen") 
print("The number of your guesses:",us)      
     
