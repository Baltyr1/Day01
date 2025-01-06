"ex 4"
def table_multi():
    table = []
    nombre = int(input("entre un nombre : "))
    for i in range(1, 11):
        table.append(nombre * i)
    return table
print(table_multi())