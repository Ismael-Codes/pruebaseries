def ecuacion(nn):
    r=((nn**2)*((nn+1)**2))/4
    print(r)
    return r




#..
def formula(nn):
    ac=0.0
    for i in range(1,int(nn)+1):
        ac+=i**3
        print(f"{i**3} + ",end="")
    print("= ", ac,end="")
    return ac






if __name__ == '__main__':
     k=float(input("Dame n"))
     r=ecuacion(k)
     r2=formula(k)

     if r==r2:
        print(" Si son equivalentes")
     else:
         print(" No son equivalentes")
