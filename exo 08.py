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
print(maximum())