import math
print("welcom")
while 1==1:
    print("+:sum")
    print("-:sud")
    print("*:mul")
    print("/:div")
    print("sin")
    print("log")
    print("pleas")
    print("cos")
    print("tan")
    print("cot")
    print("factorial")
    print("sqrt")
    op = input()
    
    if op == "ex":
        print("good bye")
        break 

    if op == "+" or op=="-" or op=="*" or op=="/":
     a=float(input("first number:"))
     b=float(input("second number:"))
    else:
     a=float(input("first number:"))

    if op =="+":
        result = a+b

    elif op =="-":
        result = a - b

    elif op =="*":
        result=a*b

    elif op =="/":
        if b == 0 :
            result = "Cannot divide by zero"
        else:
         result = a/b         
    elif op == "sin":
        result = math.sin(a)
    elif op == "log":
        result = math.log(a)
    elif op=="cos":
        a * 0.0174532925
        print(math.cos(a))
    elif op==tan:   
        a * 0.0174532925
        print(math.tan(a))
    elif op==cot:   
        a * 0.0174532925
        print(1 / math.tan(a))
    elif op==sqrt :
        print(math.sqrt(a))  
   

    print(result)