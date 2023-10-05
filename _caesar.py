def caesar(szoveg, eltolas):
    ujszoveg  = ""
    for betu in szoveg:
        if betu.isalpha():
            kezdes = ord('A') if betu.isupper() else ord('a')
            betueltolas = chr((ord(betu) - kezdes + eltolas) % 26 + kezdes) #ord(betu) - kezdes: átalakítja a betűt pl A az 65 abból lesz 0
            ujszoveg  += betueltolas                                        #ord(betu - kezdes + eltolas) % 26 maradékosan osztja, így ha az eltolás 
                                                                            #több mint 26 akkor előröl kezdi a számozást Z nem 66 lesz,ha 1 az eltolás,hanem 1.
        else:                                                               #   + kezdes a végén visszaalakítja unicode karakterré. az else a nem az ábécé részét képző karaktereknek van.
            ujszoveg  += betu
    return ujszoveg 

szoveg = input("Írd be a szöveget amit el akarsz tolni!     ")
eltolas = int(input("Add meg az eltolás mértékét! (egész szám) "))
ujszoveg = caesar(szoveg, eltolas)
print(f"A kódolt szöveged:  {ujszoveg}")