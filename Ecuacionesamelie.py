def ecuacion(n, op):
    if op == 1:
        r = 2 * n**2
    elif op == 2:
        r = n * (2 * n - 1)
    elif op == 3:
        r = n * (n + 1) * (n + 2) // 6
    elif op == 4:
        r = 5 * n * (n + 1) // 2
    elif op == 5:
        r = n * (n + 1) * (2 * n + 1) // 6
    else:
        r = n**2 * (n + 1)**2 // 4

    print("Resultado con formula:", r)
    return r


def formula(n, op):
    ac = 0

    for i in range(1, n + 1):
        if op == 1:
            x = 4 * i - 2
        elif op == 2:
            x = 4 * i - 3
        elif op == 3:
            x = i * (i + 1) // 2
        elif op == 4:
            x = 5 * i
        elif op == 5:
            x = i**2
        else:
            x = i**3

        ac += x
        print(x, end=" + " if i < n else " = ")

    print(ac)
    return ac


def ejercicio7(n):

    for i in range(3, n + 1):
        print(i**2, ">", i + 1, ":", i**2 > i + 1)


if __name__ == "__main__":
    n = int(input("Ingrese numero: "))
    op = int(input("Elige el ejercicio del 1 al 7: "))

    if n <= 0:
        print("Este numero debe ser positivo")

    elif op == 7:
        if n <= 2:
            print("Para el ejercicio 7, el numero debe ser mayor a 2")
        else:
            ejercicio7(n)

    elif 1 <= op <= 6:
        r = ecuacion(n, op)
        r2 = formula(n, op)

        if r == r2:
            print("Si son equivalentes")
        else:
            print("No son equivalentes")

    else:
        print("Opcion no valida")