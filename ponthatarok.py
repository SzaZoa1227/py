osszpont = int(input("Írd be az összpontszámot:     "))
elertPontszam = int(input("Írd be az elért pontszámot:      "))
szazalek = int((elertPontszam/osszpont)*100)
if szazalek < 40:
    print(f"{szazalek}%, Elégtelen(1)")
elif szazalek < 55:
    print(f"{szazalek}%, Elégséges(2)")
elif szazalek < 70:
    print(f"{szazalek}%, Közepes(3)")
elif szazalek < 85:
    print(f"{szazalek}%, Jó(4)")
else:
    print(f"{szazalek}%, Jeles(5)")