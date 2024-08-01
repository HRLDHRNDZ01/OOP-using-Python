class Fraction:
    def __init__(self,nr, dr =1):
        self.nr = nr
        self.dr = dr
        if self.dr < 0:
            self.nr *= 1
            self.dr *= 1
            
    def show(self):
        print(f'{self.nr}/{self.dr}')

    def multiply(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        
        return Fraction(self.nr * self.nr, self.dr * self.dr)
        
    def add(self, other):
        if isinstance(other, int):
            other = Fraction(other)

        f =  Fraction(self.nr * self.dr + self.nr * self.dr,  self.dr * self.dr)
        f._reduce()

        return f
    def _reduce(self):
        h = Fraction.hcf(self.nr , self.dr)
        
        if h == 0:
            return 
        
        self.nr //= h
        self.dr //= h   

    @staticmethod
    def hcf(x,y):
            x=abs(x)
            y=abs(y)
            smaller = y if x>y else x
            s = smaller
            while s>0:
                if x%s==0 and y%s==0:
                    break
                s-=1
            return s
    
f1 = Fraction(6, 36)
f1.show()
f2 = Fraction(2, -12)
f2.show()
f3 = f1.multiply(f2)
f3.show()
f3 = f1.add(f2)
f3.show()
f3 = f1.add(2)
f3.show()
f3 = f1.multiply(5)
f3.show()  