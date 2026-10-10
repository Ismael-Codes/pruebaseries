def ecuacion(nn):
    r=(5*nn*(nn+1))/2
    print(r)
    return r




#..
def formula(nn):
    lim=5*nn
    ac=0.0
    for i in range(5,int(lim)+1,5):
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
