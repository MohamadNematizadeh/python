number=int(input(" Number:"))
for i in range(number):

    for j in range(number*2):

        if(number-i<=j<=number+i):

            print("*",end="")

        else: 
            print(" ",end="")
    print()

for i in range(number):

    for j in range(number*2):

        if(i+1<j<number*2-i-1):

            print("*",end="")
        else: 
            print(" ",end="")
    print()


