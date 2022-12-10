PRODUCTS = []

def read_from_databse():
    f=open("databast.text","r")
    for line in f:
        result = line.split(",")
        my_dict = {"code":result[0],"name":result [2], "count":result[3]}
        PRODUCTS.append(my_dict)
    f.close()


    

def show_menu():
    print("1-Add")    
    print("2-Edit")    
    print("3-Removoe")    
    print("4-Search")
    print("5-Show List")
    print("6-Buy")
    print("7-Exit")    

def add():
    code = input("enter code:")
    name = input("enter name:")
    price = input("enter price:")
    count = input("enter count:")
    new = {'code':code, 'name':name,'price':price,'count':count }
    PRODUCTS.append(new)

def Edit():
  while True:
        edit_from_name = input("Enter name product:\n")
        for i in range(len(PRODUCTS)):
            if edit_from_name == PRODUCTS[i]["name"]:
                edit_item = int(input('1.Edit id\n 2.Edit name\n 3.Edit price\n 4.Edit count\nEnter number:'))
                if edit_item == 1 :
                    PRODUCTS[i]["id"] = input("Enter new id:\n")
                elif edit_item == 2 :
                    PRODUCTS[i]["name"] = input("Enter new name:\n")
                elif edit_item == 3 :
                    PRODUCTS[i]["price"] = input("Enter new pice:\n")
                elif edit_item == 4 :
                    PRODUCTS[i]["count"] = input("Enter new count:\n")
        edit_repeat = input('do you edit enother product(Y/N):')
        if edit_repeat == 'n' or 'N':
            break
def Removoe():
    pass

def Search():
    user = input("type your:")
    for product in PRODUCTS:
        if product["code"] == user or product["name"]==user:
            print(product["code"],"/t",product["name"],"",product["price"])
            break
    else:
        print("not found")        

def Show_list():

    print("code/neme/price")
    for product in PRODUCTS:
         print(product["code"],"/t",product["name"],"",product["price"])

def Buy():
    ...


print("Wellcom to Mohammad Store")
print("Loading...")
read_from_databse()
print("Data Loaded.")
while True:
    show_menu()

    choice = int(input("enter your Choice:"))

    if choice == 1 :
        add()
    elif choice == 2 :
        Edit()
    elif choice == 3 :
        Removoe()
    elif choice == 4 :
        Search()
    elif choice == 5 :
        Show_list()  
    elif choice == 6 :
        Buy()
    elif choice == 7 :
        Edit()     

# ._._._._._._._._._._._._._._.
# for product in PRODUCTS:  
#     print(product)
