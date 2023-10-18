def hatvany(a,k):
    eredmeny = 1
    if k == 0: return 1
    for i in range(0,k):
        eredmeny *= a
    print(eredmeny)

hatvany(int(input("Hatványalap  ")),int(input("Hatványkitevő    ")))