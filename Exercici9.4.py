import random
cara=0
creu=0
for i in range(50):
    x = random.randrange(0,2)
    if (x == 0):
        cara+=1
    else:
        creu+=1
print("Hi ha",cara,"cares hi ha",creu,"creus")