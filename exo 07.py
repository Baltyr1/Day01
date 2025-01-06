"ex 7"
def comptage_voyelles():
    voyelles = ["a", "e", "i", "o", "u", "y"]
    nbr_voyelles = 0
    phrase = input("entre une phrase : ")
    for i in phrase:
        if i in voyelles:
            nbr_voyelles += 1
    return nbr_voyelles
print(comptage_voyelles())