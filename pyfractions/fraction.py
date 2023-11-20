
from .utilities import largest_common_factor


class Fraction:
    def __init__(self, numerator: int, denominator: int = 1):
        self.numerator = numerator
        if denominator == 0:
            raise ZeroDivisionError
        self.denominator = denominator

    def reduce(self):
        lcf = largest_common_factor(self.numerator, self.denominator)
        self.numerator //= lcf
        self.denominator //= lcf

    def get_reciprocal(self):
        return Fraction(self.denominator, self.numerator)

    def multiply_numerator_and_denominator(self, x: int):
        self.numerator *= x
        self.denominator *= x

    def display(self):
        return f"{self.numerator}/{self.denominator}"

    def get_float(self):
        return self.numerator / self.denominator


def common_denominators(fraction1: Fraction, fraction2: Fraction):
    x = fraction1.denominator
    fraction1.multiply_numerator_and_denominator(fraction2.denominator)
    fraction2.multiply_numerator_and_denominator(x)
