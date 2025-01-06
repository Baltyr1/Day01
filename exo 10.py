"ex 10"
def moyenne_notes():
    nbr_notes = 1
    notes = input("entre des notes separes par des ',' : ")
    add_notes = notes.replace("," ,"+")
    for i in add_notes:
        if i == "+":
            nbr_notes += 1
    return eval(add_notes)/nbr_notes
print(moyenne_notes())