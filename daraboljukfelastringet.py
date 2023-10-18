import random
karakterek = []
kisbetuk = ""
nagybetuk = ""
randomString = ""
for i in range(97,123):
    karakterek.append(chr(i))
    nagybetuk += (chr(i))
for i in range(65,91):
    karakterek.append(chr(i))
    kisbetuk += (chr(i))
for i in range(0,10):
    karakterek.append(str(i))
for i in range(25):
    randomString = randomString + karakterek[random.randint(0,len(karakterek)-1)]
print(randomString)
uj = ""
szamolo = 0
for betu in randomString:
    if szamolo%3==0 and szamolo != 0:
        uj += " "
    szamolo += 1
    uj += betu
print(uj)