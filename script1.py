def ecuacion1(n):
    return 2 * n**2

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

def ecuacion(nn):
    r=nn*(nn+1)*(nn+2)/6
    print(r)
    return r

def formula(nn):
    lim=nn*(nn + 1)/2
    ac=0.0
    for i in range(1,int(lim)):
        ac+=i
        print(f"{i} + ",end="")
    print("= ", ac,end="")
    return ac

if __name__ == '__main__':
     k=float(input("Dame n"))
     r=ecuacion1(k)
     r2=formula1(k)

     if r==r2:
        print("Si son equivalentes")
     else:
        print("No son equivalentes")



