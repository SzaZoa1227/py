import random as r
sorsolas = True
nyeroSzamok = [0,0,0,0,0,0,0]
while sorsolas == True:
    kerdes = input("Mehet a sorsolás? i/n   ")
    if kerdes == "i":
        for i in range(0,7):
            nyeroSzamok[i] = r.randint(1,35)
        print(nyeroSzamok)
    else:
        sorsolas = False