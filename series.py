def resolver_series(n):
    print(f"resultados de n = {n}\n")

    suma_1 = sum(4 * i - 2 for i in range(1, n + 1))
    formula_1 = 2 * (n**2)
    print(
        f"1) Serie 1: Suma = {suma_1} | Formula (2*n^2) = {formula_1} | coincide?: {suma_1 == formula_1}"
    )

    suma_2 = sum(4 * i - 3 for i in range(1, n + 1))
    formula_2 = n * (2 * n - 1)
    print(
        f"2) Serie 2: Suma = {suma_2} | Formula (n*(2n-1)) = {formula_2} | coincide?: {suma_2 == formula_2}"
    )

    suma_3 = sum(i * (i + 1) // 2 for i in range(1, n + 1))
    formula_3 = (n * (n + 1) * (n + 2)) // 6
    print(
        f"3) Serie 3: Suma = {suma_3} | Formula (n(n+1)(n+2)/6) = {formula_3} | coincide?: {suma_3 == formula_3}"
    )

    suma_4 = sum(5 * i for i in range(1, n + 1))
    formula_4 = (5 * n * (n + 1)) // 2
    print(
        f"4) Serie 4: Suma = {suma_4} | Formula (5n(n+1)/2) = {formula_4} | coincide?: {suma_4 == formula_4}"
    )

    suma_5 = sum(i**2 for i in range(1, n + 1))
    formula_5 = (n * (n + 1) * (2 * n + 1)) // 6
    print(
        f"5) Serie 5: Suma = {suma_5} | Formula (n(n+1)(2n+1)/6) = {formula_5} | coincide?: {suma_5 == formula_5}"
    )

    suma_6 = sum(i**3 for i in range(1, n + 1))
    formula_6 = (n**2 * (n + 1) ** 2) // 4
    print(
        f"6) Serie 6: Suma = {suma_6} | Formula (n^2*(n+1)^2/4) = {formula_6} | coincide?: {suma_6 == formula_6}"
    )

    cumple_7 = (n**2) > (n + 1) if n > 2 else "No aplica (n debe ser > 2)"
    print(
        f"7) Desigualdad (n^2 > n + 1): {n}^2 > {n}+1 => {n**2} > {n+1} | se cumple?: {cumple_7}"
    )


if __name__ == "__main__":
    n_test = 5
    resolver_series(n_test)