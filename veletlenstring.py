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

##hazi beszamolni a kis es nagybetuket