kezd = float(input("Adj meg egy kezdőértéket:             "))
dif = float(input("Írj be egy számot differenciálnak!     "))
n = int(input("Add meg, hogy mennyi számot írjunk ki!   "))
szam = kezd + dif
print(kezd)
for i in range(n):
    print(round(szam,8))
    szam += dif
    