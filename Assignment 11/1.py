
class Fraction_number:
    def __init__(self, ss, mm):
        self.s = ss
        self.m = mm

    def sum(self, other):
        result_s = self.s * other.m + self.m * other.s
        result_m = self.m * other.m
        x = Fraction(result_s, result_m)
        return x

    def sub(self, other):
        result_s = self.s * other.m - self.m * other.s
        result_m = self.m * other.m
        x = Fraction(result_s, result_m)
        return x

    def mul(self, other):
        result_s = other.s * self.s
        result_m = other.m * self.m
        x = Fraction(result_s, result_m)
        return x

    def div(self, other):
        result_s = other.m * self.s
        result_m = other.s * self.m
        x = Fraction(result_s, result_m)
        return x

    def fraction_to_number(self):
        return self.s / self.m

    def greatest_common_divisor(self):
        Greatest_Common_Divisor = 1
        Divisors1 = []
        Divisors2 = []

        for i in range(1,self.s + 1):
            if (self.s / i).is_integer():
                Divisors1.append(i)
                
        for i in range(1,self.m + 1):
            if (self.m / i).is_integer():
                Divisors2.append(i)
                if i in Divisors1:
                    Greatest_Common_Divisor = i

        return Greatest_Common_Divisor

    def simplify_the_fraction(self):
        GCD = Fraction.greatest_common_divisor(self)
        x = Fraction(self.s / GCD, self.m / GCD)
        return x
    
    def show(self):
        print(self.s, '/', self.m)
a=2
b=0

c=7
d=1

a = Fraction(31, 93)
a.show()

b = Fraction(23, 69)
b.show()

z = b.simplify_the_fraction()
# print(z)
z.show()

