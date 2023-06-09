import array
array.array('i')

number = int(input("enter your number:"))

if number == 1:
    print("1")
elif number == 2:
    print("1, 1")
elif number > 2:
    Fibonacci = array.array('i',(0 for i in range(0,number)))

    Fibonacci[0] = 1
    Fibonacci[1] = 1
    print("1, 1", end=", ")
    for i in range(2, number):
        Fibonacci[i] = Fibonacci[i - 1] + Fibonacci[i - 2]
        print(Fibonacci[i], end= ", ")