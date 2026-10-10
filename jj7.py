def lado_izquierdo(nn):
    r=nn**2
    print(r)
    return r

#..
def lado_derecho(nn):
    ac=nn+1
    return ac



if __name__ == '__main__':
     k=float(input("Dame n"))

     r=lado_izquierdo(k)
     ac=lado_derecho(k)

     if r>ac:
        print(" Si se cumple la desigualdad")
     else:
         print(" No se cumple la desigualdad")
