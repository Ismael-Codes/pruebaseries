def ecuacion1(n):
    r = 2 * n**2
    print(r)
    return r
def formula1(n):
    ac = 0
    for i in range(1, int(n) + 1):
        termino = 4*i - 2
        ac += termino
        if i < n:
            print(f"{termino} + ", end="")
        else:
            print(f"{termino}", end="")
    print(f" = {ac}")
    return ac


def ecuacion2(n):
    r = n * (2*n - 1)
    print(r)
    return r

def formula2(n):
    ac = 0
    for i in range(1, int(n) + 1):
        termino = 4*i - 3
        ac += termino
        if i < n:
            print(f"{termino} + ", end="")
        else:
            print(f"{termino}", end="")
    print(f" = {ac}")
    return ac


def ecuacion3(nn):
    r=nn*(nn+1)*(nn+2)/6
    print(r)
    return r

def formula3(nn):
    lim=nn*(nn + 1)/2
    ac=0.0
    for i in range(1,int(lim)):
        ac+=i
        print(f"{i} + ",end="")
    print("= ", ac,end="")
    return ac


def ecuacion4(n):
    r = 5 * n * (n + 1) / 2
    print(r)
    return r
def formula4(n):
    ac = 0
    for i in range(1, int(n) + 1):
        termino = 5 * i
        ac += termino
        if i < n:
            print(f"{termino} + ", end="")
        else:
            print(f"{termino}", end="")
    print(f" = {ac}")
    return ac

def ecuacion5(n):
    r = n * (n + 1) * (2*n + 1) / 6
    print(r)
    return r

def formula5(n):
    ac = 0
    for i in range(1, int(n) + 1):
        ac += i**2
        if i < n:
            print(f"{i}² + ", end="")
        else:
            print(f"{i}²", end="")
    print(f" = {ac}")
    return ac

def ecuacion6(n):
    r = (n**2 * (n + 1)**2) / 4
    print(r)
    return r

def formula6(n):
    ac = 0
    for i in range(1, int(n) + 1):
        ac += i**3
        if i < n:
            print(f"{i}³ + ", end="")
        else:
            print(f"{i}³", end="")
    print(f" = {ac}")
    return ac

def ecuacion7(n):
    r=(n**2)>(n+1)
    print(f"{n**2} > {n+1}")
    return r

if __name__ == '__main__':
     print("elije una comparacion:")
     print("[1] 2 + 6 + 10 + ... + (4n-2) = 2n²")
     print("[2] 1 + 5 + 9 + ... + (4n-3) = n(2n-1)")
     print("[3] 1 + 3 + 6 + ... + n(n+1)/2 = n(n+1)(n+2)/6")
     print("[4] 5 + 10 + 15 + ... + 5n = 5n(n+1)/2")
     print("[5] 1² + 2² + ... + n² = n(n+1)(2n+1)/6")
     print("[6] 1³ + 2³ + ... + n³ = n²(n+1)²/4")
     print("[7] n² > n + 1 para n > 2")

     op = input("Opcion: ")

     k = float(input("Dame n: "))
     print("--------------------------------------------")

     if op == "7":
         print("Desigualdad: ")
         if ecuacion7(k):
             print("Si se cumple")
         else:
             print("No se cumple")
     elif op in ("1", "2", "3", "4", "5", "6"):
         if op == "1":
             ecuacion, formula = ecuacion1, formula1
         elif op == "2":
             ecuacion, formula = ecuacion2, formula2
         elif op == "3":
             ecuacion, formula = ecuacion3, formula3
         elif op == "4":
             ecuacion, formula = ecuacion4, formula4
         elif op == "5":
             ecuacion, formula = ecuacion5, formula5
         else:
             ecuacion, formula = ecuacion6, formula6

         print("Ecuacion: ")
         r = ecuacion(k)
         print("Formula: ")
         r2 = formula(k)

         if r == r2:
             print("Si son equivalentes")
         else:
             print("No son equivalentes")
     else:
         print("Opcion no valida")



