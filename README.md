# python-fractions

Simple Python library to work with fractions.

## How to install?

    git clone https://github.com/KrzysMur/python-fractions.git
    pip install --upgrade build
    python -m build
    python -m pip install .


## Requirements
- git
- Python
- pip

## How to use?
    Fraction(numerator, denominator)

Module pyfractions.operations contains following functions:
    add_fraction(Fraction, Fraction)
    subtract_fraction(Fraction, Fraction)
    multiply_fraction(Fraction, Fraction)
    divide_fraction(Fraction, Fraction)

To display Fraction object in readable format use
    fraction.display()
This function returns for instance "3/4" instead of Fraction object.
It does not mutate the object.
