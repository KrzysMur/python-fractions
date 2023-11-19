
class Fraction:
    def __init__(self, numerator: int, denominator: int):
        self.numerator = numerator
        self.denominator = denominator

    def reduce(self):
        lcf = largest_common_factor(self.numerator, self.denominator)
        self.numerator //= lcf
        self.denominator //= lcf

    def multiply_numerator_and_denominator(self, x: int):
        self.numerator *= x
        self.denominator *= x



def largest_common_factor(a: int, b: int):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a



