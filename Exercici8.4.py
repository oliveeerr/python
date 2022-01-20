print ("Aquest programa demana 7 números i te dona la suma d'aquests 7 ")
total=0 
negatiu=0
positiu=0
zero=0

for i in range(7):
        x = float(input("Introdueix un número"))
        if x > 0:
                positiu+=1
        elif x < 0:
                negatiu-=1
        else:
                zero+=1                
        total = total + x
print ("El total és:", total)
print ("Hi ha", positiu,"positius, hi ha", negatiu,"negatius hi ha", zero,"zeros")
