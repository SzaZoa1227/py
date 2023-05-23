elsoSzam = int(input("Első szám:    "))
masodikSzam = int(input("Második szám:  "))
print(f"{elsoSzam}{masodikSzam}")
temp = elsoSzam
elsoSzam = masodikSzam
masodikSzam = temp
print(f"{elsoSzam}{masodikSzam}")