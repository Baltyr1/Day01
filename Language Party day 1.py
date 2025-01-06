"ex 0"
#print("Hello world from Python !")

"ex 1"
def nom_age():
    nom = input("quel est ton nom : ")
    age = str(input("quel est ton age : "))
    return "tu as " + age + " ans " + nom
#print(nom_age())

"ex 2"
def calculatrice():
    calcul = (input("entre un calcul : "))
    return eval(calcul)
#print(calculatrice())

"ex 3"
def Fahrenheit():
    celsius = int(input("entre une temperature en celsius : "))
    Fahrenheit = (celsius * 9 / 5) + 32
    return Fahrenheit
#print(Fahrenheit())

"ex 4"
def table_multi():
    table = []
    nombre = int(input("entre un nombre : "))
    for i in range(1, 11):
        table.append(nombre * i)
    return table
#print(table_multi())

"ex 5"
def inverse_liste(liste):
    inv_liste = []
    for i in range(1, len(liste) + 1):
        inv_liste.append(liste[-i])
    return inv_liste
#print(inverse_liste([1,8,3,4,5]))

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
#print(devinettes())

"ex 7"
def comptage_voyelles():
    voyelles = ["a", "e", "i", "o", "u", "y"]
    nbr_voyelles = 0
    phrase = input("entre une phrase : ")
    for i in phrase:
        if i in voyelles:
            nbr_voyelles += 1
    return nbr_voyelles
#print(comptage_voyelles())

"ex 8"
def maximum():
    nombre1 = int(input("entre un 1er nombre : "))
    nombre2 = int(input("entre un 2em nombre : "))
    nombre3 = int(input("entre un 3em nombre : "))
    if nombre1 >= nombre2 and nombre1 >= nombre3:
        return nombre1
    if nombre2 >= nombre1 and nombre2 >= nombre3:
        return nombre2
    else:
        return nombre3
#print(maximum())

"ex 9"
def palindrome():
    mots = input("entre un mots : ")
    if mots == mots[::-1]:              #crée une copie inversee de l'objet d'origine
        return "c'est un palindrome"
    else:
        return "ce n'est pas un palindrome"
#print(palindrome())

"ex 10"
def moyenne_notes():
    nbr_notes = 1
    notes = input("entre des notes separes par des ',' : ")
    add_notes = notes.replace("," ,"+")
    for i in add_notes:
        if i == "+":
            nbr_notes += 1
    return eval(add_notes)/nbr_notes
#print(moyenne_notes())

"ex 11"
def FizzBuzz():
    for i in range(1, 101):
        if i%3 == 0 and i%5 != 0:
            print('Fizz')
        if i%5 == 0 and i%3 != 0:
            print('Buzz')
        if i%3 == 0 and i%5 == 0:
            print('FizzBuzz')
        else:
            print(i)
#print(FizzBuzz())

"ex 12"
def mot_de_passe():
    caractere = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '%' , '_' , '-' , '!' , '$' , '^' , '&' , '#' , '(' , ')' , '[' , ']' , '=' , '@', '0', '1' ,'2' , '3' , '4' , '5' , '6' , '7' , '8' ,'9']
    mot_de_passe = []
    n = int(input("entre le nombre de caractere : "))
    for i in range(n):
        x = randint(1, len(caractere))
        mot_de_passe.append(caractere[x])
    return "".join(mot_de_passe)
#print(mot_de_passe())

"ex 13"
def tri_liste():
    nombre = input("entre une liste de nopmbre separes par des ',' : ")
    liste_nombre = nombre.split(',')
    liste_nombre_croissant = sorted(liste_nombre)
    return liste_nombre_croissant
#print(tri_liste())

"ex 14"
def factoriel():
    nombre = int(input("entre un nombre : "))
    factoriel = 1
    for i in range(1, nombre+1):
        factoriel *= i
    return factoriel
#print(factoriel())

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