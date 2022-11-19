#python_Assignment 1._./3
from PIL import Image,ImageTk
print("Welcome_to_ferdowsi_university_student_system")
first_name_and_last_name = input("first_name_and_last_name")
S1 = float(input())
S2 = float(input())
S3 = float(input())
GPA=(S1+S2+S3)/3
print(f"{first_name_and_last_name} average = {GPA}")
if GPA >= 17:
    print(f"{first_name_and_last_name} Well done")
elif GPA < 17 and GPA >= 12:
      print(f"{first_name_and_last_name} Is it good")
elif GPA < 12:
    print(f"{first_name_and_last_name}You did not pass")

photo_bg = PhotoImage(file=r'E:\python\جلسه اول\aq\img\ds.png')
label_bg =Label(window,image=photo_bg)
label_bg.place(x=1,y=1)