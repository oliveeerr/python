import random
x=random.randrange(0,3)
""""

Pedra=0
Paper=1
Tisores=2

"""
#print(x)
y=int(input("Introdueix pedra=0 paper=1 o tisores=2: "))
if x == 0 and y == 1 or x == 1 and y == 2 or x == 2 and y == 0:
    print("Has guanyat")
elif x == 0 and y == 0 or x == 1 and y == 1 or x == 2 and y == 2:
    print("has empatat")
else:
    print("has perdut")