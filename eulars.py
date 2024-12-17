import sys

sys.setrecursionlimit(15000)
class Euler:
    def __init__(self, h, formula, baseLevel, baseValue):
        self.h = h
        self.formula = formula
        self.baseLevel = baseLevel
        self.baseValue = baseValue

    def numericalMethod(self, n):
        if(n == self.baseLevel):
            return self.baseValue
               
        return self.numericalMethod(n-1) + self.h * self.formula(n-1)
    

# This is the differential function
def fn(x):
    return x*x

if(__name__ == '__main__'):
    euler = Euler(2, fn, 0, 1)
    print(euler.numericalMethod(10000))
