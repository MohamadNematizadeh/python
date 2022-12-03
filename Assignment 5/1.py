n=int(input("Enter the number: "))


m=int(input("Enter the number: "))


def number(n,m):

    for m1 in range (m):
        for mi in range(3,n + 3):
            if m1%2 == 1:
                if mi%2 == 1:
                    print('*', end = '')
                else:
                    print('#', end = '')
            else:
                if mi%2 == 1:
                    print('#', end = '')
                else:
                    print('*', end = '')
print(number(n, m))              
