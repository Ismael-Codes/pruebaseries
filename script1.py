##Codigo Ian Hernandez Ibarra

n = int(input("Dame n: "))


def probar(numero, ecuacion, terminos, texto_formula, valor_formula):
    suma = sum(terminos)
    proceso = " + ".join(str(t) for t in terminos)
    print(numero, ecuacion)
    print("   Sucesión: ", proceso, "=", suma)
    print("   Fórmula:  ", texto_formula, "=", valor_formula)
    if suma == valor_formula:
        print("   Sí son equivalentes\n")
    else:
        print("   No son equivalentes\n")


# 1) 2 + 6 + 10 + ... + (4n-2) = 2n^2
terminos = [4 * k - 2 for k in range(1, n + 1)]
probar("1)", "2 + 6 + 10 + ... + (4n-2) = 2n^2",
       terminos, f"2({n})^2", 2 * n ** 2)

# 2) 1 + 5 + 9 + ... + (4n-3) = n(2n-1)
terminos = [4 * k - 3 for k in range(1, n + 1)]
probar("2)", "1 + 5 + 9 + ... + (4n-3) = n(2n-1)",
       terminos, f"{n}(2({n})-1)", n * (2 * n - 1))

# 3) 1 + 3 + 6 + ... + n(n+1)/2 = n(n+1)(n+2)/6
terminos = [k * (k + 1) // 2 for k in range(1, n + 1)]
probar("3)", "1 + 3 + 6 + ... + n(n+1)/2 = n(n+1)(n+2)/6",
       terminos, f"{n}({n}+1)({n}+2)/6", n * (n + 1) * (n + 2) // 6)

# 4) 5 + 10 + 15 + ... + 5n = 5n(n+1)/2
terminos = [5 * k for k in range(1, n + 1)]
probar("4)", "5 + 10 + 15 + ... + 5n = 5n(n+1)/2",
       terminos, f"5({n})({n}+1)/2", 5 * n * (n + 1) // 2)

# 5) 1^2 + 2^2 + ... + n^2 = n(n+1)(2n+1)/6
terminos = [k ** 2 for k in range(1, n + 1)]
probar("5)", "1^2 + 2^2 + ... + n^2 = n(n+1)(2n+1)/6",
       terminos, f"{n}({n}+1)(2({n})+1)/6", n * (n + 1) * (2 * n + 1) // 6)

# 6) 1^3 + 2^3 + ... + n^3 = n^2(n+1)^2/4
terminos = [k ** 3 for k in range(1, n + 1)]
probar("6)", "1^3 + 2^3 + ... + n^3 = n^2(n+1)^2/4",
       terminos, f"({n})^2({n}+1)^2/4", n ** 2 * (n + 1) ** 2 // 4)

# 7) n^2 > n + 1 para n > 2
print("7) n^2 > n + 1 para n > 2")
if n > 2:
    todos = True
    for k in range(3, n + 1):
        cumple = k ** 2 > k + 1
        todos = todos and cumple
        print(f"   n={k}: {k}^2 = {k ** 2} > {k}+1 = {k + 1}  ->  {cumple}")
    if todos:
        print("   Sí se cumple la desigualdad")
    else:
        print("   No se cumple la desigualdad")
else:
    print("   n debe ser mayor que 2")


