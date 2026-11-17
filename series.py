
# EJERCICIOS DE SERIES

# EJERCICIO 1
def ecuacion1(n):
    return 2 * n**2


def serie1(n):
    acumulador = 0

    for i in range(1, n + 1):
        acumulador += 4 * i - 2

    return acumulador


# EJERCICIO 2
def ecuacion2(n):
    return n * (2 * n - 1)


def serie2(n):
    acumulador = 0

    for i in range(1, n + 1):
        acumulador += 4 * i - 3

    return acumulador


# EJERCICIO 3
def ecuacion3(n):
    return n * (n + 1) * (n + 2) / 6


def serie3(n):
    acumulador = 0

    for i in range(1, n + 1):
        acumulador += i * (i + 1) / 2

    return acumulador


# EJERCICIO 4
def ecuacion4(n):
    return 5 * n * (n + 1) / 2


def serie4(n):
    acumulador = 0

    for i in range(1, n + 1):
        acumulador += 5 * i

    return acumulador


# EJERCICIO 5
def ecuacion5(n):
    return n * (n + 1) * (2 * n + 1) / 6


def serie5(n):
    acumulador = 0

    for i in range(1, n + 1):
        acumulador += i**2

    return acumulador


# EJERCICIO 6
def ecuacion6(n):
    return (n**2 * (n + 1)**2) / 4


def serie6(n):
    acumulador = 0

    for i in range(1, n + 1):
        acumulador += i**3

    return acumulador


# EJERCICIO 7
def ejercicio7(n):
    if n > 2:
        return n**2 > n + 1
    else:
        return False


# PROGRAMA PRINCIPAL
if __name__ == '__main__':

    n = int(input("Dame el valor de n: "))

    if n <= 0:
        print("El valor de n debe ser positivo.")

    else:
        print("\n----- EJERCICIO 1 -----")
        print("Formula:", ecuacion1(n))
        print("Serie:", serie1(n))
        print("Equivalentes:", ecuacion1(n) == serie1(n))

        print("\n----- EJERCICIO 2 -----")
        print("Formula:", ecuacion2(n))
        print("Serie:", serie2(n))
        print("Equivalentes:", ecuacion2(n) == serie2(n))

        print("\n----- EJERCICIO 3 -----")
        print("Formula:", ecuacion3(n))
        print("Serie:", serie3(n))
        print("Equivalentes:", ecuacion3(n) == serie3(n))

        print("\n----- EJERCICIO 4 -----")
        print("Formula:", ecuacion4(n))
        print("Serie:", serie4(n))
        print("Equivalentes:", ecuacion4(n) == serie4(n))

        print("\n----- EJERCICIO 5 -----")
        print("Formula:", ecuacion5(n))
        print("Serie:", serie5(n))
        print("Equivalentes:", ecuacion5(n) == serie5(n))

        print("\n----- EJERCICIO 6 -----")
        print("Formula:", ecuacion6(n))
        print("Serie:", serie6(n))
        print("Equivalentes:", ecuacion6(n) == serie6(n))

        print("\n----- EJERCICIO 7 -----")
        print("n al cuadrado:", n**2)
        print("n + 1:", n + 1)

        if ejercicio7(n):
            print("Se cumple la desigualdad.")
        else:
            print("No se cumple la desigualdad.")
