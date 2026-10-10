def ejercicio_1(n: int):
    lado_izq = sum(4 * i - 2 for i in range(1, n + 1))
    lado_der = 2 * (n ** 2)
    return lado_izq, lado_der, lado_izq == lado_der


def ejercicio_2(n: int):
    lado_izq = sum(4 * i - 3 for i in range(1, n + 1))
    lado_der = n * (2 * n - 1)
    return lado_izq, lado_der, lado_izq == lado_der


def ejercicio_3(n: int):
    lado_izq = sum(i * (i + 1) // 2 for i in range(1, n + 1))
    lado_der = n * (n + 1) * (n + 2) // 6
    return lado_izq, lado_der, lado_izq == lado_der


def ejercicio_4(n: int):
    lado_izq = sum(5 * i for i in range(1, n + 1))
    lado_der = 5 * n * (n + 1) // 2
    return lado_izq, lado_der, lado_izq == lado_der


def ejercicio_5(n: int):
    lado_izq = sum(i ** 2 for i in range(1, n + 1))
    lado_der = n * (n + 1) * (2 * n + 1) // 6
    return lado_izq, lado_der, lado_izq == lado_der


def ejercicio_6(n: int):
    lado_izq = sum(i ** 3 for i in range(1, n + 1))
    lado_der = (n ** 2) * ((n + 1) ** 2) // 4
    return lado_izq, lado_der, lado_izq == lado_der


def ejercicio_7(n: int):
    lado_izq = n ** 2
    lado_der = n + 1
    # Se evalúa si se cumple la desigualdad estricta
    cumple = (lado_izq > lado_der) if n > 2 else False
    return lado_izq, lado_der, cumple


if __name__ == "__main__":
    n = int(input("Ingresa el valor de n (entero positivo): "))

    ejercicios = [
        ("Ejercicio 1", ejercicio_1),
        ("Ejercicio 2", ejercicio_2),
        ("Ejercicio 3", ejercicio_3),
        ("Ejercicio 4", ejercicio_4),
        ("Ejercicio 5", ejercicio_5),
        ("Ejercicio 6", ejercicio_6),
        ("Ejercicio 7 (Desigualdad n > 2)", ejercicio_7),
    ]

    print("\n Validación")
    for nombre, func in ejercicios:
        izq, der, valido = func(n)
        relacion = ">" if "7" in nombre else "=="
        estado = "Cumple" if valido else "No cumple"
        print(f"{nombre}: Lado Izq = {izq} | Lado Der = {der} -> ({izq} {relacion} {der}) : {estado}")