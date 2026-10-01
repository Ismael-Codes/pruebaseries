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
     n=float(input("Dame n"))
     r=ecuacion(n)
     r2=formula(n)

     if r==r2:
        print("Si son equivalentes")
     else:
        print("No son equivalentes")



