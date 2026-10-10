def ecuacion3(nn):
    r=nn*(nn+1)*(nn+2)/6
    print(r)
    return r




#..
def formula3(nn):
    lim=nn*(nn + 1)/2
    ac=0.0
    for i in range(1,int(lim)):
        ac+=i
        print(f"{i} + ",end="")
    print("= ", ac,end="")
    return ac

def ecuacion1(nn):
    print("Resultado de la ecuacion: ")
    r = 2 * (nn** 2)
    print(r)
    return r

def formula1(nn):
    print("Resultado de la formula: ")
    ac = 0
    for i in range(1, nn + 1):
        k = (4 * i) - 2
        ac += k
        if i <= nn:
            print(f"{k} + ",end="")
        else:
            print(f"{k} = ",end="")
    print(ac)
    return ac


def ecuacion2(nn):
    print("Resultado de la ecuacion: ")
    r = nn * (2 * nn - 1)
    print(r)
    return r

def formula2(nn):
    print("Resultado de la formula: ")
    ac = 0
    for i in range(1, nn + 1):
        k = (4 * i) - 3
        ac += k
        if i <= nn:
            print(f"{k} + ",end="")
        else:
            print(f"{k} = ",end="")
    print(ac)
    return ac


def ecuacion4(nn):
    print("Resultado de la ecuacion: ")
    r = 5 * nn * (nn + 1)/2
    print(r)
    return r

def formula4(nn):
    print("Resultado de la formula: ")
    ac = 0
    for i in range(1, nn + 1):
        k = 5 * i
        ac += k
        if i <= nn:
            print(f"{k} + ",end="")
        else:
            print(f"{k} = ",end="")
    print(ac)
    return ac






if __name__ == '__main__':
    while True:
        print("Menu")
        print("Ejercicio 1: 2 + 6 + 10 + ... + (4n - 2) = 2n²")
        print("Ejercicio 2: 1 + 5 + 9 + ... + (4n - 3) = n(2n - 1)")
        print("Ejercicio 3: 1 + 3 + 6 + ... + n(n+1)/2 = n(n+1)(n+2)/6")
        print("Ejercicio 4: 5 + 10 + 15 + ... + 5n = 5n(n+1)/2")
        print("Ejercicio 5: 1^2 + 2^2 + ... + n^2 = n(n+1)(2n+1)/6")
        print("Ejercicio 6: 1^3 + 2^3 + ... + n^3 = n^2(n+1)^2/4")
        print("Ejercicio 7: Desigualdad -> n^2 > n + 1 para n > 2")
        print("8. Salir")

        opcion = int(input(" elige una opcion: "))

        if opcion in range(1,8):
            k=int(input("Dame n"))

        if opcion == 1:
            r = ecuacion1(k)
            r2 = formula1(k)
            if r == r2:
                print("Si son equivalentes")
            else:
                print("No son equivalentes")

        elif opcion == 2:
            r = ecuacion2(k)
            r2 = formula2(k)
            if r == r2:
                print("Si son equivalentes")
            else:
                print("No son equivalentes")

        elif opcion == 3:
            r = ecuacion3(k)
            r2 = formula3(k)
            if r == r2:
                print("Si son equivalentes")
            else:
                print("No son equivalentes")

        elif opcion == 4:
            r = ecuacion4(k)
            r2 = formula4(k)
            if r == r2:
                print("Si son equivalentes")
            else:
                print("No son equivalentes")

        elif opcion == 5:
            r = ecuacion5(k)
            r2 = formula5(k)
            if r == r2:
                print("Si son equivalentes")
            else:
                print("No son equivalentes")

        elif opcion == 6:
            r = ecuacion6(k)
            r2 = formula6(k)
            if r == r2:
                print("Si son equivalentes")
            else:
                print("No son equivalentes")

        elif opcion == 7:
            r = ecuacion7(k)
            if r:
                print("Si cumple la condicion")
            else:
                print("No cumple porque n<2")

        elif opcion == 8:
            print("adioss!")






