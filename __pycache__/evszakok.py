honap = int(input("Kérem a hónap számát:    "))
if honap > 12 or honap < 1:
    honap = int(input("A hónap száma nem helyes kérlek adj meg létező hónapszámot:      "))

if honap == 12 or honap == 1 or honap == 2:
    print("Az adott hónap télen van.")

if honap == 3 or honap == 4 or honap == 5:
    print("Az adott hónap tavasszal van")

if honap == 6 or honap == 7 or honap == 8:
    print("Az adott hónap nyáron van")

if honap == 9 or honap == 10 or honap == 11:
    print("Az adott hónap ősszel van")