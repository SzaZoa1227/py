bekertJegy = 1
while bekertJegy != 0:
    bekertJegy = int(input("Kérem az érdemjegyet"))
    if bekertJegy == 1:
        print("Elégtelen")
    elif bekertJegy == 2:
        print("Elégséges")
    elif bekertJegy == 3:
        print("Közepes")
    elif bekertJegy == 4:
        print("Jó")
    elif bekertJegy == 5:
        print("Jeles")
    else:
        print("A megadott érdemjegy nem megfelelő!")


