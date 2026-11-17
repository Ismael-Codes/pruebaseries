
def ecuacion(n):
    resultado = 2 * n**2
    return resultado


def serie(n):
    acumulador = 0

    for i in range(1, n + 1):
        termino = 4 * i - 2
        acumulador += termino
        print(termino, end=" + ")

    print("=", acumulador)
    return acumulador


if __name__ == '__main__':
    n = int(input("Dame el valor de n: "))

    r1 = ecuacion(n)
    r2 = serie(n)

    print("Resultado de la ecuacion:", r1)

    if r1 == r2:
        print("Si son equivalentes")
    else:
        print("No son equivalentes")
