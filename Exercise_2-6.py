class Fraction:
    def __init__(self, nr, dr=1):
        self.nr = nr
        self.dr = dr

        if self.dr < 0:
            self.nr *= -1
            self.dr *= -1

    def appear(self):
        print(f'{self.nr}/{self.dr}')

no1 = Fraction(2, 3)
no1.appear()
no2 = Fraction(2,-3)
no2.appear()
no3 = Fraction(-5,-6)
no3.appear()
