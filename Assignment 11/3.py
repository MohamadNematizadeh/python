class Complex_numpu:
    def __init__(self, real, image):
        self.real = real
        self.image = image

    def show(self):
        sign = '+'
        if self.image < 0:
            sign = '-'
        print(self.real, sign, f'i{abs(self.image)}')

    def sum(self, other):
        x = Complex(self.real + other.real, self.image + other.image)
        return x

    def sub(self, other):
        x = Complex(self.real - other.real, self.image - other.image)
        return x

    def mul(self, other):
        real = self.real * other.real - self.image * other.image
        image = self.real * other.image + self.image * other.real
        x = Complex(real, image)
        return x
        
a = Complex_numpu(-4 , 6)
a.show()

b = Complex_numpu(6 , -9)
b.show()        
