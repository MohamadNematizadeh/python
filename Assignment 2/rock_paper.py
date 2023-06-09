import random
computer_Choice=0
user_Choice = 0
x = random.randint(1,3)
if x == 1:
    computer_Choice="rock"
elif x ==2:
   computer_Choice="paper"
elif x ==3:
   computer_Choice="scissors"   

user_Choice = input()

print("computer_Choice")
print("user_Choice")

if computer_Choice =="rock" and user_Choice == "paper":
    computer_Choice = user_Choice+1

elif computer_Choice =="rock" and user_Choice == "scissors":
   computer_Choice = computer_Choice+1 
elif computer_choice == "paper" and user_choice == "scissors" :
   user_score += 1
elif computer_choice == "paper" and user_choice == "rock" :
   computer_score += 1
elif computer_choice == "scissors" and user_choice == "rock" :
   user_score += 1
elif computer_choice == "scissors" and user_choice == "paper" :
 computer_score += 1    
print("computer score :" , computer_score)
print("user score     :" , user_score,)
count += 1
