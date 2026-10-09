def verificar_series(n):
    print(f"--- Verificando expresiones para n = {n} ---")
    
    
    suma_1 = sum(4 * i - 2 for i in range(1, n + 1))
    formula_1 = 2 * n**2
    print(f"Ejercicio 1: Suma = {suma_1}, Fórmula = {formula_1} -> {'Correcto' if suma_1 == formula_1 else 'Incorrecto'}")

    
    suma_2 = sum(4 * i - 3 for i in range(1, n + 1))
    formula_2 = n * (2 * n - 1)
    print(f"Ejercicio 2: Suma = {suma_2}, Fórmula = {formula_2} -> {'Correcto' if suma_2 == formula_2 else 'Incorrecto'}")

   
    suma_3 = sum((i * (i + 1)) // 2 for i in range(1, n + 1))
    formula_3 = (n * (n + 1) * (n + 2)) // 6
    print(f"Ejercicio 3: Suma = {suma_3}, Fórmula = {formula_3} -> {'Correcto' if suma_3 == formula_3 else 'Incorrecto'}")

  
    suma_4 = sum(5 * i for i in range(1, n + 1))
    formula_4 = (5 * n * (n + 1)) // 2
    print(f"Ejercicio 4: Suma = {suma_4}, Fórmula = {formula_4} -> {'Correcto' if suma_4 == formula_4 else 'Incorrecto'}")

    
    suma_5 = sum(i**2 for i in range(1, n + 1))
    formula_5 = (n * (n + 1) * (2 * n + 1)) // 6
    print(f"Ejercicio 5: Suma = {suma_5}, Fórmula = {formula_5} -> {'Correcto' if suma_5 == formula_5 else 'Incorrecto'}")

    
    suma_6 = sum(i**3 for i in range(1, n + 1))
    formula_6 = (n**2 * (n + 1)**2) // 4
    print(f"Ejercicio 6: Suma = {suma_6}, Fórmula = {formula_6} -> {'Correcto' if suma_6 == formula_6 else 'Incorrecto'}")

    
    if n > 2:
        izq_7 = n**2
        der_7 = n + 1
        print(f"Ejercicio 7: {izq_7} > {der_7} -> {'Correcto' if izq_7 > der_7 else 'Incorrecto'}")
    else:
        print("Ejercicio 7: n debe ser mayor a 2 para evaluar esta condición.")


verificar_series(10)