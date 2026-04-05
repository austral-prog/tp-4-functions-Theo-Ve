# ---- Funciones provistas (NO modificar) ----

def is_even(n):
    """Dado un número entero n, retorna True si es par, False si es impar."""
    return n % 2 == 0

def is_positive(n):
    """Dado un número entero n, retorna True si es mayor a 0, False en caso contrario."""
    return n > 0

# ---- Función a implementar ----

def classify_number(n):
    if n == 0:
        return print("zero")
    elif is_even(n) and is_positive(n):
        return print("positive even")
    elif is_even(n) and not is_positive(n):
        return print("negative even")
    elif is_positive(n) and not is_even(n):
        return print("positive odd")
    elif not is_even(n) and not is_positive(n):
        return print("negative odd")


classify_number(0)