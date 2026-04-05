# Replace the "ANSWER HERE" for your answer
from encodings.rot_13 import rot13


def roots(a, b, c):
    discriminante = b**2 - 4*a*c

    if discriminante > 0:
        r1 = (-b + discriminante)/(2*a)
        r2 = (-b - discriminante)/(2*a)
        return print(f"({r1}, {r2})")

    elif discriminante == 0:
        r = -b / (2*a)
        return print(f"{r}")

    else:
        return print(f"( )")


def value_y(a, b, c, x):
    y = a*x**2 + b*x + c
    return print(f"{y}")


def to_string(a, b, c):
    return print(f"f(x) = {a} * X^2 + {b} * X + {c}")


def derivation(a, b, c):
    return print(f"f'(x) = {2*a}x + {b}")

roots(1,2,3)
value_y(1,-3,2,0)
to_string(2,-3,1)
derivation(2,-3,1)