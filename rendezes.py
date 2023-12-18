from random import randint

szamok1 = [randint(0,20) for _ in range(11)]
szamok2 = sorted(szamok1,reverse=True)
novekvo = szamok2[:len(szamok2)//2]
csokkeno = szamok2[len(szamok2)//2:]
csokkeno.sort(reverse=True)
novekvo.sort()
szamokRendezett = novekvo + csokkeno
print(szamokRendezett)