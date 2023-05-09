elsOra = int(input("Első időpont órája:     "))
elsoPerc = int(input("Első időpont perce:   "))
masodikOra = int(input("Második időpont órája:     "))
masodikiPerc = int(input("Második időpont perce:   "))


def percbeAlakitas():
    elsOra = elsOra*60
    masodikOra = masodikOra*60

elsoIdopont = elsOra+elsoPerc
masodikIdonpont = masodikOra+masodikiPerc

print(masodikIdonpont)
print(elsoIdopont)
print(f"A két időpont között eltelt {masodikIdonpont - elsoIdopont} perc")
