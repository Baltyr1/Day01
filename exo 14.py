"ex 14"
def factoriel():
    nombre = int(input("entre un nombre : "))
    factoriel = 1
    for i in range(1, nombre+1):
        factoriel *= i
    return factoriel
print(factoriel())