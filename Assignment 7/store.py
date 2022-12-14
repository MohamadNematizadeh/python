import pyfiglet
def Title():
    title = pyfiglet.figlet_format("Mohamad Store@-@",font="slant")
    print(title)
PRODUCTS = []
def read_from_databse():
     f=open("databast.text","r")
     for line in f:
        result = line.split(",")
        my_dict = {"code":result[0],"name":result [2], "count":result[3],"price": result[2]}
        PRODUCTS.append(my_dict)
     f.close()
# .-.-.-.-.-.-.-.-.-.-.-.
def show_menu():
    print("1-Add") 
    print("2-Edit")    
    print("3-Removoe")    
    print("4-Search")
    print("5-Show List")
    print("6-Buy")
    print("7-Exit")    
# .-.-.-.-.-.-.-.-.-.-.-.
def add():
    code = input("enter code:")
    name = input("enter name:")
    price = input("enter price:")
    count = input("enter count:")
    new = {'code':code, 'name':name,'price':price,'count':count }
    PRODUCTS.append(new)
# .-.-.-.-.-.-.-.-.-.-.-.
def Edit():
        id = int(input("enter your code:"))
        for i in range(len(PRODUCTS)):
            if PRODUCTS[i]['code']==id:
             while True:
                  print("1-Edit code")    
                  print("2-Edit name")    
                  print("3-Edit price")  
                  edit=int(input("Pls Choose from Edit Menu : "))
                  if edit == 1:
                    name=input("Pls Enter New Name : ")
                    PRODUCTS[i]['Name']=name
                    print("Product Edited Successfully!")
                  elif edit==2:
                    price=float(input("Pls Enter New Price : "))
                    PRODUCTS[i]['Price']=price
                    print("Product Edited Successfully!")
                  elif edit==3:
                    count=int(input("Pls Enter New Count : "))
                    PRODUCTS[i]['Count']=count
                    print("Product Edited Successfully!")
                  elif edit==4:
                    break
                  else:
                    print("Value Error ,Try Again !")
# .-.-.-.-.-.-.-.-.-.-.-.
def Removoe():
        A = 0
        code = input("enter code: ")
        for product in PRODUCTS:
            code_a = A + 1
            if product["code"] == code:
                del PRODUCTS[A-1]
                print("Your item has been successfully deleted")
                break
        else:
            print("not found")
# .-.-.-.-.-.-.-.-.-.-.-.
def Search():
    user = input("type your:")
    for product in PRODUCTS:
        if product["code"] == user or product["name"]==user:
             print(product["code"],"\t",product["name"],"\t",product["count"])
             break
    else:
        print("not found")        
# .-.-.-.-.-.-.-.-.-.-.-.
def Show_list():
     print("cod\tname\tcount")
     for product in PRODUCTS:
        print(product["code"],"\t",product["name"],"\t",product["count"])
# .-.-.-.-.-.-.-.-.-.-.-.
def QR_code():
    code_qr = input("code: ")
    for product in PRODUCTS:
        if product["code"] == code_qr:
            img = qrcode.make(product)
            img.save("product_qr.png")
            break
    else:
        print("not found")
# .-.-.-.-.-.-.-.-.-.-.-.
def Buy():
    ...
Title()
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
        Exit(0)     

# ._._._._._._._._._._._._._._.
# for product in PRODUCTS:  
#     print(product)
