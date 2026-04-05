# ---- Funciones provistas (NO modificar) ----

def count_vowels(text):
    """Dado un texto, retorna la cantidad de vocales (a, e, i, o, u) que contiene."""
    count = 0
    for char in text.lower():
        if char in "aeiou":
            count += 1
    return count

def count_consonants(text):
    """Dado un texto, retorna la cantidad de consonantes que contiene."""
    count = 0
    for char in text.lower():
        if char.isalpha() and char not in "aeiou":
            count += 1
    return count

# ---- Funciones a implementar ----

def total_letters(text):
    # Calcula la cantidad total de letras sumando vocales y consonantes
    vowels = count_vowels(text)
    consonants = count_consonants(text)
    return vowels + consonants


def vowel_percentage(text):
    # Calcula el porcentaje de vocales sobre el total de letras
    # Si no hay letras, devuelve 0.0
    vowels = count_vowels(text)
    total = total_letters(text)

    if total == 0:
        return 0.0

    porcentaje = (vowels / total) * 100
    return round(porcentaje, 1)


def analyze_text(text):
    # Genera un resumen del texto con cantidad de vocales, consonantes,
    # total de letras y porcentaje de vocales
    vowels = count_vowels(text)
    consonants = count_consonants(text)
    total = total_letters(text)
    percentage = vowel_percentage(text)

    return f"V:{vowels} C:{consonants} T:{total} P:{percentage}%"
