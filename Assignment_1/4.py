
#python_Assignment 1._./4

w = float(input("weight(kg): "))
f = float(input("height(meter): "))

BMI = round(w / (f/100)**2,3)

if BMI < 18.5:
    print("You are a thin person._./._./._./._.")
elif BMI>=18.5 and BMI<24.9:
    print("your weight is normal gret._./._./._.")
elif BMI>=25 and BMI<20.9:
    print("Reduce your weight ._./._.")

elif BMI>=30 and BMI<39.9:
    print("You are a fat person._.")
elif BMI>=35 and BMI<39.9:
    print("Your body is very fat")


