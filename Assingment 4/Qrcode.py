import qrcode
nam= input("enter nam:")
a= float(input("enter namber:"))
img= qrcode.make("nam,a")
img.save("my_nam.png")
