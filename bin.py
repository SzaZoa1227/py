szam = int(input("Kérem az átalakítandó számot:     "))
binErtek = []
def bin(num):
     
    if num >= 1:
        bin(num // 2)
    binErtek.append(num % 2)
print(binErtek)