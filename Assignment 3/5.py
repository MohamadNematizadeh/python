first= int(input("enter First number :"))

second= int(input("enter second number :"))


if first > second : 
     number = second
else: 
     number = first
for i in range(1, number+1): 
    
      if((first % i == 0) and (second % i == 0)): 
            B. M. M = i  
   

print ("The gcd value is :" , B. M. M)
