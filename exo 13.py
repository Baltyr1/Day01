"ex 13"
def tri_liste():
    nombre = input("entre une liste de nopmbre separes par des ',' : ")
    liste_nombre = nombre.split(',')
    liste_nombre_croissant = sorted(liste_nombre)
    return liste_nombre_croissant
print(tri_liste())