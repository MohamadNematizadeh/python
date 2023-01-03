import pyfiglet
from class_media import Media
from class_media import Actor
from class_actor import Film
from class_actor import Series
from class_actor import Clip
from class_actor import Documentary

PRODUCTS = []
def Title():
    title = pyfiglet.figlet_format("MediaMohamad@-@",font="slant")
    print(title)
#  ._._._._._._._._._._._.
def read_from_databse():
     f=open("deata_media_mohammad.text","r")
     for line in f:
        result = line.split(",")
        my_dict = {"id": result[0],"name_filem":result[1],"duration":result[2]}
        PRODUCTS.append(my_dict)
     f.close()
#  ._._._._._._._._._._._.
def Show_menu():
        print("1-Add") 
        print("3-Removoe")    
        print("4-Search")
        print("5-Show List")
        print("6-Exit") 
#  ._._._._._._._._._._._.

def Add():
    id = input("enter code: ")
    name_filem = input("enter name: ")
    duration = input("enter duration: ")
    new_product = {"id": id,"name_filem":name_filem,"duration":duration}
    PRODUCTS.append(new_product)
#  ._._._._._._._._._._._.
def Serch():
    print("1-Search With Name_filem id ")
    print("2-Search With Duration ")
    choice=int(input("Which Method do You Want to Search : "))
    if choice==1:
        userKey=input("Pls Enter Media Id : " )
        f=0
        for i in range(len(PRODUCTS)):
            if str(PRODUCTS[i]['id'])==userKey or (PRODUCTS[i]['name_filem'].lower()==userKey.lower()) :
                print(PRODUCTS[i])
                f=1
        if f==0:   
            print("Media Not Found!")
    elif choice==2:
        print("Duration between A and B ")
        A=int(input("A : "))
        B=int(input("B : "))
        f=0
        for i in range(len(PRODUCTS)):
            if PRODUCTS[i]["duration"]>=A and PRODUCTS[i]["duration"]>=B :
                print(PRODUCTS[i])
                f=1
        if f==0:   
            print("Media Not Found!")      

    else:
        print('Try Again !')
#  ._._._._._._._._._._._.
def Show_list():
    print("id\t\t name_filem\t\t\t duration")
    for product in PRODUCTS:
        print(product["id"],"\t\t",product["name_filem"],product["duration"])    
#  ._._._._._._._._._._._.
def Remove():
    A = 0
    id = input("enter id: ")
    for product in PRODUCTS:
            code_a = A + 1
            if product["id"] == id:
                del PRODUCTS[A-1]
                print("Your item has been successfully deleted")
                break
    else:
            print("not found")
#  ._._._._._._._._._._._.

Title()
print("wellcom to medie mohammad")

print("Loading...")
read_from_databse()
print("Data Loaded.")

while True:
    Show_menu()
    choice = int(input("enter your choice: "))

    if choice == 1:
        Add()

    elif choice == 2:
        Edit()

    elif choice == 3:
        Remove()

    elif choice == 4:
        Serch()

    elif choice == 5:
        Show_list()

    elif choice == 7 :
        Exit(0) 
    else:
        print("dorost vared kon")


