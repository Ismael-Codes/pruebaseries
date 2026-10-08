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





if __name__ == '__main__':
     k=int(input("Dame n: "))
     r=ecuacion2(k)
     r2=formula2(k)

     if r==r2:
        print("Si son equivalentes")
     else:


        print("No son equivalentes")



