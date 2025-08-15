def count_char(cadena, caracter):
    """Cuenta las veces que un carácter aparece en una cadena."""
    
    if not isinstance(cadena, str):
        return (-100, None)
    
    for char in cadena:
        if not (char.isalpha() or char.isdigit()):
            return (-200, None)
    
    if not isinstance(caracter, str) or len(caracter) != 1:
        return (-300, None)
    
    if not (caracter.isalpha() or caracter.isdigit()):
        return (-300, None)
    
    count = cadena.count(caracter)
    return (0, count)


def multiplo_2(base, multiplo):
    """Calcula múltiplo * base usando bit-shifting."""
    
    if (isinstance(base, str) or isinstance(multiplo, str) or 
        not isinstance(base, int) or not isinstance(multiplo, int) or
        base <= 0 or multiplo <= 0):
        return (-400, None)
    
    valid_multiplos = [1, 2, 4, 8, 16]
    if multiplo not in valid_multiplos:
        return (-500, None)
    
    if multiplo == 1:
        resultado = base
    elif multiplo == 2:
        resultado = base << 1
    elif multiplo == 4:
        resultado = base << 2
    elif multiplo == 8:
        resultado = base << 3
    elif multiplo == 16:
        resultado = base << 4
    
    return (0, resultado)


# Error codes:
# Success: 0
# count_char errors: -100 (not string), -200 (invalid chars), -300 (invalid character)
# multiplo_2 errors: -400 (not positive integers), -500 (invalid multiplier)
