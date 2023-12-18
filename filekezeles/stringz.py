fajl = open("fa.txt","wt")
szoveg = "    *\n"
sSz = 3
for i in range(1,4):
        szoveg += sSz*" " + "*" + ((i*2)-1)*" "+"*\n"
        sSz -= 1
szoveg += 9*"*" + "\n"
for i in range(2):
    szoveg += 4*" " + "*\n"
print(szoveg)

fajl.write(szoveg)