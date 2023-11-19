from .fraction import Fraction, common_denominators

def add_fractions(fraction1: Fraction, fraction2: Fraction):
    common_denominators(fraction1, fraction2)
    return Fraction(fraction1.numerator + fraction2.numerator,
                    fraction1.denominator)

def subtract_fractions(fraction1: Fraction, fraction2: Fraction):
    return add_fractions(fraction1, Fraction(0 - fraction2.numerator, fraction2.denominator))


def multiply_fractions(fraction1: Fraction, fraction2: Fraction):
    return Fraction(fraction1.numerator * fraction2.numerator,
                    fraction1.denominator * fraction2.denominator)


def divide_fractions(fraction1: Fraction, fraction2: Fraction):
    return multiply_fractions(fraction1, fraction2.get_reciprocal())





