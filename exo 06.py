"ex 6"
from random import *

def devinettes():
    x = randint (1, 100)
    nbr_choisit = int(input("écrit un nombre entre 0 et 100 : "))
    while x != nbr_choisit:
        if x > nbr_choisit :
            print("le nombre est plus grand")
        if x < nbr_choisit:
            print("le nombre est plus petit")
        nbr_choisit = int(input(""))
    return "GOOD JOB"
print(devinettes())