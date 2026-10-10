def ecuacion(nn):
    r=nn*(2*nn-1)
    print(r)
    return r




#..
def formula(nn):
    lim=(4*nn)-3
    ac=0.0
    for i in range(1,int(lim)+1,4):
        ac+=i
        print(f"{i} + ",end="")
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
