
def ecuacion(nn, op):
    if op == 1:
        r = 2*nn**2
    elif op == 2:
        r = nn*(2*nn-1)
    elif op == 3:
        r = nn*(nn+1)*(nn+2)/6
    elif op == 4:
        r = 5*nn*(nn+1)/2
    elif op == 5:
        r = nn*(nn+1)*(2*nn+1)/6
    elif op == 6:
        r = nn**2*(nn+1)**2/4
    elif op == 7:
        r = nn**2 > nn+1

    print("Resultado de ecuacion:", r)
    return r


def formula(nn, op):
    ac = 0

    if op == 7:
        ac = nn**2 > nn+1
        print(nn**2, ">", nn+1, "=", ac)
        return ac

    for i in range(1, nn+1):
        if op == 1:
            termino = 4*i-2
        elif op == 2:
            termino = 4*i-3
        elif op == 3:
            termino = i*(i+1)/2
        elif op == 4:
            termino = 5*i
        elif op == 5:
            termino = i**2
        elif op == 6:
            termino = i**3

        ac += termino
        print(f"{termino:g}", end="")
        if i < nn:
            print(" + ", end="")

    print(" =", ac)
    return ac


if __name__ == '__main__':
    print("Ejercicios de series")
    print("1. Serie 2 + 6 + 10 ...")
    print("2. Serie 1 + 5 + 9 ...")
    print("3. Serie 1 + 3 + 6 ...")
    print("4. Serie 5 + 10 + 15 ...")
    print("5. Serie 1² + 2² + 3² ...")
    print("6. Serie 1³ + 2³ + 3³ ...")
    print("7. Desigualdad n² > n + 1")

    op = int(input("Selecciona un ejercicio: "))
    
    if op >= 1 and op <= 7:
        n = int(input("Dame n: "))

        if n >= 1 and (op != 7 or n > 2):
            r = ecuacion(n, op)
            r2 = formula(n, op)

            if r == r2:
                print("Los resultados son iguales")
            else:
                print("Los resultados son diferentes")
        else:
            print("Valor de n no valido")
    else:
        print("Opcion no valida")
