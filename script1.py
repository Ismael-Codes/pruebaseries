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
     k=float(input("Dame n"))
     r=ecuacion3(k)
     r2=formula3(k)

     if r==r2:
        print("Si son equivalentes")
     else:


        print("No son equivalentes")



