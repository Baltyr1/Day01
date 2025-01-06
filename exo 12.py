"ex 12"
def mot_de_passe():
    caractere = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '%' , '_' , '-' , '!' , '$' , '^' , '&' , '#' , '(' , ')' , '[' , ']' , '=' , '@', '0', '1' ,'2' , '3' , '4' , '5' , '6' , '7' , '8' ,'9']
    mot_de_passe = []
    n = int(input("entre le nombre de caractere : "))
    for i in range(n):
        x = randint(1, len(caractere))
        mot_de_passe.append(caractere[x])
    return "".join(mot_de_passe)
print(mot_de_passe())
