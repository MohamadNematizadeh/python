class Time:
    def __init__(self,hh,mm,ss):
        self.hour = hh
        self .minute= mm
        self.second = ss 
        self.fix()

    def show(self):
        print(self.hour,":",self.minute,":",self.second)

    def sum (self, zammzn_2):
        s =self.second+zammzn_2.second
        m =self.minute+zammzn_2.minute
        h =self.hour+zammzn_2.hour
        result = Time(h,m,s)
        return result

    def sud (self, zammzn_2):
         s =self.second-zammzn_2.second
         m =self.minute-zammzn_2.minute
         h =self.hour-zammzn_2.hour
         result = Time(h,m,s)
         return result
    @staticmethod
    def convert_second_to_time(second):
        x = Time(0, 0, second)
        return x


    def convert_time_to_second(self):
        second = (self.hour * 60 + self.minute) * 60 + self.second
        return second
        
    def convert_GMT_to_Tehran(self):
        Tehran = Time(3, 30, 0)
        x = Time.sum(self, Tehran)
        # t = Time(30, 30, 0)
        # x = self.sum(t)
        return x
        
    def fix(self):
        if self.second>=60:
            self.second-=60
            self.minute +=1

        if self.minute>=60:
            self.minute-=60 
            self.hour+=1 

        if self.second<0:
            self.second+=60 
            self.minute-=1     

        if self.minute<0:
            self.minute+=60 
            self.hour-=1     

    def gmt_to_tehran(self):
        tehran_time=self.sum(Time(3, 30,0))
        return tehran_time
    
    def time_to_secods(self):
        secands = self.hour*3600 + self.minute * 60 + self.second
        return secands
    @staticmethod
    def secods_to_time(self):  
        hour = secands//3600
        secands = secands-(hour*3600)
        minute = secands // 60
        secands = secands - (minute*60)
        secand = secands
        t=Time(hour, minute, secand)
        return t
        


     
t1 =Time(3, 45, 17)
t1.show()
t2 =Time(4, 13, 2)
t2.show()
t3 = t1.sum(t2)
t3.show()
# gmt_tehran
t4=t3.gmt_to_tehran()
t4.show()
t5=t4.time_to_secods()
print(t5)