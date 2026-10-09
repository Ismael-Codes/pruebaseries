def formula(nn, equ):
    ac=0.0
    for i in range(1,int(nn)+1):
        match equ:
            case "1":
                paso = 4*i-2
            case "2":
                paso = 4*i-3
            case "3":
                paso = i*(i + 1)/2
            case "4":
                paso = 5*i
            case "5":
                paso = pow(i,2)
            case "6":
                paso = pow(i,3)
        ac+=paso
        print(f"{paso} + ",end="")
    print("= ", ac,end="")
    return ac

def formula7(nn):
    if nn>2:
        todos = True
        for k in range(3, nn + 1):
            cumple = k ** 2 > k + 1
            todos = todos and cumple
            print(f"   n={k}: {k}^2 = {k ** 2} > {k}+1 = {k + 1}  ->  {cumple}")
        if todos:
            print("   Sí se cumple la desigualdad")
        else:
            print("   No se cumple la desigualdad")
    else:
        print("   n debe ser mayor que 2") 

if __name__ == '__main__':
    k=float(input("Dame n: "))
    sw=input("Ingresa que ecuacion quieres evaluar (1 - 7): ")

    match sw:
        case "1":
            lim=(4*k-2)
            print(lim)
            r=2*pow(k, 2)
            print(r)
            r2=formula(k, sw)
            print(r)
        case "2":
            lim=(4*k-3)
            r=k*(2*k-1)
            r2=formula(k, sw)
            print(r)
        case "3":
            lim=k*(k + 1)/2
            r=k*(k+1)*(k+2)/6
            r2=formula(k, sw)
            print(r)
        case "4":
            lim=5*k
            r=(5*k*(k+1))/2
            r2=formula(k, sw)
            print(r)
        case "5":
            lim=pow(k,2)
            r=k*(k+1)*(2*k+1)/6
            r2=formula(k, sw)
            print(r)
        case "6":
            lim=pow(k,3)
            r=pow(k,2)*pow((k+1),2)/4
            r2=formula(k, sw)
            print(r)
        case "7":
            formula7(int(k))
            raise SystemExit
        case _:
            print("Opcion no valida")
            exit()

    if r==r2:
        print("Si son equivalentes")
    else:
        print("No son equivalentes")

##Leonardo

