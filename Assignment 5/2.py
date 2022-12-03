n=int(input("Enter the number 2; "))
m=int(input("Enter the number 2; "))

def nest(n,m):
    for ii in range(n+1):

        for m in range(m+1):

            if(ii==0):

                if(m==0):
                    
                    print("x",end=" ")
                else:
                    print(m,end=" ")
            elif(m==0):
                    print(ii,end=" ")
            else: 
                print(ii*m,end=" ")
    
nest(n, m)
   
