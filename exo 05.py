"ex 5"
def inverse_liste(liste):
    inv_liste = []
    for i in range(1, len(liste) + 1):
        inv_liste.append(liste[-i])
    return inv_liste
print(inverse_liste([1,8,3,4,5]))