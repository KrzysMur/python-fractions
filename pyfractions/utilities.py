def largest_common_factor(a: int, b: int):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a
