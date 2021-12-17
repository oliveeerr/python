print("Bienvenidos a la Ultra Trail!")
 
print("A. Banquero")
print("B. Carpintero")
print("C. Granjero")
 
entrada_usuario = input("¿Cuál es tu profesión?")
 
if entrada_usuario == "A":
    dinero = 100
if entrada_usuario == "B":
    dinero = 70
if entrada_usuario == "C":
    dinero = 50
     
print("Genial! empezarás el juego con", dinero, "dólares.")