"""Luhn checksum. Standard library only."""


def is_valid(number):
    digits = [int(c) for c in str(number) if c.isdigit()]
    total, alt = 0, False
    for d in reversed(digits):
        if alt:
            d *= 2
            if d > 9:
                d -= 9
        total += d
        alt = not alt
    return total % 10 == 0


def check_digit(partial):
    for d in range(10):
        if is_valid(str(partial) + str(d)):
            return d
    raise AssertionError("unreachable")
