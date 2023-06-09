
seconds = int(input("enter seconds: "))

hour = seconds//3600
minute = (seconds - hour * 3600)//60
second = (seconds - hour * 3600 - minute*60)%60
print("Time is: ", str(hour),":", str(minute),":", str(second))