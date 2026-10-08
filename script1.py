def ecuacion1(n):
    print("Resultado ecuación: ")
    r=2*(n**2)
    print(r)
    return r


def formula1(n):
    print("Resultado formula: ")
    ac = 0
    for i in range(1, n + 1):
        k = (4*i)-2
        ac += k
        if i < n:
            print(f"{k} + ", end="")
        else:
            print(f"{k} = ", end="")
    print(ac)
    return ac

def ecuacion2(n):
    print("Resultado ecuación: ")
    r=n*(2*n-1)
    print(r)
    return r


def formula2(n):
    print("Resultado formula: ")
    ac = 0
    for i in range(1, n + 1):
        k = (4*i)-3
        ac += k
        if i < n:
            print(f"{k} + ", end="")
        else:
            print(f"{k} = ", end="")
    print(ac)
    return ac

def ecuacion3(n):
    print("Resultado ecuación: ")
    r=n*(n+1)*(n+2)//6
    print(r)
    return r


def formula3(n):
    print("Resultado formula: ")
    ac = 0
    for i in range(1, n + 1):
        k = i * (i + 1) // 2
        ac += k
        if i < n:
            print(f"{k} + ", end="")
        else:
            print(f"{k} = ", end="")
    print(ac)
    return ac
#Git branch from Deivid

def ecuacion4(n):
    print("Resultado ecuación: ")
    r=5*n*(n+1)//2
    print(r)
    return r


def formula4(n):
    print("Resultado formula: ")
    ac = 0
    for i in range(1, n + 1):
        k = 5*i
        ac += k
        if i < n:
            print(f"{k} + ", end="")
        else:
            print(f"{k} = ", end="")
    print(ac)
    return ac

def ecuacion5(n):
    print("Resultado ecuación: ")
    r=n*(n+1)*(2*n+1)//6
    print(r)
    return r


def formula5(n):
    print("Resultado formula: ")
    ac = 0
    for i in range(1, n + 1):
        k = i**2
        ac += k
        if i < n:
            print(f"{k} + ", end="")
        else:
            print(f"{k} = ", end="")
    print(ac)
    return ac

def ecuacion6(n):
    print("Resultado ecuación: ")
    r=(n**2)*((n+1)**2)//4
    print(r)
    return r


def formula6(n):
    print("Resultado formula: ")
    ac = 0
    for i in range(1, n + 1):
        k = i**3
        ac += k
        if i < n:
            print(f"{k} + ", end="")
        else:
            print(f"{k} = ", end="")
    print(ac)
    return ac

def ecuacion7(n):
    r=(n**2)>(n+1)
    print(f"{n**2} > {n+1}")
    return r

if __name__ == '__main__':

    while True:
        print("EVALUACIÓN DE ECUACIONES Y FÓRMULAS")
        print("1. Expresión 1: 2 + 6 + 10 + ... + (4n - 2) = 2n²")
        print("2. Expresión 2: 1 + 5 + 9 + ... + (4n - 3) = n(2n - 1)")
        print("3. Expresión 3: 1 + 3 + 6 + ... = n(n+1)(n+2)/6")
        print("4. Expresión 4: 5 + 10 + 15 + ... + 5n = 5n(n+1)/2")
        print("5. Expresión 5: 1² + 2² + ... + n² = n(n+1)(2n+1)/6")
        print("6. Expresión 6: 1³ + 2³ + ... + n³ = n²(n+1)²/4")
        print("7. Expresión 7: Desigualdad (n² > n + 1 para n > 2)")
        print("0. Salir")

        opcion = int(input("Selecciona una opción (0-7): "))

        if opcion in range(1, 8):
            n = int(input("Ingresa el valor de n (entero positivo): "))


        if opcion == 1:
            r = formula1(n)
            r1 = ecuacion1(n)
            print("Si son equivalentes" if r == r1 else "No son equivalentes")

        elif opcion == 2:
            r = formula2(n)
            r1 = ecuacion2(n)
            print("Si son equivalentes" if r == r1 else "No son equivalentes")

        elif opcion == 3:
            r = formula3(n)
            r1 = ecuacion3(n)
            print("Si son equivalentes" if r == r1 else "No son equivalentes")

        elif opcion == 4:
            r = formula4(n)
            r1 = ecuacion4(n)
            print("Si son equivalentes" if r == r1 else "No son equivalentes")

        elif opcion == 5:
            r = formula5(n)
            r1 = ecuacion5(n)
            print("Si son equivalentes" if r == r1 else "No son equivalentes")

        elif opcion == 6:
            r = formula6(n)
            r1 = ecuacion6(n)
            print("Si son equivalentes" if r == r1 else "No son equivalentes")

        elif opcion == 7:
            print("Resultado:")
            c = ecuacion7(n)
            print("Si cumple la condicion" if c else "No cumple ya que n < 2")

        elif opcion == 0:
            print("¡Hasta luego!")
            break

        elif opcion not in range(1, 8):
            print("Opción no válida. Intenta de nuevo.")
            continue


