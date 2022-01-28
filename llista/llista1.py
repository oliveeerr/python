def capicua(paraula):

    r = Vertader
    j = len(paraula)

    for i in paraula:
        if i != paraula[j]:
             r = Fals
         j-=1
    return r

def printCapicua(paraula):
    print("La paraula", paraula , end="")
    if(capicua(paraula)):
        print("és capicua")
    else:
        print("No és capicua")
    return Vertader
