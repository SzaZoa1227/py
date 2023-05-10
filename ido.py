elsoOra = int(input("Az első időpont órája: "))
elsoPerc = int(input("Az első időpont perce: "))
masodikOra = int(input("Az második időpont órája: "))
masodikPerc = int(input("Az második időpont perce: "))

elsoIdo = elsoOra * 60 + elsoPerc
# print(elsoIdo)
masodikIdo = masodikOra * 60 + masodikPerc
# print(masodikIdo)
elteltIdo = masodikIdo - elsoIdo
#print(elteltIdo)

orak = elteltIdo // 60
# print(orak)
percek = elteltIdo % 60
# print(percek)

print(f"A két időpont között eltelt {orak} óra és {percek} perc.")
