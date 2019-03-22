#En una granja se contaron 94 patas y 35 cabezas de animales
#Se sabe que hay conejos y gallinas
#Cuantos animales hay de cada tipo


conejos=1

total=conejos*4
indicador=True
patas=94-total
patasGallina= patas/2

while(indicador):
    patasConejos=conejos*4
    gallinas=((94-patasConejos)/2)
    if((conejos+gallinas)!=35):
        conejos=conejos+1
    else:
        indicador=False

print("Hay:", conejos, "conejos y ", gallinas, "gallinas")
