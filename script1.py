def ecuacion3(n):
    print("Resultado ecuación: ")
    r=n*(n+1)*(n+2)/6
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

#def ecuacion4





if __name__ == '__main__':
     k=int(input("Dame n: "))
     r=ecuacion3(k)
     r2=formula3(k)

     if r==r2:
        print("Si son equivalentes")
     else:


        print("No son equivalentes")



