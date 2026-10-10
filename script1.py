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

if __name__ == '__main__':
     k=float(input("Dame n: "))
     print("--------------------------------------------")
     print("Ecuacion: ")
     r=ecuacion1(k)
     print("Formula: ")
     r2=formula1(k)

     if r==r2:
        print("Si son equivalentes")
     else:
        print("No son equivalentes")



