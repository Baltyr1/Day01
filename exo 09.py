"ex 9"
def palindrome():
    mots = input("entre un mots : ")
    if mots == mots[::-1]:              #crée une copie inversee de l'objet d'origine
        return "c'est un palindrome"
    else:
        return "ce n'est pas un palindrome"
print(palindrome())