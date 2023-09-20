n = 100
for i in range(2, n+1):
    nemPrim = True
    szam = 2
    while nemPrim and szam < i:
        if i % szam == 0:
            nemPrim = False
        szam += 1
    if nemPrim or i == 2:
        print(i)