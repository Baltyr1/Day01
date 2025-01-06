"ex 15"
def nombre_mystere():
    x = randint(1, 1000)
    nbr_choisit = int(input("écrit un nombre entre 0 et 1000 : "))
    tentative = 9
    while x != nbr_choisit:
        if x > nbr_choisit:
            print("le nombre est plus grand")
        if x < nbr_choisit:
            print("le nombre est plus petit")
        nbr_choisit = int(input(""))
        tentative -= 1
        if tentative == 0:
            return "you lose"
    return "you win"
print(nombre_mystere())