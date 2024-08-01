class Fraction:
    def __init__(self, nr, dr=1):
        self.nr = nr
        self.dr = dr
        if self.dr < 0:
            self.nr *= -1
            self.dr *= -1
        self.simplify()

    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def simplify(self):
        common_divisor = self.gcd(self.nr, self.dr)
        self.nr //= common_divisor
        self.dr //= common_divisor

    def show(self):
        print(f'{self.nr}/{self.dr}')

    def multiply(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        result = Fraction(self.nr * other.nr, self.dr * other.dr)
        result.simplify()
        return result
    
    def add(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        new_nr = self.nr * other.dr + other.nr * self.dr
        new_dr = self.dr * other.dr
        result = Fraction(new_nr, new_dr)
        result.simplify()
        return result
        
f1 = Fraction(2, 3)
f1.show()
f2 = Fraction(3, 4)
f2.show()
f3 = Fraction(6, 12)
f3.show()

# Adding two fractions
f4 = f1.add(f2)
f4.show()

# Adding a fraction and an integer
f5 = f1.add(5)
f5.show()

# Multiplying a fraction by an integer
f6 = f1.multiply(5)
f6.show()
