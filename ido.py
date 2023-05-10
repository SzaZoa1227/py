elsoOra= int(input("Az első időpont órája:   "))
elsoPerc= int(input("Az első időpont perce:   "))
masodikOra=int(input("Az második időpont órája:   "))
masodikiPerc=int(input("Az második időpont perce:   "))

def percbeAlakitas(ora):
    return ora*60

elsoIdo = elsoPerc+percbeAlakitas(elsoOra)
masodikIdo = masodikPerc+percbeAlakitas(masodikOra)
elteltIdo1 = elsoIdo-masodikIdo
elteltIdo2 = elsoIdo-masodikIdo
print(f"A két időpont között eltelt {elteltIdo1} perc.")

def orabaAlakitas(idoPercben):
    idoOraban = 0
    while (idoPercben - 60) >= 60:
        idoOraban +=1
    return idoOraban
for i in range(0, orabaAlakitas(elteltIdo1)):
    elteltIdo -= 60

print(f"A két időpont között eltelt {orabaAlakitas(elteltIdo1)} óra és {elteltIdo2} perc.")