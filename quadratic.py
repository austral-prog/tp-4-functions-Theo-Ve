def roots(a, b, c):
    discriminante = b**2 - 4*a*c

    if discriminante > 0:
        r1 = (-b + discriminante**0.5)/(2*a)
        r2 = (-b - discriminante**0.5)/(2*a)
        return f"({r1}, {r2})"

    elif discriminante == 0:
        r = -b / (2*a)
        return f"({r})"

    else:
        return f"( )"


def value_y(a, b, c, x):
    y = a*x**2 + b*x + c
    return y


def to_string(a, b, c):
    if a == 0 and b == 0:
        return f"f(x) = {c}"

    if a == 0:
        return f"f(x) = {b} * X + {c}"

    if b == 0:
        return f"f(x) = {a} * X^2 + {c}"

    return f"f(x) = {a} * X^2 + {b} * X + {c}"


def derivation(a, b, c):
    if a == 0 and b == 0:
        return "f'(x) = 0"

    if a == 0:
        return f"f'(x) = {b}"

    if b == 0:
        return f"f'(x) = {2 * a} * X"

    return f"f'(x) = {2 * a} * X + {b}"