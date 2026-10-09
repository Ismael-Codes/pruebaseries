# Yurem Jesús Aco Luna

def formula(nn, equ):
    ac = 0
    terminos = []

    for i in range(1, nn + 1):
        match equ:
            case "1":
                paso = 4 * i - 2
            case "2":
                paso = 4 * i - 3
            case "3":
                paso = i * (i + 1) // 2
            case "4":
                paso = 5 * i
            case "5":
                paso = i ** 2
            case "6":
                paso = i ** 3
            case _:
                raise ValueError("Opción no válida")

        ac += paso
        terminos.append(str(paso))

    print(" + ".join(terminos), "=", ac)
    return ac


def formula7(nn):
    if nn <= 2:
        print("n debe ser mayor que 2")
        return

    todos = True

    for k in range(3, nn + 1):
        cumple = k ** 2 > k + 1
        todos = todos and cumple
        print(f"n={k}: {k ** 2} > {k + 1} -> {cumple}")

    if todos:
        print("Sí se cumple la desigualdad para los valores evaluados")
    else:
        print("No se cumple la desigualdad")


if __name__ == "__main__":
    try:
        k = int(input("Dame n: "))

        if k < 1:
            print("n debe ser un entero positivo")
            raise SystemExit

        sw = input("Elige la ecuación (1 - 7): ").strip()

        match sw:
            case "1":
                r = 2 * k ** 2
            case "2":
                r = k * (2 * k - 1)
            case "3":
                r = k * (k + 1) * (k + 2) // 6
            case "4":
                r = 5 * k * (k + 1) // 2
            case "5":
                r = k * (k + 1) * (2 * k + 1) // 6
            case "6":
                r = k ** 2 * (k + 1) ** 2 // 4
            case "7":
                formula7(k)
                raise SystemExit
            case _:
                print("Opción no válida")
                raise SystemExit

        r2 = formula(k, sw)
        print("Resultado de la fórmula:", r)

        if r == r2:
            print("Sí son equivalentes para este valor de n")
        else:
            print("No son equivalentes para este valor de n")

    except ValueError:
        print("Debes ingresar un número entero")